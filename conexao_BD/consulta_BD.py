import mysql.connector

class Consulta():
    def __init__(self):
        # configurações da conexão com o banco de dados 
        self.connection = mysql.connector.connect(
            user = 'root',
            password = '',
            host = 'localhost',
            database = 'mydb',
        )
    def verificar_tipo(self,cpf):
        """
        A função de verificar o tipo de consulta se é uma nova consulta ou se é o retorno do paciente ao médico:
        se a consulta for do tipo retorno ela retorna False é porque o paciente já pagou a consulta, portanto não é cobrado nenhum
        valor para a consulta. Mas se for uma nova consulta a função retorna True e então é cobrado na recepção o valor da consulta
        #parâmetros:#
            - sem parâmetros
        #retorno#
            - boll = True ou False
        """
        try:
            cursor = self.connection.cursor()
            sql = "SELECT tipo_consulta FROM consulta WHERE cpf_paciente = %s"
            cursor.execute(sql,(cpf,))
            tipo_consulta = cursor.fetchone()
            self.connection.commit()
            if tipo_consulta[0] == 'retorno':
                return False
            else:
                return True
            
        except mysql.connector.Error as error:
            print(f'Eroo ao verificar um dado: {error}')
        finally:
            cursor.close()

    def excluir_consulta(self, cpf_paciente):
        # A função de excluir uma consulta recebe como parâmetros o cpf do cliente para que após 30 dias da primieira consulta
        # se o paciente não tiver voltado para o retorno, o recepcionista excluir os dados do paciente. caso o cliente tenha
        # retornado antes dos 30 dias. após o retorno já é excluido imediatamente os dados do cliente. 
        try:
            cursor = self.connection.cursor()
            sql = "DELETE FROM consulta WHERE cpf_paciente = %s"
            cursor.execute(sql,(cpf_paciente,))
            self.connection.commit()
            print('Dado excluido')
        except mysql.connector.Error as error:
            print(f'Eroo ao excluir um dado: {error}')
        finally:
            cursor.close()

    def vagas_disponiveis(self, medico):
        try:
            cursor = self.connection.cursor()
            medico_responsavel = "SELECT nome, qtd_vagas FROM medico"
            cursor.execute(medico_responsavel)
            selecionar = cursor.fetchall()
            for dado in selecionar:
                if dado[0] == medico:
                    qtd_vagas = dado[1]
                    if qtd_vagas == 0:
                        return False
                    else:
                        qtd_vagas -= 1
                        atualiza =  "UPDATE medico SET qtd_vagas = %s"
                        cursor.execute(atualiza,(qtd_vagas,))
                        return qtd_vagas
        
        except mysql.connector.Error as error:
            print(f'Eroo ao atualizar a quantidade de vagas de um medico no banco de dados: {error}')
        finally:
            cursor.close()

    def enviar_consulta(self):
        # A função de enviar uma consulta recebe como parâmetro uma consulta que deve ser enviada pelo recepcionista para o
        # médico responsável pelo paciente.
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM consulta ORDER BY id_consulta DESC LIMIT 1 ")
            ultimo_elemento = cursor.fetchone()
            print(ultimo_elemento)
            
            retorno = self.vagas_disponiveis(ultimo_elemento[4])
            if retorno == False:
                print('Não há mais vagas para este médico')
            else:
                print('Quantidade de vagas: ', retorno)
                cpf = ultimo_elemento[1]
                nome = ultimo_elemento[2]
                medico = ultimo_elemento[4]
                sql = "INSERT INTO lista_pacientes (cpf,nome,medico) VALUES (%s,%s,%s)"
                cursor.execute(sql,(cpf,nome,medico,))
                self.connection.commit()
            
                print('Paciente enviado para a lista de pacientes')
        except mysql.connector.Error as error:
            print(f'Eroo ao enviar um dado para a lista de pacientes: {error}')
        finally:
            cursor.close()
        
    def fechar_conecao(self):
        self.connection.close()
        




    