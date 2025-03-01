# 1.1 Validador de infos passadas

def validador_numero(numero):
    # Conferindo se é um número válido:
    #   1. Ter somente dígitos.
    #   2. Ter EXATAMENTE 11 números, considerando somente números do Brasil.
    return numero.isdigit() and len(str(numero)) == 11 

def validador_email(email):
    # Conferindo se é um email válido:
    #   1. ter o "@" inserido.
    #   2. ter ao menos um dos gTLD OU ccTLD mais comuns que existem.
    common_gtld = [".com", ".org", ".net", ".edu", ".gov", ".mil", ".int"]
    common_cctld = [".br", ".us", ".uk",".ca", ".au", ".de", ".fr", ".jp", ".cn", ".in"]

    confere = False
    # Confere se está na lista 'common_gtld'.
    for gtld in common_gtld:
        if gtld in email:
            confere = True
            break
    if not confere:
        # Confere se está na lista 'common_cctld'.
        for cctld in common_cctld:
            if cctld in email:
                confere = True
                break
    
    return '@' in email and confere

######

# 1. Adicionar contato

def adicionar_contato(agenda_telefonica):
    contato = {}
    print('\n--- Adicionando Contato ---')
    nome = input('Nome: ').title()  

    # Loop para conferir se o número é válido.
    erro1 = True
    while erro1:
        numero = input('Número: ')
        if validador_numero(numero): 
            contato['Número'] = numero 
            erro1 = False
        else:
            print('\n\U000026A0 O número celular deve conter apenas dígitos e ter exatamente 11 caracteres(DDD+Número).')
            print('Exemplo de entrada esperada: 41999999999\n')

    # Loop para conferir se o email é válido.
    erro2 = True
    while erro2:
        email = input('E-mail: ').lower()
        if validador_email(email):
            contato['E-mail'] = email 
            erro2 = False
        else:
            print('\n\U000026A0 E-mail inválido!')
            print('Exemplo de entrada esperada: meuexemplo@gmail.com\n')

    agenda_telefonica[nome] = contato
    print("\n==============================================") 
    print(f'\U00002705 Contato {nome} adicionado com sucesso!')
    print("==============================================\n")



######


# 2. Alterar contato

def alterar_contato(agenda_telefonica):
    print('\n--- Alterar Contato ---')  
    print('Qual contato deseja alterar?')
    contato = input('Contato: ').title()

    if contato not in agenda_telefonica:
        print('\n\U000026A0 Atenção! Contato não encontrado na agenda.')
        return 
    
    # Biblioteca a qual vou modificar.
    contato_atual = agenda_telefonica[contato]


    # Conferindo se a pessoa deseja mudar o nome do contato.
    opcao_nome = input('Você deseja atualizar o nome ?(s/n)\n')
    while (opcao_nome != 's' and opcao_nome != 'n'):
        print('Entrada inválida. Por favor, digite somente "s" ou "n"\n')
        opcao_nome = input('Você deseja atualizar o nome ?(s/n)\n')
    if opcao_nome == 's':
        novo_nome = input('Nome atualizado: ').title()

        
    # Conferindo se a pessoa deseja mudar o número do contato.
    opcao_numero = input('Você deseja atualizar o número ?(s/n)\n')
    while (opcao_numero != 's' and opcao_numero != 'n'):
        print('Entrada inválida. Por favor, digite somente "s" ou "n"\n')
        opcao_numero = input('Você deseja atualizar o número ?(s/n)\n')    
    if opcao_numero == 's':    
        # Loop para conferir se o número é válido.
        erro1 = True
        while erro1:
            numero = input('Número atualizado: ')
            if validador_numero(numero):
                # Se não mudou o nome do contato, deve-se apagar o número antigo.
                if opcao_nome == 'n':
                    contato_atual.pop('Número', None)
                contato_atual['Número:'] = numero
                erro1 = False
            else:
                print('\n\U000026A0 Atenção! O número celular deve conter apenas dígitos.')


    # Conferindo se a pessoa deseja mudar o email do contato.
    opcao_email = input('Você deseja atualizar o email ?(s/n)\n')
    while (opcao_email != 's' and opcao_email != 'n'):
        print('Entrada inválida. Por favor, digite somente "s" ou "n"\n')
        opcao_email = input('Você deseja atualizar o email ?(s/n)\n')
    if opcao_email == 's':
        # Loop para conferir se o email é válido.    
        erro2 = True
        while erro2:
            email = input('E-mail atualizado: ').lower()
            if validador_email(email):
                # Se não mudou o nome do contato, deve-se apagar o email antigo.
                if opcao_nome == 'n':
                    contato_atual.pop('E-mail', None)
                contato_atual['E-mail:'] = email  
                erro2 = False
            else:
                print('\n\U000026A0 Atenção! E-mail inválido!')

    # Se ele modificou o nome, eu crio um novo contato com as informações novas (mesmo que ele tenha mudado apenas o nome).
    if opcao_nome == 's':
        agenda_telefonica.pop(contato) 
        agenda_telefonica[novo_nome] = contato_atual
        print(f'\n\U00002705 Contato {novo_nome} atualizado com sucesso!')
    # Se ele não modificou o nome, eu somente sobreescrevo as informações novas nas antigas.
    else:
        agenda_telefonica[contato] = contato_atual
        print(f'\n\U00002705 Contato {contato} atualizado com sucesso!')



######


# 3. Remover contato

def remover_contato(agenda_telefonica):
    print('\n--- Removendo Contato ---')

    print('Qual contato deseja excluir?')
    contato = input('Contato: ').title()

    if contato not in agenda_telefonica:
        print('\U000026A0 O contato informado não está listado na agenda')
        return
    else:
        decisao = input(f'\nConfirma a exclusão de {contato}?(s/n): ').lower()

        while (decisao != 's' and decisao != 'n'):
            print('Entrada inválida. Por favor, digite somente "s" ou "n"\n')
            decisao = input('Você deseja atualizar o nome ?(s/n)\n')

        if decisao == 's':
            del agenda_telefonica[contato]
            print("\n===================================================================") 
            print(f'\U00002705 Exclusão do contato {contato} realizada com sucesso!')
            print("===================================================================\n")
        else:
            print("\n===================================================================") 
            print('\U0000274C Exclusão cancelada!')
            print("===================================================================\n")

######


# 4. Listar contato

def listar_contato(agenda_telefonica):
    print('\n--- Lista de Contatos ---')

    if len(agenda_telefonica) == 0:
        print('\U0001F622 Agenda vazia!')

    else:
        for numeracao, chave in enumerate(agenda_telefonica.keys(), start=1):
            print(f'\t{numeracao} - {chave}')

        mais_detalhes = input('\n\U0001F50D Deseja ver mais informações sobre um contato? (s/n): ').lower()

        # Validando a entrada
        opcoes_validas = {'s', 'n'}
        while mais_detalhes not in opcoes_validas:
            print('\n\U000026A0 Atenção! O valor inserido não é uma opção válida. Informe uma das opções: (s/n)\n')
            mais_detalhes = input('Deseja ver mais informações sobre um contato? (s/n): ').lower()

        while mais_detalhes == 's':
            contato = input('Informe o contato que deseja visualizar: ').title()

            if contato not in agenda_telefonica:
                print('\n\U000026A0 Atenção! O contato informado não está na sua Agenda. Por favor, informe um contato válido:\n')
            else:
                print(f'\n--- Detalhes do Contato: {contato} ---')
                for chave, valor in agenda_telefonica[contato].items():
                    print(f'\t{chave}: {valor}')
                
            mais_detalhes = input('\n\U0001F503 Deseja ver mais informações sobre outro contato? (s/n): ').lower()

            # Validando a entrada
            while mais_detalhes not in opcoes_validas:
                print('\n\U000026A0 Atenção! O valor inserido não é uma opção válida. Informe uma das opções: (s/n)\n')
                mais_detalhes = input('Deseja ver mais informações sobre um contato? (s/n): ').lower()


######

def cria_lista(agenda_telefonica):
    # Criando um arquivo "Contatos.txt" quando o usuário sair.
    with open('Contatos.txt', 'w') as file1:
        # Adicionando os contatos nessa lista:
        file1.write('\n--- Lista de Contatos ---\n')

        if len(agenda_telefonica) == 0:
            file1.write('\U0001F622 Agenda vazia!')

        else:
            for numeracao, chave in enumerate(agenda_telefonica.keys(), start=1):
                file1.write('\n-----------------------------------------------------------------------\n')
                file1.write(f'\t{numeracao} - {chave}')
                for sub_chave, sub_valor in agenda_telefonica[chave].items():
                    file1.write(f'\t{sub_chave}: {sub_valor}')
                file1.write('\n-----------------------------------------------------------------------\n')
