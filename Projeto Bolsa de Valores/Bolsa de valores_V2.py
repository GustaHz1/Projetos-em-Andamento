
cnpjs = {}
cpfs = {}
acoes = {}

while True:
    print('''
          ===BEM VINDO===
          [1]Login CNPJ
          [2]Login CPF
          [3]Sair
          ''')
    login = input()

    if login == '1':
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
            continue
            
        elif opcao_cnpj == '2':
            validar_cnpj = int(input("Digite o CNPJ que deseja fazer login: "))
            if validar_cnpj in cnpjs:
                validar_senha_cnpj = input(f"Digite sua senha para login do CNPJ: {validar_cnpj} ")
                if validar_senha_cnpj == cnpjs[cnpj]:
                    print("Login conlcuido! \n")
                    print('''
                          [1]Cadastrar empresa
                          [2]Comprar ações
                          [3]Vender ações
                          [4]Sair
                          ''')
                    acao_cnpj = input()
                    if acao_cnpj == '1':
                        nome_empresa_grande = input("Digite o nome da sua empresa: ")
                        cnpj_empresa_grande = input("Digite o CNPJ da empresa: ")
                        quantidade_empresa_grande = input("Quantidade de ações para vender:  ")
                        acoes[cnpj_empresa_grande] = quantidade_empresa_grande

                
                else:
                    print("Senha incorreta!")
                
            else:
                print("CNPJ não cadastrado!")
                
                
        elif opcao_cnpj == '3':
            break
        
        else:
            print("Opção invalida!")
        
        
    elif login == "2":
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
        
    elif login == '3':
        break
        
    else:
        print("Opção inválida! ")
    
        
