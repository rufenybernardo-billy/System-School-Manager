import database

# cadastra uma nova turma
def cadastrar_turma():
    print("\n-- Cadastrar Turma --")
    classe = input("Classe (ex: 10, 11, 12): ")
    nome = input("Nome da turma (ex: A, B, C): ")
    turno = input("Turno (manha/tarde/noite): ")

    turmas = database.carregar("turmas")

    # verifica se a turma ja existe
    for t in turmas:
        if t["classe"] == classe and t["nome"] == nome:
            print("Essa turma ja existe.")
            return

    nova_turma = {
        "classe": classe,
        "nome": nome,
        "turno": turno
    }

    turmas.append(nova_turma)
    database.salvar("turmas", turmas)
    print(f"Turma {classe}{nome} cadastrada com sucesso!")

# lista todas as turmas
def listar_turmas():
    turmas = database.carregar("turmas")

    if len(turmas) == 0:
        print("\nNenhuma turma cadastrada.")
        return

    print("\n-- Lista de Turmas --")
    for i, t in enumerate(turmas, 1):
        print(f"{i}. Classe {t['classe']} | Turma {t['nome']} | Turno: {t['turno']}")

# devolve as turmas de uma classe especifica
def turmas_da_classe(classe):
    turmas = database.carregar("turmas")
    return [t for t in turmas if t["classe"] == classe]

# menu de turmas
def menu_turmas():
    while True:
        print("\n===== TURMAS =====")
        print("1. Cadastrar turma")
        print("2. Listar turmas")
        print("0. Voltar")
        opcao = input("Opcao: ")

        if opcao == "1":
            cadastrar_turma()
        elif opcao == "2":
            listar_turmas()
        elif opcao == "0":
            break
        else:
            print("Opcao invalida.")
