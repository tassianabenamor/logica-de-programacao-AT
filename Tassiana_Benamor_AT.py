def menu():
    print("\n Bem vindo ao banco da Tassi :) O que deseja fazer? \n [1] - Criar usuario. \n [2] - Atualizar: Sacar e/ou Depositar. \n [3] - Excluir usuario. \n [4] - Relatório gerencial. \n [5] - Sair.")
    opcao_usuario = le_numero_int("Entre com a opção: ")
    if valida_opcao_menu(opcao_usuario):
        return opcao_usuario
    else: 
        print("Dado inválido. Insira número entre 1 a 5.")

def le_numero_int(texto):
    while True:
        try:
            opcao_usuario = int(input(texto))
            break
        except:
            print("Valor inválido.")
    return opcao_usuario

def le_numero_float(texto):
    while True:
        try:
            opcao_usuario = float(input(texto))
            if opcao_usuario > 0:
                break
        except:
            print("Entre com valor válido. O programa aceita somente número reais.")
    return opcao_usuario

def valida_opcao_menu(opcao_usuario):
    if (opcao_usuario == 1) or (opcao_usuario == 2) or (opcao_usuario == 3) or (opcao_usuario == 4) or (opcao_usuario == 5):
        return True
    else:
        return False

def verificar_numero(contas, numero):
    for usuario in contas:
        if usuario[0] == numero:
            return True
    return False

def criar_conta(contas):
    print("Olá, vamos criar sua usuario!")
    nome = input("Conte-me seu nome: ")
    nome_sobrenome = nome.split(" ")
    if (len(nome_sobrenome) >= 2):
        saldo = le_numero_float("Saldo inicial (não utilize vírgula): R$")
        if saldo > 0:
            numero = le_numero_int("Número da usuario: ")
            if verificar_numero(contas, numero) is False:
                print("Usuário cadastrado com sucesso.")
                contas.append([numero, nome, saldo])
            else:
                print("Usuário já existente.")
        else:
            print("Investimento inicial deve ser maior que ZERO.")
    else:
        print("Entre com NOME e SOBRENOME")

def excluir_conta(contas):
    if verifica_banco_de_dados(contas) == True:
        print("Vamos excluir seu usuário.")
        numero_da_conta = le_numero_int("Informe o número da usuario que deseja excluir: ")
        flag_conta = True
        for usuario in contas:
            if numero_da_conta == usuario[0]:
                flag_conta = False
                if usuario[2] == 0:
                    print("Sua conta foi excluída com sucesso.")
                    contas.remove(usuario)
                else:
                    print("Seu saldo deve ser ZERO para excluir a conta.")
        if flag_conta:
            print("Conta não encontrada.")
    return contas

def atualizar_conta(contas):
    if verifica_banco_de_dados(contas) == True:
        numero = le_numero_int("Digite o numero da conta do usuário: ")
        if verificar_numero(contas, numero):
            print("Qual transação você deseja realizar? \n [1] - Sacar \n [2] - Depositar")
            escolha_usuario = le_numero_int("Opção: ")
            if escolha_usuario == 1:
                sacar(contas, numero)
            elif escolha_usuario == 2:
                depositar(contas, numero)
            else:
                print("Entrada inválida. Entre com opção '[1] - Sacar' ou '[2] - Depositar'.")
        else:
            print("Conta não encontrada.")

def sacar(contas, numero):
    print("Okay, vamos sacar.")
    saque_usuario = le_numero_float("Digite o valor que deseja sacar: ")
    for usuario in contas:
        if numero == usuario[0]:
            if saque_usuario > 0:
                usuario[2] = usuario[2] - saque_usuario
                print(f"O seu saldo atual é de {usuario[2]} reais")
            else:
                print("Não pode realizar saque, pois não possui saldo para isso.")

def depositar(contas, numero):
    print("Okay, vamos depositar.")
    deposito_usuario = le_numero_float("Digite o valor que deseja depositar: ")
    for usuario in contas:
        if numero == usuario[0]:
            usuario[2] += deposito_usuario
            print(f"O seu saldo atual é de {usuario[2]} reais.")

def relatorio_gerencial(contas):
    if verifica_banco_de_dados(contas) == True:
        print("Relatórios gerenciais \n [1] - Clientes com saldo negativo \n [2] - Clientes com saldo acima do valor desejado. \n [3] - Relatório de todos os clientes.")
        entrada_usuario = le_numero_int("Entre com opção: ")
        if entrada_usuario == 2:
            valor = le_numero_float("Qual o valor desejado: ")
        for usuario in contas:
            if entrada_usuario == 1:
                if usuario[2] < 0:
                    print(f"{usuario[1]} está com saldo negativo de {usuario[2]} reais.")
            elif entrada_usuario == 2:
                if usuario[2] >= valor:
                    print(f"{usuario[1]} está com saldo acima de {valor}. O saldo do cliente é {usuario[2]}\n")
            elif entrada_usuario == 3:
                print(f"{usuario[1]}, número de conta {usuario[0]}, possui saldo é: {usuario[2]} \n")
            else:
                print("Entre com opção válida: [1], [2] ou [3].")

def salvar_modificacoes(contas): 
    arquivo = open("./contas.txt", "w") #vai abrir o arquivo txt no modo WRITE (escrita)
    for usuario in contas:
        dados_da_conta = str(usuario[0]) + ";" + usuario[1] + ";" + str(usuario[2]) + "\n" #vai adicionar ao txt numero (string), nome (já era string) e saldo (string)
        arquivo.write(dados_da_conta) #comando que vai escrever na variavel arquivo (que abriu o contas.txt) os dados para atualizar a usuario do usuario

def abrir_banco_de_dados():
    contas = []
    arquivo = open("./contas.txt", "r")
    for usuario in arquivo:
        data = usuario.split(";")
        numero = int(data[0])
        nome = data[1]
        saldo = float(data[2])
        contas.append([numero, nome, saldo])
    arquivo.close()
    return contas

def verifica_banco_de_dados(contas):
    if len(contas) > 0:
        return True
    else:
        print("Erro: Não existem contas cadastradas no Banco da Tassi.")
        return False

opcao = 1
todos_usuarios = abrir_banco_de_dados()
while opcao != 5:
    opcao = menu()
    if opcao == 1:
        criar_conta(todos_usuarios)
    elif opcao == 2:
        atualizar_conta(todos_usuarios)
    elif opcao == 3:
        excluir_conta(todos_usuarios)
    elif opcao == 4:
        relatorio_gerencial(todos_usuarios) 
    elif opcao == 5:
        print("Obrigado por usar o banco da Tassi :)")
        salvar_modificacoes(todos_usuarios)