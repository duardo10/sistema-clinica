class Consulta():
    """
    A classe da consulta recebe como parâmetros os dados do paciente,o medico responsável por realizar a consulta,
    o tipo de consulta (retorno/nova consulta) e a hora da consulta (hora que o médico chega)
    #Parâmetros utilizados#
        cpf_paciente: str
        nome_paciente: str
        dt_nasc: str
        especialidade: str
        hr_atendimento: str
        crm: int
        lista_pacientes: list
    """
    def __init__(self, cpf_paciente, nome_paciente,dt_nasc, medico, crm, tipo_consulta, hr_consulta):
        self._cpf_paciente = cpf_paciente
        self._nome_paciente = nome_paciente
        self._dt_nasc = dt_nasc
        self._medico = medico
        self._crm = crm
        self._tipo_consulta = tipo_consulta
        self._hr_consulta = hr_consulta

    def excluir_consulta(self, cpf_paciente):
        # A função de excluir uma consulta recebe como parâmetros o cpf do cliente para que após 30 dias da primieira consulta
        # se o paciente não tiver voltado para o retorno, o recepcionista excluir os dados do paciente. caso o cliente tenha
        # retornado antes dos 30 dias. após o retorno já é excluido imediatamente os dados do cliente. 
        pass

    def enviar_consulta(self, consulta):
        # A função de enviar uma consulta recebe como parâmetro uma consulta que deve ser enviada pelo recepcionista para o
        # médico responsável pelo paciente.
        pass



    