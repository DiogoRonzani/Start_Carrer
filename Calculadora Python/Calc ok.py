
# Online Python - IDE, Editor, Compiler, Interpreter

def sum (a, b):
    return (a + b)
def subt (a, b):
    return (a - b)
def mult (a, b):
    return (a * b)
def divi (a, b):
    return (a / b)
def continua ():
    print ("Deseja fazer outro cálculo?")
    print ("1 - Sim")
    print ("2 - Não")
    s_ou_n = int(input())
    if s_ou_n == 1:
        return start()
    elif s_ou_n == 2:
        return print("Obrigado")
    else:
        print("Escolha uma opção válida")
        return continua ()
def tela():    
    print ("Selecione o número da operação desejada:")
    print ("1 - Soma")
    print ("2 - Subtração")
    print ("3 - Multiplicação")
    print ("4 - Divisão")

    return int(input("Digite uma Opção ( 1/2/3/4): "))
    
def calc(opt):
    if opt == 1:
        n1 = float(input('Digite o Primeiro número: '))
        n2 = float(input('Digite o Segundo Número: '))
        print ("O resultado da Soma é: ", sum (n1, n2))
        continua()
    
    elif opt == 2:
        n1 = float(input('Digite o Primeiro número: '))
        n2 = float(input('Digite o Segundo Número: '))
        print ("O resultado da Subtração é: ", subt(n1, n2))
        continua()
    
    elif opt == 3:
        n1 = float(input('Digite o Primeiro número: '))
        n2 = float(input('Digite o Segundo Número: '))
        print ("O resultado da Multiplicação é: ", mult(n1, n2))
        continua()
    
    elif opt == 4:
        n1 = float(input('Digite o Primeiro número: '))
        n2 = float(input('Digite o Segundo Número: '))
        print ("O resultado da Divisão é: ", divi(n1, n2))
        continua()
    else:
        print ("Escolha uma opção válida")
        print (tela())
def start ():
    x = tela()
    calc(x)
    
start()