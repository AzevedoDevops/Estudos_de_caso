from time import sleep
from os import system

def linha(qnt):
    return '\033[33;1m'+'='*qnt+'\n\033[0m'

def adicionar():
    system('cls')
    print(f'\033[36;1m=============CADASTRO DE PRODUTO=============\033[0m')
    nome = input('Nome: ')
    validacao = True
    for produto in produtos:
        if produto[0] == nome:
            print('\033[31;1mVocê não pode adicionar este produto pois ele já existe.\033[0m')
            sleep(3)
            validacao = False
    if validacao:
        valor = float(input('Valor: R$'))
        estoque = int(input('Estoque: '))
        produto = (nome, valor, estoque)
        produtos.append(produto)
        system('cls')
        print(f'\033[32;1mProduto adicionado com sucesso!\033[0m\n\n{linha(30)}\033[37;1mNome: {nome}\nValor: R${valor:.2f}\nEstoque: {estoque} unidades\033[0m\n{linha(30)}')
        sleep(2)

def atualizar():
    system('cls')
    print(f'\033[36;1m=============ATUALIZAR PRODUTO=============\033[0m')
    validacao = True
    nome = input('Nome do produto: ')
    for i, produto in enumerate(produtos):
        if produto[0] == nome:
            valor = float(input('Valor: R$'))
            estoque = int(input('Estoque: '))
            produtos.pop(i)
            produto = (nome, valor, estoque)
            produtos.append(produto)
            system('cls')
            print(f'\033[32;1mProduto atualizado com sucesso!\033[0m\n{linha(30)}\033[37;1mNome: {nome}\nValor: R${valor:.2f}\nEstoque: {estoque} unidades\n\033[0m{linha(30)}')
            validacao = False
            sleep(2)
    if validacao:
        print('\033[31;1mEsse produto não existe.\033[0m')
        sleep(2)

def visualizar():
    system('cls')
    print(f'\033[36;1m=============VISUALIZAR PRODUTO=============\033[0m')
    for produto in produtos:
        print(f'{linha(30)}\033[37;1mNome: {produto[0]}\nValor: R${produto[1]:.2f}\nEstoque: {produto[2]} unidades\033[0m\n{linha(30)}')
    sleep(5)

def menu():
    system('cls')
    print('\033[33;1m============= MENU =============\033[0m\033[37;1m\n[1] Adicionar novo produto\n[2] Atualizar produto\n[3] Visualizar produto\n[4] Sair\033[0m')

def sair():
    system('cls')
    confirmacao = input('Você tem certeza que deseja sair?\n\033[31;1m[S]\033[0m/\033[32;1m[N]\n\033[0m').lower().replace(' ', '')
    if confirmacao == 's':
        print('\033[31;1mEncerrando programa...\033[0m')
        sleep(1.5)
        exit()
    elif confirmacao == 'n':
        print('\033[32;1mCancelando operação...\033[0m')
        sleep(0.5)
    else:
        print('Opção invalida.')

produtos = []
while True:
    try:
        menu()
        escolha = int(input('Escolha uma das opções: '))
        if escolha == 1:
            adicionar()
        elif escolha == 2:
            atualizar()
        elif escolha == 3:
            visualizar()
        elif escolha == 4:
            sair()
        else:
            print('\033[31;1mOpção inexistente! Por favor, escolha uma das opções apresentadas.\033[0m')
            sleep(2)
    except ValueError:
        print('\033[31;1mERRO! Você deve digitar um número.\033[0m')
        sleep(2)