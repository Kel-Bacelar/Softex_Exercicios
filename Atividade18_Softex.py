#Desenvolva um programa que recebe do usuário nome completo
# e ano de nascimento que seja entre 1922 e 2021.
# A partir dessas informações, o sistema mostrará o nome do usuário e a idade
# que completou, ou completará, no ano atual (2022).
# Caso o usuário não digite um número ou apareça um inválido no campo do ano,
# o sistema informará o erro e continuará perguntando até que um valor
# correto seja preenchido.







try:
    nomeComp = str(input("Digite o seu nome completo: "))
    anoNasc = int(input("Digite o seu ano de nascimento: "))
    idadeAtual = 2021 - anoNasc
except:
    print(f"Houve um erro tente outra vez!")
else:
    print(f'{nomeComp} sua idade atual é {idadeAtual}')

