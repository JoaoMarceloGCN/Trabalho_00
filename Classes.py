# Class_Equo.py
import json
import os

class Paciente:
    def __init__(self, nome, idade, laudo):
        self.nome = nome
        self.idade = idade
        self.laudo = laudo

class Cavalo:
    def __init__(self, nome):
        self.nome = nome

class Desafio:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao

class Percurso:
    def __init__(self, nome):
        self.nome = nome
        self.desafios = []

    def adicionar_desafio(self, desafio):
        self.desafios.append(desafio)

class Sessao:
    def __init__(self, dia, horario, paciente, cavalo, percurso):
        self.dia = dia
        self.horario = horario
        self.paciente = paciente
        self.cavalo = cavalo
        self.percurso = percurso

class Sistema:
    def __init__(self):
        self.pacientes = []
        self.cavalos = []
        self.percursos = []
        self.sessoes = []

    def cadastrar_paciente(self, nome, idade, laudo):
        paciente = Paciente(nome, idade, laudo)
        self.pacientes.append(paciente)

    def cadastrar_cavalo(self, nome):
        cavalo = Cavalo(nome)
        self.cavalos.append(cavalo)

    def cadastrar_percurso(self, nome):
        percurso = Percurso(nome)
        self.percursos.append(percurso)
        return percurso

    def cadastrar_desafio(self, percurso, nome, descricao):
        desafio = Desafio(nome, descricao)
        percurso.adicionar_desafio(desafio)

    def agendar_sessao(self, dia, horario, paciente, cavalo, percurso):
        sessao = Sessao(dia, horario, paciente, cavalo, percurso)
        self.sessoes.append(sessao)

    def salvar_json(self, caminho='dados.json'):
        dados = []
        for item in self.sessoes:
            dados.append({
                "dia": item.dia,
                "horario": item.horario,
                "nome_paciente": item.paciente.nome,
                "nome_cavalo": item.cavalo.nome,
                "nome_percurso": item.percurso.nome,
            })
        with open(caminho, "w") as arquivo:
            json.dump(dados, arquivo, indent=4)
        print(f'Dados salvos em {caminho}!')

    def listar_agendamentos(self, caminho="dados.json"):
        if not os.path.exists(caminho):
            print(f'Arquivo {caminho} não encontrado!')
            return

        with open(caminho, "r") as arquivo:
            dados = json.load(arquivo)

        print(f'Dados carregados de {caminho}')
        for item in dados:
            print(f"\nDia: {item['dia']}, Horário: {item['horario']}")
            print(f"Paciente: {item['nome_paciente']}, Cavalo: {item['nome_cavalo']}")
            print(f"Percurso: {item['nome_percurso']}")

#ENcapsluar usando if main

#Privar muitas coisas

#Mostrar como deve ser usado

#