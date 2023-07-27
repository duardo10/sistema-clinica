class Guiche():
    """
    Representa um guichê de atendimento.

    Attributes
    ---------
    id_guiche : int
        Identificacao do guiche
    status : str
        Status do guiche(livre|ocupado)
    senha : str
        Senha do guiche
    modo : str
        Modo do guiche(ativo|inativo)
    """
    def __init__(self, id_guiche, status, senha, modo):
        """
         Paramethers
        -----------
        id_guiche : int
            Identificacao do guiche
        status : str
            Status do guiche(livre|ocupado)
        senha : str
            Senha do guiche
        modo : str
            Modo do guiche(ativo|inativo)
        """
        self._id_guiche = id_guiche
        self._status = status
        self._senha = senha
        self._modo = modo
    
    def get_id_guiche(self):
        return self._id_guiche

    def set_id_guiche(self, id_guiche):
        self._id_guiche = id_guiche

    def get_status(self):
        return self._status

    def set_status(self, status):
        self._status = status

    def get_senha(self):
        return self._senha

    def set_senha(self, senha):
        self._senha = senha

    def get_modo(self):
        return self._modo

    def set_modo(self, modo):
        self._modo = modo