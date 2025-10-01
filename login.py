import random

print("Bem-vindo Ao nosso Templo Harmônico")

def formatar_telefone(telefone):
    telefone = str(telefone)
    return f"{telefone[:2]} {telefone[2:7]}-{telefone[7:]}"

def formatar_cpf(cpf):
    cpf = str(cpf)
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

def mascarar_dados(dado):
    if len(dado) > 2:
        return dado[:2] + '*' * (len(dado) - 2)
    return dado

def ler_arquivo():
    dados = {}
    try:
        with open('arquivo.txt', 'r') as f:
            linhas = f.readlines()
        for linha in linhas:
            if linha.strip():
                chave, valor = linha.strip().split(': ', 1)
                dados[chave.lower()] = valor
    except FileNotFoundError:
        pass
    return dados

while True:
    esc = input("Possui login?\n(1) Sim\n(2) Não\nDigite aqui: ")

    if esc == "1":
        print("Certo! Vamos prosseguir")

        dados_cadastrados = ler_arquivo()

        if not dados_cadastrados:
            print("Nenhum usuário cadastrado. Por favor, cadastre-se primeiro.")
            continue

        while True:
            print("Email")
            email = input("Digite aqui: ")
            if "@" in email and len(email.split('@')[0]) >= 3 and ("@gmail.com" in email or "@hotmail.com" in email or "@outlook.com" in email or "@yahoo.com" in email or "@icloud.com" in email or "@baidu.com"):
                if dados_cadastrados.get('email') != email:
                    print("Email não cadastrado. Tente novamente.")
                    continue
                else:
                    print("Email válido!")
                    break
            else:
                print("Email inválido, tente novamente.")

        senha = input("Digite sua senha: ")

        if dados_cadastrados.get('senha') != senha:
            print("Senha incorreta. Tente novamente.")
            continue

        while True:
            lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
            random.shuffle(lista)
            listalimite = lista[0:5]
            print("Digite os números a seguir, separados por espaço:")
            print(listalimite)

            try:
                numeroslistas = input("Digite os números acima: ")
                entrada = list(map(int, numeroslistas.strip().split()))
                if entrada == listalimite:
                    print("Login realizado com sucesso!")
                    break
                else:
                    print("Você digitou os números errados, tente novamente.")
            except ValueError:
                print("Por favor, digite apenas números válidos.")
        break

    elif esc == "2":
        print("Certo, vamos fazer o cadastro")

        while True:
            print("Email")
            email = input("Digite aqui: ")
            if "@" in email and len(email.split('@')[0]) >= 3 and ("@gmail.com" in email or "@hotmail.com" in email or "@outlook.com" in email or "@yahoo.com" in email or "@icloud.com" in email or "@baidu.com"):
                print("Email válido!")
                break
            else:
                print("Email inválido, tente novamente.")

        senha = input("Digite sua senha: ")

        while True:
            senhaconfirmar = input("Digite Novamente sua senha: ")
            if senhaconfirmar == senha:
                print("Correto!")
                break
            else:
                print("Errado! As senhas não coincidem. Tente novamente.")
        
        telefone = input("Digite seu número de telefone (apenas números): ")
        telefone_formatado = formatar_telefone(telefone)
        cpf = input("Digite seu CPF (apenas números): ")
        cpf_formatado = formatar_cpf(cpf)
       
        email_mascarado = mascarar_dados(email)
        senha_mascarada = mascarar_dados(senha)
        telefone_mascarado = mascarar_dados(telefone_formatado)
        cpf_mascarado = mascarar_dados(cpf_formatado)

        with open('arquivo.txt', 'w') as f:
            f.write(f"Email: {email}\n")
            f.write(f"Senha: {senha}\n")
            f.write(f"Telefone: {telefone_formatado}\n")
            f.write(f"CPF: {cpf_formatado}\n")

        print(f"Cadastro realizado com sucesso")
        print(email_mascarado)
        print(senha_mascarada)
        print(telefone_mascarado)
        print(cpf_mascarado)
        break

    else:
        print("Que pena! Sem login, não podemos prosseguir.")
