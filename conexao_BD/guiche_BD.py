import mysql.connector
class Guiche():
    """
    A classe Guichê é responsavel por receber os paciente através de um sistema de senhas para que então seja realizada
    a fixa de consulta. recebe como atributos o numero do Guichê o stsatus dele(livre/ocupado) o paciente e a senha do paciente para
    que então seja chamada a próxima senha. 
    """
    def __init__(self):
         # configurações da conexão com o banco de dados 
        self.connection = mysql.connector.connect(
            user = 'root',
            password = '',
            host = 'localhost',
            database = 'mydb',
        )
        
    
    """
    A função de iniciar atendimento, quando abre a clinica o staus dos Guichês são livres, porém quando é chamada uma nova senha,
    O status do Guichê ficará ocupado e o atributo senha é incrementado para quando o atendimento for finalizado o recepcionista
    chamar a proxima senha. A função irá retornar True se o status do Guichê for livre, e False se for ocupado. os parâmetros 
    utilizados foram um cliente e o numero do Guichê
    #Parâmetros:#
        cliente = object
        ident = int
    #Retorno:#
        boll = (True ou False)
  
    def atualizar_senha(self):
        try:
            cursor = self.connection.cursor()
            selecionar =  "SELECT * FROM guiche"
            cursor.execute(selecionar)
            selecionar = cursor.fetchall()
            print(selecionar)
            for dado in selecionar:
                if dado[3] == 'ativo':
                    if dado[1] == 'livre':
                        guiche = dado[0]
                        senha = dado[2]
                        senha += 1
                        print(senha)
                        atualiza =  "UPDATE guiche SET senha = %s"
                        status_guiche = "UPDATE guiche SET status = 'ocupado' WHERE id_guiche == %s"
                        cursor.execute(atualiza,status_guiche,(senha,guiche,))
                        #confirmar da atualização da senha
                        self.connection.commit()

                    
                        
                elif dado[3] == 'inativo':
                    print('inativo')
                    print(dado[0])
                else:
                    print('Guiche está no modo errado! cadastre ele em ativo ou inativo')
        
        except mysql.connector.Error as error:
            print(f'Eroo ao iniciar atendimento em um guiche no banco de dados: {error}')
        finally:
            cursor.close()
        """
    def atualizar_senha(self):
        try:
            cursor = self.connection.cursor()
            selecionar =  "SELECT * FROM guiche"
            cursor.execute(selecionar)
            selecionar = cursor.fetchall()
            for dado in selecionar:
                if dado[3] == 'ativo':
                    if dado[1] == 'livre':
                        senha = dado[2]
                        senha += 1
                        atualiza =  "UPDATE guiche SET senha = %s"
                        cursor.execute(atualiza,(senha,))
                        #confirmar da atualização da senha
                        self.connection.commit()
        
        except mysql.connector.Error as error:
            print(f'Eroo ao atualizar uma senha no banco de dados: {error}')
        finally:
            cursor.close()
        
    def iniciar_atendimento(self):
        try:
            cursor = self.connection.cursor()
            # Encontre o primeiro guichê livre
            consulta = "SELECT id_guiche FROM guiche WHERE status = 'livre' LIMIT 1"
            cursor.execute(consulta)
            resultado = cursor.fetchone()

            # Verifica se encontrou um guichê livre
            if resultado:
                id_guiche_livre = resultado[0]
                
                self.atualizar_senha()
                chamada = "SELECT senha FROM guiche WHERE id_guiche = %s"
                cursor.execute(chamada,(id_guiche_livre,))
                resultado = cursor.fetchone()
                print('Senha: {}, se dirija ao Guiche {}'.format(resultado[0], id_guiche_livre))
                # Atualiza o status do guichê para "ocupado"
                atualizacao = "UPDATE guiche SET status = 'ocupado' WHERE id_guiche = %s"
                cursor.execute(atualizacao, (id_guiche_livre,))
                self.connection.commit()
                print('Guichê', id_guiche_livre, 'agora está ocupado.')
            else:
                print('Não há guichês disponíveis no momento.')
            
        except mysql.connector.Error as error:
            print(f'Eroo ao iniciar atendimento em um guiche no banco de dados: {error}')
        finally:
            cursor.close()
        



    """
    A função de finalizar o atendimento, quando o staus do Guichê é ocupado, é porque há um paciente sendo atendido, ao realizar 
    o atendimento desse paciente o Guiche fica livre, e pode ser realizado um novo atendimento quando o atendimento for finalizado 
    o recepcionista chama a proxima senha. A função irá retornar True se o status do Guichê for ocupado, e False se for livre. 
    #Parâmetros:#
        - sem parâmetros
    #Retorno:#
        boll = (True ou False)
    """    
    def finalizar_atendimento(self):
        try:
            cursor = self.connection.cursor()
            consulta = "SELECT id_guiche FROM guiche WHERE status = 'ocupado'"
            cursor.execute(consulta)
            resultado = cursor.fetchall()
            guiche = int(input('Numero do Guiche que deseja finalizar o atendimento: '))
            guiche_encontrado = False
            for dado in resultado:
                if dado[0] == guiche:
                    atualiza = "UPDATE guiche SET status = 'livre' WHERE id_guiche = %s"
                    cursor.execute(atualiza,(guiche,))
                    self.connection.commit()
                    print('Guiche', guiche,' agora está liberado!') 
                    guiche_encontrado = True  # Atualiza a variável de controle
                    break  # Encerra o loop após encontrar o guichê correspondente
            
            if not guiche_encontrado:  # Verifica se o guichê foi encontrado
                print('O Guichê já está liberado!') 
                

            
        except mysql.connector.Error as error:
            print(f'Eroo ao finalizar um atendimento em um guiche no banco de dados: {error}')
        finally:
            cursor.close()
        
    def ativarGuiche(self, ident_guiche):
        try:
            cursor = self.connection.cursor()
            busc = "SELECT id_guiche,modo FROM guiche"
            cursor.execute(busc)
            busc = cursor.fetchall()
            self.connection.commit()
           
            for dado in busc:
                if dado[0] == ident_guiche:
                    if dado[1] == 'ativo':
                        return False
                    else:
                        return True
            
        except mysql.connector.Error as error:
            print(f'Eroo ao ativar um guiche no banco de dados: {error}')
        finally:
            cursor.close()

        
    
    def desativarGuiche(self, idt_guiche):
        try:
            cursor = self.connection.cursor()
            busc = "SELECT id_guiche,modo FROM guiche"
            cursor.execute(busc)
            busc = cursor.fetchall()
            self.connection.commit()
            for dado in busc:
                if dado[0] == idt_guiche:
                    if dado[1] == 'ativo':
                        return True
                    else:
                        return False
                
                """
                if dado[0] == ident_guiche:
                    if dado[1] == 'ativo':
                        return True
                    else:
                        return False
                else:
                    return None
                """
            
        except mysql.connector.Error as error:
            print(f'Eroo ao desativar um guiche no banco de dados: {error}')
        finally:
            cursor.close()
       