from funcionario import Funcionario

class Medico(Funcionario):
    """
    A classe do médico recebe como parâmetros os dados do médico e uma lista de pacientes que irão ser atendidos por ele durante o dia
    #Parâmetros utilizados#
        cpf: str
        nome: str
        telefone: str
        dt_nasc: str
        especialidade: str
        hr_atendimento: str
        crm: int
        lista_pacientes: list
    """
    def __init__(self, cpf, nome, telefone, dt_nasc, email, especialidade, hr_atendimento, crm, qtd_vagas):
        super().__init__(cpf, nome, telefone, dt_nasc, email)
        self._especialidade = especialidade
        self._hr_atendimento = hr_atendimento
        self._crm = crm
        self._qtd_vagas = qtd_vagas
    
    def vagas_disponiveis(self):
        if self._qtd_vagas > 0:
            self._qtd_vagas -= 1
            print(self._qtd_vagas)
            return True
        else:
            return False

    def imprimir(self):
        print('CPF: ', self._cpf)
        print('Nome: ', self._nome)
        print('Telefone: ', self._telefone)
        print('Data de nascimento: ', self._dt_nasc)
        print('Email: ', self._email)
        print('Especialidade: ', self._especialidade)
        print('Hora de atendimento: ', self._hr_atendimento)
        print('CRM: ', self._crm)
    
    def imprimir_lista_de_pacientes(self, lista_paciente):
        for paciente in lista_paciente:
            print(paciente)


    def excluir(self, nome, lista_paciente):
        """
        Na função de excluir o médico responsável irá excluir na sua lista os pacientes que já foram atendidos por ele 
        #parâmetros:#
            lista_paciente
            nome
        A lista de paciente contém os pacientes que irão ser atendidos naquele dia de trabalho.
        #retorno:#
            lista_paciente 
        O retorno da função é a lista depois de ter excluido o paciente que foi atendido
        """
        if nome in lista_paciente:
            lista_paciente.remove(nome)
            return lista_paciente
        else:
            print('Paciennte não encontrado')

        

    


    
    
        """
        A função imprimir tem como objetivo imprimir os dados de um médico de acordo com o seu CPF
        parametros:
            #Parâmetros utilizados#
                cpf: str
                nome: str
                telefone: str
                data de nascimento: str

            
        Retorno:
            'seu retorno'
            ex:
            bool
            (bool,str)

        """
        """
        print('CPF: ', self._cpf)
        print('nome: ', self._nome)
        print('telefone: ', self._telefone)
        print('data de nascimento: ', self.dt_nasc)
        print('email: ', self._email)
        print('especialidade: ', self._especialidade)
        print('hora de atendimento: ', self._hr_atendimento)
        print('CRM: ', self._crm)

        """
