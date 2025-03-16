'''
Precisamos deixar nosso código mais modularizado, para isso vamos criar funções para as operações existentes:
- Sacar
- Depositar
- Visualizar histórico

Além disso para a versão 2 do nosso sistema, precisamos criar duas novas funções: criar usuário (cliente do banco) e criar conta corrente (vincular com usuário)
Devemos cirar funções para todas as operações do sistema.
Para colocar em prática tudo o que aprendendemos até agora, cada função vai ter uma regra de passagem de argumentos.
O retorno e a forma como serão chamadas, pode ser definida da forma que você achar melhor.

A função saque deve receber os argumentos apenas por nome (keyword only).
Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques.
Sugestão de retorno: Saldo e extrato

A função depósito deve reveber os argumentos apenas por posição (positional only). 
Sugestão de argumentos: saldo, valor, extrato.
Sugestão de retorno: saldo e extrato.

A função extrato deve receber os argumentos por posição e nome (positional only e keyword only).
Argumentos posicionais: saldo.
Argumentos nomeados: extrato.

Precisamos criar 2 novas funções: criar usuário e criar conta corrente.
Fique a vontade para adicionar mais funções se quiser.

Criar usuário: O programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, CPF, data de nascimento e endereço.
O endereço é uma string com o formato: logradouro, número, bairro, cidade/sigla do estado.
Deve ser armazenado somete os números do CPF.
Não podemos cadastrar 2 usuários com o mesmo CPF.

Criar conta corrente: O programa deve armazenar contas em uma lista.
Uma conta é composta por: agência, número da conta e usuário. O número da conta é sequencial, iniciando em 1.
O número da agência é fixo: 0001.
O usuário pode ter mais de uma conta, mas uma conta pertence somente a um único usuário.

Dica: para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do CPF informado para cada usuário da lista.

'''

import textwrap

# Function do Menu, para armazenar as opções de serviços bancários para o usuário
def menu():
    menu = '''\n
    ========== MENU ==========
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [nu]\tNovo usuário
    [lc]\tListar contas
    [q]\tSair
    '''
    return input(textwrap.dedent(menu))

# Function depositar
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito: \tR$ {valor:.2f}\n'
        print('\n=== Depósito realizado com sucesso! ===')
    else:
        print('\n@@@ Operaçao falhou! O valor informado é inválido. @@@')

    return saldo, extrato

#Function sacar
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    execedeu_saldo = valor > saldo
    execedeu_limite = valor > limite
    execedeu_saques = numero_saques >= limite_saques

    if execedeu_saldo:
        print('\n@@@ Operação falhou! Você não tem saldo suficiente. @@@')

    elif execedeu_limite:
        print('\n@@@ Operação falhou! O valor do saque exede o limite. @@@')

    elif execedeu_saques:
        print('\n @@@ Operação falhou! Número máximo de saques excedido. @@@')

    elif valor > 0:
        saldo -= valor
        extrato += f'Saque: \t\tR$ {valor:.2f}\n'
        numero_saques += 1
        print('\n=== Saque realizado com sucesso! ===')

    else:
        print('\n@@@ Operação falhou! O valor informado é inválido. @@@')

    return saldo, extrato

#Function exibir extrato
def exibir_extrato(saldo, /, *, extrato):
    print('\n========== EXTRATO ==========')
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'\nSaldo:\t\tR$ {saldo:.2f}')
    print('===============================')

#Function criar novo usuário
def criar_usuario(usuarios):
    cpf = input('Informe seu CPF (somente números): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\n@@@ Já existe um usuário com esse CPF! @@@')
        return
    
    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe o endereço (logradouro, número - bairro, cidade / sigla do estado): ')

    usuarios.append({'Nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})

    print('===== Usuário criado com sucesso! =====')

# Function filtrar usuário
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

# Function criar nova conta
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do usuário: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\n=== Conta criada com sucesso! ===')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
    
    print('\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@')

# Function para listar as contas existentes do usuário
def listar_contas(contas):
    for conta in contas:
        linha = f'''\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['Nome']}
        '''
        print('=' * 100)
        print(textwrap.dedent(linha))
    
# Function principal, contendo toda a parte lógica do funcionamento do sistema bancário
def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 'd':
            valor = float(input('Informe o valor do depósito: '))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 's':
            valor = float(input('Informe o valor do saque: '))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == 'e':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao ==  'nu':
            criar_usuario(usuarios)

        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == 'lc':
            listar_contas(contas)

        elif opcao == 'q':
            break

        else:
            print('Operação inválida! Por favor, selecione novamente a opção desejada.')

# Colocando o programa para rodar no terminal
main()