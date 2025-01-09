from Classes import Sistema

def cadastrar_paciente(sistema):
    print("\n=== CADASTRAR PACIENTE ===")
    nome = input("Digite o nome do paciente: ")
    idade = int(input("Digite a idade do paciente: "))
    laudo = input("Digite o laudo do paciente: ")
    sistema.cadastrar_paciente(nome, idade, laudo)
    print("Paciente cadastrado com sucesso!")

def cadastrar_cavalo(sistema):
    print("\n=== CADASTRAR CAVALO ===")
    nome = input("Digite o nome do cavalo: ")
    sistema.cadastrar_cavalo(nome)
    print("Cavalo cadastrado com sucesso!")

def cadastrar_percurso_desafios(sistema):
    print("\n=== CADASTRAR PERCURSO ===")
    nome_percurso = input("Digite o nome do percurso: ")
    percurso = sistema.cadastrar_percurso(nome_percurso)

    while True:
        print("\nAdicionar desafio ao percurso:")
        nome_desafio = input("Digite o nome do desafio: ")
        descricao = input("Digite a descrição do desafio: ")
        sistema.cadastrar_desafio(percurso, nome_desafio, descricao)

        opcao = input("Deseja adicionar outro desafio? (S/N): ").strip().upper()
        if opcao != "S":
            break

def agendar_sessao(sistema):
    print("\n=== AGENDAR SESSÃO ===")
    dia = input("Digite o dia da sessão: ")
    horario = input("Digite o horário da sessão: ")

    # Selecionar paciente
    if sistema.pacientes:
        print("\nPacientes cadastrados:")
        for i, paciente in enumerate(sistema.pacientes, start=1):
            print(f"{i}. {paciente.nome}")
        while True:
            try:
                indice_paciente = int(input("Escolha o paciente pelo número: ")) - 1
                if 0 <= indice_paciente < len(sistema.pacientes):
                    break
                else:
                    print("Número inválido. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número.")
    else:
        print("Nenhum paciente cadastrado.")
        return

    # Selecionar cavalo
    if sistema.cavalos:
        print("\nCavalos cadastrados:")
        for i, cavalo in enumerate(sistema.cavalos, start=1):
            print(f"{i}. {cavalo.nome}")
        while True:
            try:
                indice_cavalo = int(input("Escolha o cavalo pelo número: ")) - 1
                if 0 <= indice_cavalo < len(sistema.cavalos):
                    break
                else:
                    print("Número inválido. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número.")
    else:
        print("Nenhum cavalo cadastrado.")
        return

    # Selecionar percurso
    if sistema.percursos:
        print("\nPercursos cadastrados:")
        for i, percurso in enumerate(sistema.percursos, start=1):
            print(f"{i}. {percurso.nome}")
        while True:
            try:
                indice_percurso = int(input("Escolha o percurso pelo número: ")) - 1
                if 0 <= indice_percurso < len(sistema.percursos):
                    break
                else:
                    print("Número inválido. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número.")
    else:
        print("Nenhum percurso cadastrado.")
        return

    sistema.agendar_sessao(
        dia,
        horario,
        sistema.pacientes[indice_paciente],
        sistema.cavalos[indice_cavalo],
        sistema.percursos[indice_percurso],
    )
    print("Sessão agendada com sucesso!")

def menu_principal():
    sistema = Sistema()

    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Cadastrar Paciente")
        print("2. Cadastrar Cavalo")
        print("3. Cadastrar Percurso e Desafios")
        print("4. Agendar Sessão")
        print("5. Salvar dados")
        print("6. Listar Cronograma")
        print("7. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_paciente(sistema)
        elif opcao == "2":
            cadastrar_cavalo(sistema)
        elif opcao == "3":
            cadastrar_percurso_desafios(sistema)
        elif opcao == "4":
            agendar_sessao(sistema)
        elif opcao == "5":
            sistema.salvar_json()
        elif opcao == "6":
            sistema.listar_agendamentos()
        elif opcao == "7":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()

