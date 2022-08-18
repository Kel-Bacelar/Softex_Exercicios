#Crie um tipo abstrato de dado (TAD) para manipular números complexos
# na linguagem Python.
#O método deve:

#- calcular três números complexos;
#- realizar todas as operações básicas;
#- e imprimir as propriedades real e img do números.



class Num_Complx:
    def __init__(self, comple_x, comple_y, comple_z):
        self.comple_x = comple_x
        self.comple_y = comple_y
        self.comple_z = comple_z
        result_complex = 0

    def soma_complex(self, comple_x, comple_y, comple_z ):
        result_complex = (comple_x + comple_y + comple_z)
        return result_complex

    def subtra_complex(self, comple_x, comple_y, comple_z):
        result_complex = ((comple_x - comple_y) - comple_z)
        return  result_complex

    def multipl_complex(self, comple_x, comple_y, comple_z):
        result_complex = ((comple_x * comple_y) * comple_z)
        return result_complex

    def divi_complex(self, comple_x, comple_y, comple_z ):
        result_complex = (((comple_x / comple_y) / comple_z))


comple_x = complex(5,2)
comple_y = complex(3,8)
comple_z = complex(4,6)

print(f'Resultado = {result_complex}')
print(f'Resultado real = {result_complex.real}')
print(f'Resultado imaginario = {result_complex.imag}')