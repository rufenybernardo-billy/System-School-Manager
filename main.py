import database
import auth
from modulos import alunos as mod_alunos
from modulos import turmas as mod_turmas
from modulos import notas as mod_notas

# menu principal do sistema
def menu_principal(usuario):
    while True:
        print("\n=============================")
        print("  SISTEMA DE GESTAO ESCOLAR  ")
        print("=============================")
        print(f"  Utilizador: {usuario['nome']}")
        print("-----------------------------")
        print("1. Alunos")
        print("2. Turmas")
        print("3. Notas")
        print("0. Sair")
        print("-----------------------------")
        opcao = input("Opcao: ")

        if opcao == "1":
            mod_alunos.menu_alunos()
        elif opcao == "2":
            mod_turmas.menu_turmas()
        elif opcao == "3":
            mod_notas.menu_notas()
        elif opcao == "0":
            print("\nAte logo!")
            break
        else:
            print("Opcao invalida.")

# inicio do programa
def iniciar():
    # inicializa os ficheiros de dados
    database.inicializar()

    # cria o admin se nao existir
    auth.criar_admin()

    # tentativas de login
    tentativas = 0
    usuario = None

    while tentativas < 3:
        usuario = auth.login()
        if usuario:
            break
        tentativas += 1
        restantes = 3 - tentativas
        if restantes > 0:
            print(f"Tentativas restantes: {restantes}")

    if usuario is None:
        print("\nAcesso bloqueado. Tenta mais tarde.")
        return

    menu_principal(usuario)

# arranca o programa
iniciar()
