# 🏫 Sistema de Gestão Escolar

Sistema de gestão escolar via terminal desenvolvido em Python. Permite gerir alunos, turmas e notas de forma simples e organizada, com sistema de login seguro.

---

## ✨ Funcionalidades

- 🔐 Login com senha encriptada (SHA-256)
- 👨‍🎓 Cadastro, listagem e remoção de alunos
- 📋 Listagem de alunos por classe e turma
- 🔍 Pesquisa de aluno por nome
- 🏫 Gestão de turmas e classes
- 📝 Lançamento de notas por trimestre
- 📊 Cálculo automático de médias
- 💾 Dados guardados em JSON

---

## 🛠️ Tecnologias

- Python 3
- JSON (base de dados local)
- hashlib (encriptação de senhas)

---

## 📁 Estrutura

```
escola/
├── main.py           # ficheiro principal
├── auth.py           # sistema de login
├── database.py       # leitura e escrita de dados
└── modulos/
    ├── alunos.py     # gestão de alunos
    ├── turmas.py     # gestão de turmas
    └── notas.py      # gestão de notas
```

---

## 🚀 Como usar

**1. Clona o repositório**
```bash
git clone https://github.com/rufenybernardo-billy/System-School-Manager
```

**2. Entra na pasta**
```bash
cd sistema-escolar
```

**3. Corre o programa**
```bash
python main.py
```

**4. No primeiro acesso cria o teu admin**
```
-- Primeiro acesso, cria o teu admin --
Nome de utilizador: admin
Senha: ****
Admin criado com sucesso!
```

---

## 📌 Exemplo de uso

```
=============================
  SISTEMA DE GESTAO ESCOLAR  
=============================
  Utilizador: admin
-----------------------------
1. Alunos
2. Turmas
3. Notas
0. Sair
-----------------------------
Opcao: 
```

---

## 👨‍💻 Autor

**Rufeny Bernardo**  
[GitHub](https://github.com/rufenybernardo-billy) · [WhatsApp](https://wa.me/244953613315) · [Email](mailto:rufenybernardo@gmail.com)
