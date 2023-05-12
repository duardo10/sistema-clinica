class Pessoa():
    def __init__(self, cpf, nome, telefone,dt_nasc):
        self._cpf = cpf
        self._nome = nome
        self._telefone = telefone
        self._telefone = dt_nasc

class Funcionario(Pessoa):
    def __init__(self, cpf, nome, telefone, dt_nasc, email):
        super().__init__(cpf, nome, telefone, dt_nasc)
        self._email = email

class Paciente(Pessoa):
    def __init__(self, cpf, nome, telefone, dt_nasc, idade):
        super().__init__(cpf, nome, telefone, dt_nasc)
        self._idade = idade      

class Recepcionista(Funcionario):
    def __init__(self, cpf, nome, telefone, dt_nasc, email):
        super().__init__(cpf, nome, telefone, dt_nasc, email)

class Medico(Funcionario):
    def __init__(self, cpf, nome, telefone, dt_nasc, email, especialidade, hr_atendimento, crm):
        super().__init__(cpf, nome, telefone, dt_nasc, email)
        self._especialidade = especialidade
        self._hr_atendimento = hr_atendimento
        self._crm = crm

class Consulta():
    def __init__(self, cpf_paciente, nome_paciente,idade_paciente, medico, crm, tipo_consulta, hr_consulta):
        self._cpf_paciente = cpf_paciente
        self._nome_paciente = nome_paciente
        self._idade_paciente = idade_paciente
        self._medico = medico
        self._crm = crm
        self._tipo_consulta = tipo_consulta
        self._hr_consulta = hr_consulta
        
class Agendamento():
    def __init__(self, cpf_paciente, nome_paciente, nm_medico, crm, especialidade, dt_consulta, hr_consulta, tipo_consulta):
        self._cpf_paciente = cpf_paciente
        self._nome_paciente = nome_paciente
        self._nm_medico = nm_medico
        self._cpf_paciente = cpf_paciente
        self._crm = crm
        self._especialidade = especialidade
        self._dt_consulta = dt_consulta
        self._hr_consulta = hr_consulta
        self._tipo_consulta = tipo_consulta

class Guiche():
    def __init__(self, id_guiche, status):
        self._id_guiche = id_guiche
        self._status = status
        



