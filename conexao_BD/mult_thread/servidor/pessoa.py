class Pessoa():
    """
    Representa uma pessoa.

    Attributes
    ---------
    cpf : str
        CPF da pessoa.
    nome : str
        Nome da pessoa.
    telefone : str 
        Numero de telefone da pessoa.
    dt_nasc : str
        Data de nascimento da pessoa.
    """
    __slots__ = ['_cpf','_nome','_telefone','_dt_nasc']
    def __init__(self, cpf, nome, telefone,dt_nasc):
        """
        Paramethers
        -----------
        cpf : str
            CPF da pessoa.
        nome : str
            Nome da pessoa.
        telefone : str 
            Numero de telefone da pessoa.
        dt_nasc : str
            Data de nascimento da pessoa.
        """
        self._cpf = cpf
        self._nome = nome
        self._telefone = telefone
        self._telefone = dt_nasc
