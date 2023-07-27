from funcionario import Funcionario

class Recepcionista(Funcionario):
    """
    Representa um recepcionista, que herda atributos da classe Funcionario

    Attributes
    ---------
    cpf : str
        CPF do recepcionista.
    nome : str
        Nome do recepcionista.
    telefone : str 
        Numero de telefone do recepcionista.
    dt_nasc : str
        Data de nascimento do recepcionista.
    email : str
        Endereco de e-mail do recepcionista.
    senha : str
        Senha do recepcionista para fins de autenticacao.
    """

    def __init__(self, cpf, nome, telefone, dt_nasc, email, senha):
        """
        Paramethers
        -----------
        cpf : str
            CPF do recepcionista.
        nome : str
            Nome do recepcionista.
        telefone : str 
            Numero de telefone do recepcionista.
        dt_nasc : str
            Data de nascimento do recepcionista.
        email : str
            Endereco de e-mail do recepcionista.
        senha : str
            Senha do recepcionista para fins de autenticacao.
        """
        super().__init__(cpf, nome, telefone, dt_nasc, email)
        self._senha = senha

    @property
    def cpf(self):
        return self._cpf
  

    
    