import json

# caminhos dos ficheiros
usuarios = "modulos/usuarios.json"
turmas = "modulos/turmas.json"
notas = "modulos/notas.json"
alunos = "modulos/alunos.json"

# dicionario com todos os caminhos
ficheiros = {
    "usuarios": usuarios,
    "alunos": alunos,
    "turmas": turmas,
    "notas": notas,
}

# cria os ficheiros se nao existirem
def inicializar():
    for nome, caminho in ficheiros.items():
        try:
            open(caminho, "r")
        except FileNotFoundError:
            with open(caminho, "w") as f:
                json.dump([], f)

# le os dados de um ficheiro
def carregar(nome):
    with open(ficheiros[nome], "r") as f:
        return json.load(f)

# salva os dados num ficheiro
def salvar(nome, dados):
    with open(ficheiros[nome], "w") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)
