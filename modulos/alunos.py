import database
from modulos import turmas as mod_turmas

# cadastra um novo aluno
def cadastrar_aluno():
    print("\n-- Cadastrar Aluno --")

    mod_turmas.listar_turmas()
    classe = input("\nClasse do aluno: ")
    turma = input("Turma do aluno: ")

    # verifica se a turma existe
    turmas_classe = mod_turmas.turmas_da_classe(classe)
    nomes_turmas = [t["nome"] for t in turmas_classe]

    if turma not in nomes_turmas:
        print("Turma nao encontrada. Cadastra a turma primeiro.")
        return

    nome = input("Nome completo do aluno: ")
    numero = input("Numero do aluno: ")

    lista_alunos = database.carregar("alunos")

    # verifica se o numero ja existe
    for a in lista_alunos:
        if a["numero"] == numero:
            print("Ja existe um aluno com esse numero.")
            return

    novo_aluno = {
        "nome": nome,
        "numero": numero,
        "classe": classe,
        "turma": turma
    }

    lista_alunos.append(novo_aluno)
    database.salvar("alunos", lista_alunos)
    print(f"Aluno {nome} cadastrado com sucesso!")

# lista alunos por classe e turma
def listar_alunos():
    print("\n-- Listar Alunos --")
    classe = input("Classe: ")
    turma = input("Turma: ")

    lista_alunos = database.carregar("alunos")
    filtrados = [a for a in lista_alunos if a["classe"] == classe and a["turma"] == turma]

    if len(filtrados) == 0:
        print(f"Nenhum aluno encontrado na classe {classe} turma {turma}.")
        return

    print(f"\n-- Classe {classe} | Turma {turma} --")
    for i, a in enumerate(filtrados, 1):
        print(f"{i}. {a['nome']} | N°: {a['numero']}")

# pesquisa aluno por nome
def pesquisar_aluno():
    print("\n-- Pesquisar Aluno --")
    termo = input("Nome do aluno: ").lower()

    lista_alunos = database.carregar("alunos")
    encontrados = [a for a in lista_alunos if termo in a["nome"].lower()]

    if len(encontrados) == 0:
        print("Nenhum aluno encontrado.")
        return

    print("\n-- Resultados --")
    for a in encontrados:
        print(f"Nome: {a['nome']} | N°: {a['numero']} | Classe: {a['classe']} | Turma: {a['turma']}")

# remove um aluno pelo numero
def remover_aluno():
    print("\n-- Remover Aluno --")
    numero = input("Numero do aluno: ")

    lista_alunos = database.carregar("alunos")
    nova_lista = [a for a in lista_alunos if a["numero"] != numero]

    if len(nova_lista) == len(lista_alunos):
        print("Aluno nao encontrado.")
        return

    database.salvar("alunos", nova_lista)
    print("Aluno removido com sucesso.")

# menu de alunos
def menu_alunos():
    while True:
        print("\n===== ALUNOS =====")
        print("1. Cadastrar aluno")
        print("2. Listar por classe e turma")
        print("3. Pesquisar aluno")
        print("4. Remover aluno")
        print("0. Voltar")
        opcao = input("Opcao: ")

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            pesquisar_aluno()
        elif opcao == "4":
            remover_aluno()
        elif opcao == "0":
            break
        else:
            print("Opcao invalida.")
