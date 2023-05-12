class Agendamento():
    """
    A classe agendamento recebe como parâmetros um paciente, um medico, a hora e a data da consulta, e o tipo de consulta(Retorno/nova consulta)
    #Parâmetros utilizados#
        paciente: object
        medico: object
        dt_consulta: str
        hr_atendimento: str
        tipo_consulta: str
    """
    def __init__(self, paciente, medico, dt_consulta, hr_consulta, tipo_consulta):
        self._paciente = paciente
        self._medico = medico
        self._dt_consulta = dt_consulta
        self._hr_consulta = hr_consulta
        self._tipo_consulta = tipo_consulta

    def imprimmir_agendamento(self):
        """
        A função de imprimir um agendamento tem como objetivo imprimir os dados de uma consulta:
        #paciente,#medico,data da consulta, hora da consulta e qual o tipo da consulta.
        #parâmetros:
            - sem parâmetros
        #retorno:
            - sem retorno
        """
        print('Nome do paciente: ', self._paciente)
        print('\nNome do Médico: ', self._medico)
        print('\nData da consulta: ', self._dt_consulta)
        print('\nHora da consulta: ', self._hr_consulta)
        print('\nTipo de consulta: ', self._tipo_consulta)
        

    def verificar_tipo(self):
        """
        A função de verificar o tipo de consulta se é uma nova consulta ou se é o retorno do paciente ao médico:
        se a consulta for do tipo retorno ela retorna False é porque o paciente já pagou a consulta, portanto não é cobrado nenhum
        valor para a consulta. Mas se for uma nova consulta a função retorna True e então é cobrado na recepção o valor da consulta
        #parâmetros:#
            - sem parâmetros
        #retorno#
            - boll = True ou False
        """
        if self._tipo_consulta == 'retorno':
            return False
        else:
            return True
        