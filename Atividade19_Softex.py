#Desenvolva um código que simule uma eleição com três candidatos.
#- candidato_X => 889
#- candidato_Y => 847
#- candidato_Z => 515
#- branco => 0

#O código deve perguntar se deseja finalizar a votação depois do voto.
# Caso o número do voto não corresponda a nenhum candidato ou seja branco,
# ele deve ser tratado como nulo. Se for inserido um texto ao invés de número,
# o código deve retornar uma mensagem para votar novamente.
#Quando a votação for finalizada, o código deverá mostrar o vencedor,
# aquele com o maior número de votos e, também, a quantidade de votos de cada
# candidato, os brancos e nulos

candidato_x = 0
candidato_y = 0
candidato_z = 0
branco = 0
voto = ()


while (voto != 'fim'):
    print('Vote e escolhe entre os seguintes candidatos: ')
    print(f'cadidato X - 889')
    print(f'cadidato Y - 847')
    print(f'cadidato Z - 515')
    print(f'branco ou nulo - 0')
    voto = int(input('Digite o seu voto: '))
    if (voto == 889):
        candidato_x = candidato_x + 1
    elif (voto == 847):
        candidato_y = candidato_y + 1
    elif (voto == 515):
        candidato_z = candidato_z + 1
    elif (voto == 0):
        branco = branco + 1
    elif (voto != int):
        print(f'Você digitou um valor incorreto, tente novamente!')
    else: (voto == 'fim')
    break
    print(f'Votação encerrada!')

vencedor = candidato_x

if candidato_y > vencedor:
    vencedor = candidato_y
elif candidato_z > vencedor:
    vencedor = candidato_z

print(f'O candidato mais votado foi {vencedor}')
print(f'O candidato X recebeo {candidato_x} votos')
print(f'O candidato Y recebeo {candidato_y} votos')
print(f'O candidato Z recebeo {candidato_z} votos')
print(f'Os votos brancos ou nulos foram {branco} votos')


