from controller import ControllerCadastro, ControllerLogin
while True:
    print("========== MENU ==========")
    decidir = int(input("Digite 1 para Cadastrar\nDigite 2 para Logar\nDigite 3 para Sair: "))
    print(decidir)

    if decidir == 1:
        nome = input("Digite seu nome: ")
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")
        cadastrado = ControllerCadastro.cadastrar(nome=nome, email=email, senha=senha)
        if cadastrado == 1:
            print("Usuario Cadastrado com Sucesso")
            break
        elif cadastrado == 2:
            print("Nome Inválido")
        elif cadastrado == 3:
            print("Email Inválido")
        elif cadastrado == 4:
            print("Senha Inválida")
        elif cadastrado == 5:
            print("Usuario já cadastrado")
        elif cadastrado == 6:
            print("Erro Interno do Sistema")

    elif decidir == 2:
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")
        logar = ControllerLogin.login(email=email, senha=senha)
        if logar:
            print(logar)
            break
        else:
            print("Usuario não está logado")

    elif decidir == 3:
        print("Saindo...")
        break
