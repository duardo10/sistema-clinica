from funcionario import Funcionario

class Medico(Funcionario):
    """
    Representa um médico, que herda da classe Funcionario.

    Attributes
    ---------
    cpf : str
        CPF do medico.
    nome : str
        Nome do medico.
    telefone : str 
        Numero de telefone do medico.
    dt_nasc : str
        Data de nascimento do medico.
    email : str
        Endereco de e-mail do medico.
    especialidade : str
        Especialidade do medico.
    hr_atendimento : str
        Hora de atendimento do medico
    crm : int 
        CRM do medico
    senha : str
        senha do medico 
    """
    def __init__(self, cpf, nome, telefone, dt_nasc, email, especialidade, hr_atendimento, crm,senha):
        """
        Paramethers
        -----------
        cpf : str
            CPF do medico.
        nome : str
            Nome do medico.
        telefone : str 
            Numero de telefone do medico.
        dt_nasc : str
            Data de nascimento do medico.
        email : str
            Endereco de e-mail do medico.
        especialidade : str
            Especialidade do medico.
        hr_atendimento : str
            Hora de atendimento do medico
        crm : int 
            CRM do medico
        senha : str
            senha do medico 
        """
        super().__init__(cpf, nome, telefone, dt_nasc, email)
        self._especialidade = especialidade
        self._hr_atendimento = hr_atendimento
        self._crm = crm
        self._senha = senha
    
    @property
    def cpf(self):
        return self._cpf

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, telefone):
        self._telefone = telefone
    
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def especialidade(self):
        return self._especialidade

    @especialidade.setter
    def especialidade(self, especialidade):
        self._especialidade = especialidade
    
    @property
    def hora_atendimento(self):
        return self._hr_atendimento

    @hora_atendimento.setter
    def hora_atendimento(self, hr_atendimento):
        self._hr_atendimento = hr_atendimento

    @property
    def crm(self):
        return self._crm

    @crm.setter
    def crm(self, crm):
        self._crm = crm

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, senha):
        self._senha = senha
    
        

    


    
    
        