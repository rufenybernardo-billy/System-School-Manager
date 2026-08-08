import database

# lanca nota de um aluno
def lancar_nota():
    print("\n-- Lancar Nota --")
    numero = input("Numero do aluno: ")

    # verifica se o aluno existe
    lista_alunos = database.carregar("alunos")
    aluno = None
    for a in lista_alunos:
        if a["numero"] == numero:
            aluno = a
            break

    if aluno is None:
        print("Aluno nao encontrado.")
        return

    disciplina = input("Disciplina: ")
    trimestre = input("Trimestre (1, 2 ou 3): ")

    try:
        nota = float(input("Nota (0 a 20): "))
    except ValueError:
        print("Nota invalida.")
        return

    if nota < 0 or nota > 20:
        print("Nota deve ser entre 0 e 20.")
        return

    lista_notas = database.carregar("notas")

    # verifica se ja existe nota para esse aluno, disciplina e trimestre
    for n in lista_notas:
        if n["numero"] == numero and n["disciplina"] == disciplina and n["trimestre"] == trimestre:
            n["nota"] = nota
            database.salvar("notas", lista_notas)
            print("Nota actualizada com sucesso!")
            return

    nova_nota = {
        "numero": numero,
        "nome": aluno["nome"],
        "classe": aluno["classe"],
        "turma": aluno["turma"],
        "disciplina": disciplina,
        "trimestre": trimestre,
        "nota": nota
    }

    lista_notas.append(nova_nota)
    database.salvar("notas", lista_notas)
    print(f"Nota de {aluno['nome']} em {disciplina} lancada com sucesso!")

# ver notas de um aluno
def ver_notas():
    print("\n-- Ver Notas --")
    numero = input("Numero do aluno: ")

    lista_notas = database.carregar("notas")
    notas_aluno = [n for n in lista_notas if n["numero"] == numero]

    if len(notas_aluno) == 0:
        print("Nenhuma nota encontrada para este aluno.")
        return

    print(f"\n-- Notas de {notas_aluno[0]['nome']} --")
    for n in notas_aluno:
        status = "Aprovado" if n["nota"] >= 10 else "Reprovado"
        print(f"Disciplina: {n['disciplina']} | Trimestre: {n['trimestre']} | Nota: {n['nota']} | {status}")

# media do aluno por disciplina
def media_aluno():
    print("\n-- Media do Aluno --")
    numero = input("Numero do aluno: ")
    disciplina = input("Disciplina: ")

    lista_notas = database.carregar("notas")
    notas_disciplina = [n for n in lista_notas if n["numero"] == numero and n["disciplina"] == disciplina]

    if len(notas_disciplina) == 0:
        print("Nenhuma nota encontrada.")
        return

    total = sum(n["nota"] for n in notas_disciplina)
    media = total / len(notas_disciplina)
    status = "Aprovado" if media >= 10 else "Reprovado"

    print(f"\nMedia em {disciplina}: {media:.1f} | {status}")

# menu de notas
def menu_notas():
    while True:
        print("\n===== NOTAS =====")
        print("1. Lancar nota")
        print("2. Ver notas do aluno")
        print("3. Ver media do aluno")
        print("0. Voltar")
        opcao = input("Opcao: ")

        if opcao == "1":
            lancar_nota()
        elif opcao == "2":
            ver_notas()
        elif opcao == "3":
            media_aluno()
        elif opcao == "0":
            break
        else:
            print("Opcao invalida.")
