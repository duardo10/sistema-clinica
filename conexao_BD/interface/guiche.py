class Guiche():
    """
    A classe Guichê é responsavel por receber os paciente através de um sistema de senhas para que então seja realizada
    a fixa de consulta. recebe como atributos o numero do Guichê o stsatus dele(livre/ocupado) o paciente e a senha do paciente para
    que então seja chamada a próxima senha. 
    """
    def __init__(self, id_guiche, status, senha, modo):
        self._id_guiche = id_guiche
        self._status = status
        self._senha = senha
        self._modo = modo