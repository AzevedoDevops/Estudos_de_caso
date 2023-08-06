from os import system # se comunica com cmd!
from time import sleep # da um tempo na rolagem do menu (faz pausa)
#\n pula uma linha

def menu():
    print('[1].Cadastro de produto\n[2].Atualizar produto\n[3].Visualizar Estoque\n[0].Sair\n')
#chamar função!

def cadastro(nome,preco,quantidade):         #paramentro!
    produto = (nome,preco,quantidade)
    produtos.append(produto)
    print (f"Produto adicionado com sucesso!\nNome:{nome}\nPreco:{preco}\nQuantidade:{quantidade}")
def visualizar():
    for produto in produtos:
        print (f"Nome :{produto[0]}\nPreco:{produto[1]}\nQuantidade:{produto[2]}\n\n") #\n\n pula duas linhas
def atualizar(nome):
    for i, produto in enumerate(produtos):
        if produto[0]==nome:
           nome=produto[0] # Variavel nome recebe o primeiro valor da tupla produto armazenado em produtos!    
           preco= float(input("Digite o preço do produto"))  
           quantidade= int(input("Digite a quantidade do produto"))  
           produtos.pop(i)         
           cadastro(nome,preco,quantidade)

        
produtos =[]    

while True:
    menu()
    opcao= int(input("Qual opção deseja :"))
    if opcao == 1:
        nome= input("digite o nome do produto: ")
        preco= float(input("Digite o preço do produto: "))  
        quantidade= int(input("Digite a quantidade do produto: "))
        cadastro(nome,preco,quantidade)
    elif opcao == 2:
        nome = input("digite o nome do produto: ")
        atualizar(nome)
    elif opcao == 3:
        visualizar()    
    elif opcao == 0:
        print("Saindo do sistema!")
        exit() # fecha o programa 
    else:
        print("Opção invalida, digite um numero correspondente ao Menu\n\n")
