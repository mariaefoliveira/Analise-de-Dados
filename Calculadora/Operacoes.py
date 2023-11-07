
#Lembre-se de que você já conhece o nível avançado da linguagem de programação Python e com este desafio,
#você irá praticar a criação de pacotes em Python, a organização de módulos e scripts em diretórios,
#além de aprender a tornar o seu código reutilizável e facilmente instalável em outros projetos.

import math
class Operacoes:
    def __init__(self,valor1:float,valor2:float):
        self.valor1 = valor1
        self.valor2 = valor2

def soma(valor1,valor2):
    return valor1+valor2

def subtracao(valor1,valor2):
    return valor1-valor2

def multiplicacao(valor1,valor2):
    return valor1*valor2

def divisao(valor1,valor2):
    return valor1/valor2

def potencia(valor1,valor2):
    return valor1**valor2

def quadrada(valor1):
    return math.sqrt(valor1)

def logaritmo(valor1):
    return math.log(valor1)
