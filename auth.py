import hashlib
import database

# transforma a senha em hash
def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

# compara a senha digitada com a guardada
def verificar_senha(senha_digitada, senha_guardada):
    return hash_senha(senha_digitada) == senha_guardada

# cria o admin padrao se nao existir nenhum usuario
def criar_admin():
    usuarios = database.carregar("usuarios")
    if len(usuarios) == 0:
        print("\n-- Primeiro acesso, cria o teu admin --")
        nome = input("Nome de utilizador: ")
        senha = input("Senha: ")
        novo_admin = {
            "nome": nome,
            "senha": hash_senha(senha),
            "tipo": "admin"
        }
        usuarios.append(novo_admin)
        database.salvar("usuarios", usuarios)
        print("Admin criado com sucesso!\n")

# faz o login e devolve o utilizador se for valido
def login():
    print("\n========= LOGIN =========")
    nome = input("Utilizador: ")
    senha = input("Senha: ")

    usuarios = database.carregar("usuarios")
    for usuario in usuarios:
        if usuario["nome"] == nome and verificar_senha(senha, usuario["senha"]):
            print(f"\nBem-vindo, {nome}!")
            return usuario

    print("\nUtilizador ou senha incorretos.")
    return None
