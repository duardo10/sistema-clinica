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

    def excluir_consulta(self, cpf_paciente, dc_consulta):
        # A função de excluir uma consulta recebe como parâmetros o cpf do cliente para que após 30 dias da primieira consulta
        # se o paciente não tiver voltado para o retorno, o recepcionista excluir os dados do paciente. caso o cliente tenha
        # retornado antes dos 30 dias. após o retorno já é excluido imediatamente os dados do cliente. 
        if cpf_paciente in dc_consulta:
            del(dc_consulta[cpf_paciente])
            return dc_consulta
        else:
            return False

    def enviar_consulta(self, dc_consulta):
        # A função de enviar uma consulta recebe como parâmetro uma consulta que deve ser enviada pelo recepcionista para o
        # médico responsável pelo paciente.
        for valor in dc_consulta.values():
            return self._nome_paciente




    