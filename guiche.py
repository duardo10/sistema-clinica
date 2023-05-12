class Guiche():
    """
    A classe Guichê é responsavel por receber os paciente através de um sistema de senhas para que então seja realizada
    a fixa de consulta. recebe como atributos o numero do Guichê o stsatus dele(livre/ocupado) o paciente e a senha do paciente para
    que então seja chamada a próxima senha. 
    """
    def __init__(self, id_guiche, status, paciente, senha):
        self._id_guiche = id_guiche
        self._status = status
        self._paciente = paciente
        self._senha = senha
        

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
    """
    def iniciar_atendimento(self, cliente, ident):
        if self._status == 'livre':
            self._id_guiche = ident
            self._paciente = cliente
            self._status = 'ocupado'
            self._senha += 1
            return True
        else:
            return False


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
        if self._status == 'ocupado':
            self._paciente = None
            self._status = 'livre'
            return True
        else:
            return False