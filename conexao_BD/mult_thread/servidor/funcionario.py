class Funcionario():
    """
    Representa um funcionario.

    Attributes
    ---------
    cpf : str
        CPF do funcionario.
    nome : str
        Nome do medico.
    telefone : str 
        Numero de telefone do funcionario.
    dt_nasc : str
        Data de nascimento do funcionario.
    email : str
        Endereco de e-mail do funcionario.
    """
    def __init__(self, cpf, nome, telefone, dt_nasc, email):
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
        """
        self._cpf = cpf
        self._nome = nome
        self._telefone = telefone
        self._dt_nasc = dt_nasc
        self._email = email
    
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
    def dt_nasc(self):
        return self._dt_nasc

    @dt_nasc.setter
    def dt_nasc(self, dt_nasc):
        self._dt_nasc = dt_nasc
    
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email
    

    