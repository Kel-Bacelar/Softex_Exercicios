#Desenvolva um programa que deve ler um arquivo csv intitulado
#“notas_alunos.csv”. O arquivo deve ter a seguinte estrutura:
#aluno: Nome do aluno;
#nota_1: Primeira nota;
#nota_2: Segunda nota;
#faltas: Número de faltas;
#O programa lerá esse arquivo e criará duas colunas.
#A primeira coluna será “media”, que terá a média das duas notas do aluno.
#A segunda será “situacao”, com os valores: APROVADO ou REPROVADO.
#O aluno que tiver mais de 5 faltas ou possuir média menor que sete,
#será reprovado. O programa deverá salvar esse novo dataframe com o nome
#“alunos_situacao.csv”.
#Por fim, o programa deverá mostrar na tela:
#- o maior número de faltas;
#- a média geral das notas dos alunos;
#- e a maior média.
#Veja em anexo um exemplo do arquivo “notas_alunos.csv”.


import pandas as pd


df = pd.read_csv("notas_alunos.csv")

df['media'] = (df["nota_1"] + df["nota_2"]) / 2

situacao = ""
df.loc[df['media'] >= 7, 'situacao'] = 'Aprovado'
df.loc[df['media'] < 7, 'situacao'] = 'Reprovado'
df.loc[df['faltas'] >= 5, 'situacao'] = 'Reprovado'
print(df)


maisfaltas: any = df["faltas"].máx()
print(f" \n O maior número de faltas é: {maisfaltas}")
mediageral: any = df["media"].mediana()
print(f"A média geral das notas dos alunos é: {mediageral}")
maiormedia: any = df["media"].máx()
print(f"A maior média é: {maiormedia}")

df.to_csv("situacao_alunos.csv",index=False)