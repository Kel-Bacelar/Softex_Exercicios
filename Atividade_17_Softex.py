

#func +
def adicao(num1, num2):
    return num1 + num2

#func -
def subtracao(num1, num2):
    return num1 - num2

#func *
def multiplicacao(num1, num2):
    return num1 * num2

#func /
def divisao(num1, num2):
    return num1 / num2



def calculadora(num1, num2 ,operacao):
    if (operacao == 1):
       resultado = (adicao(num1,num2))
    elif (operacao == 2):
        resultado=(subtracao(num1,num2))
    elif(operacao == 3):
        resultado= (multiplicacao(num1,num2))
    elif(operacao == 4):
        resultado= (divisao(num1,num2))
    else:
        resultado = 0
    return resultado
import os


while True:
    print("Soma -1, Subtra - 2, Multip - 3, Divi - 4 e 5 - Exit")
    operacao = int(input("Digite o codigo da operação: "))
    if operacao == 5:
        print("Programa finalizado!")
        break
    num1 = float(input("Digite um numero: "))
    num2 = float(input("Digite outro numero: "))
    print("Resultado: ", calculadora(num1, num2, operacao))
    os.system("cls")




