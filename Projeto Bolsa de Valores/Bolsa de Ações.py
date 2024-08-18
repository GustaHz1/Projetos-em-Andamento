cnpjs = {}
cpfs = {}

while True:
    login = input("Deseja fazer login como empresa/CNPJ ou pessoa/CPF: ")

    if login == 'CNPJ':
        print("""
        [1]Registar Usuário
        [2]Login
        [3]Sair 
        """)
        opcao_cnpj = input()
        
        if opcao_cnpj == '1':
            cnpj = int(input("Digite seu CNPJ para cadastro: "))
            senha_cnpj = input(f"Crie uma senha para logar no CNPJ: {cnpj} ")
            cnpjs[cnpj] = senha_cnpj
            
        elif opcao_cnpj == '2':
            validar_cnpj = int(input("Digite o CNPJ que deseja fazer login: "))
            if validar_cnpj in cnpjs:
                validar_senha_cnpj = input(f"Digite sua senha para login do CNPJ: {validar_cnpj} ")
                if validar_senha_cnpj == cnpjs[cnpj]:
                    print("Login conlcuido! ")
                    break
                
                else:
                    print("Senha incorreta!")
                
            else:
                print("CNPJ não cadastrado!")
                
                
        elif opcao_cnpj == '3':
            break
        
        else:
            print("Opção invalida!")
        
        
    elif login == "CPF":
        acesso_cpf = input("Primeiro acesso? Sim ou Não: ")
        if acesso_cpf == 'Sim':
            cpf = int(input("Digite seu CPF para cadastro: "))
            senha_cpf = input("Digite uma senha para cadastro: ")
            cpfs[cpf] = senha_cpf

        elif acesso_cpf == 'Não':
            validar_cpf = int(input("Digite seu CPF: "))
            if validar_cpf not in cpfs:
                print("CPF não cadastrado!")
            
            else:
                validar_senha_cpf = input("Digite sua senha: ")
                if validar_senha_cpf == cpfs[cpf]:
                    print("Login concluído")
                    break

                else:
                    print("Senha incorreta! ")
        
        else:
            print("Opção inválida! ")
    
        
