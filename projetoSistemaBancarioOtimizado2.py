def cadastrar_usuario(usuarios):
    nome = input("Digite o nome completo do usuário: ")
    cpf = input("Digite o CPF do usuário (apenas números): ")
    data_nascimento = input("Digite a data de nascimento do usuário: ")
    endereco = input("Digite o endereço no formato 'logradouro - bairro - cidade': ")

    # Verificar se o CPF já está cadastrado
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("CPF já cadastrado. Não é possível cadastrar dois usuários com o mesmo CPF.")
            return usuarios

    usuario = {
        "nome": nome,
        "cpf": cpf,
        "data_nascimento": data_nascimento,
        "endereco": endereco,
        "contas": []  
    }

    # Lista para armazenar as contas do usuário
    usuarios.append(usuario)
    print(f"Usuário {nome} cadastrado com sucesso!")
    return usuarios

def cadastrar_conta(usuarios, numero_conta):
    numero_agencia = "0001"
    usuario_cpf = input("Digite o CPF do usuário proprietário da conta (apenas números): ")

    usuario_encontrado = None
    for usuario in usuarios:
        if usuario["cpf"] == usuario_cpf:
            usuario_encontrado = usuario
            break

    if usuario_encontrado is None:
        print("Usuário não encontrado. Não é possível cadastrar a conta.")
        return numero_conta

    conta = {
        "numero_conta": numero_conta,
        "numero_agencia": numero_agencia,
        "usuario": usuario_encontrado
    }

    usuario_encontrado["contas"].append(conta)
    print(f"Conta número {numero_conta} cadastrada com sucesso!")
    return numero_conta + 1

def deposito(saldo, extrato):
    valor_deposito = float(input("Digite o valor do depósito: "))
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"Depósito de R${valor_deposito:.2f}\n"
        print(f"Depósito de R${valor_deposito:.2f} realizado. Saldo atual: R${saldo:.2f}")
    else:
        print("Valor inválido para depósito. O valor deve ser maior que zero.")
    return saldo, extrato

def saque(saldo, extrato, numero_saques):
    if numero_saques < LIMITE_SAQUES:
        valor_saque = float(input("Digite o valor do saque: "))
        if valor_saque > 0 and valor_saque <= 500 and saldo >= valor_saque:
            saldo -= valor_saque
            numero_saques += 1
            extrato += f"Saque de R${valor_saque:.2f}\n"
            print(f"Saque de R${valor_saque:.2f} realizado. Saldo atual: R${saldo:.2f}")
        elif valor_saque > 500:
            print("Valor inválido para saque. O valor máximo por saque é de R$ 500,00.")
        else:
            print("Saldo insuficiente para realizar o saque.")
    else:
        print("Limite de saques diários atingido.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("Extrato:")
    print(extrato)
    print(f"Saldo atual: R${saldo:.2f}")

# Inicialização da lista de usuários
usuarios = []

# Inicialização do número da próxima conta
numero_proxima_conta = 1

menu = """
[c] Cadastrar Usuário
[a] Cadastrar Conta Bancária
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).strip().lower()

    if opcao == "c":
        usuarios = cadastrar_usuario(usuarios)

    elif opcao == "a":
        numero_proxima_conta = cadastrar_conta(usuarios, numero_proxima_conta)

    elif opcao == "d":
        saldo, extrato = deposito(saldo, extrato)

    elif opcao == "s":
        saldo, extrato, numero_saques = saque(saldo, extrato, numero_saques)

    elif opcao == "e":
        exibir_extrato(saldo, extrato)

    elif opcao == "q":
        print("Saindo do sistema... Obrigado por usar nossos serviços.")
        break

    else:
        print("Operação inválida. Por favor, selecione novamente a operação desejada.")
