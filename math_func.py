import sys
import numbers
# Calculadora simples em Python
# Criando a função de Msg de bem-vindo para a calculadora


def boasvindas():
    print('''
Sejá bem-vindo a nossa calculadora!!
''')

# criação da class da calculadora
# SOLID PRINCIPLES - SRP - Princípio da Responsabilidade Única — Temos uma classe que é responsavel por apenas aquilo que se propõe a fazer.


class Calculadora:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

# criando função para somar
    def somar(self):
        return self.numero1 + self.numero2

# criando função para subtrair
    def subtrair(self):
        return self.numero1 - self.numero2

# criando função para multiplicar
    def multiplicar(self):
        return self.numero1 * self.numero2

    #criando função para dividir
    def dividir(self):
        return self.numero1 / self.numero2


# criação da class da calculadora Cientifica
# SOLID PRINCIPLES OCP — Open-Closed Principle objeto estar abertos para extensão, mas fechados para modificação, o metado calculadora scientifica herda as funções da classe caculdadora.
class CalculadoraCientifica(Calculadora):

# criando função para Calcular exponencial
    def exponencial(self):
        return self.numero1 ** self.numero2


def IniciaProcesso():

    escolha = '0'
    opcoes = ['+', '-', '*', '/', '**']
    print("+ para somar")
    print("- para subtrair")
    print("* para multiplicar")
    print("/ para dividir")
    print("** para exponencial")
    escolha = (input("Por favor inserir uma das operações:"))

    if escolha in opcoes:
        numero_1 = int(input('Digite o primeiro numero: '))
        numero_2 = int(input('Digite o segundo numero: '))
        objeto = CalculadoraCientifica(numero_1, numero_2)

    # Somar + + + +
    if escolha == '+':
        print("Resultado: ", objeto.somar())
# Subtrair - - - -
    elif escolha == '-':
        print("Resultado: ", objeto.subtrair())
# Multiplicar * * * *
    elif escolha == '*':
        print("Resultado: ", objeto.multiplicar())
# Divisão / / / /
    elif escolha == '/':
        print("Resultado: ", round(objeto.dividir(), 2))
# Divisão / / / /
    elif escolha == '**':
        print("Resultado: ", objeto.exponencial())
# Instruindo o usuario a selecionar uma opção valida
    else:
        print("Selecione uma opção valida")
        IniciaProcesso()

# Função para perguntar o usuario se ele quer usar a calculadora novamente


def novamente():
    calcular_novamente = input('''
Você gostaria de usar a calculadora novamente?
Por favor inserir S para SIM ou N para NÃO.
''')

    # Se o usuario inserir S rodar a função de calculadora ()
    # incluindo str.upper para aceitar 's' ou 'S'
    if calcular_novamente.upper() == 'S':
        IniciaProcesso()
# Chamando Função Novamante
        novamente()
# Se o usuario inserir N, escrever tchau para o usuario e finaliza a aplicação
    # incluindo str.upper para aceitar 'n' ou 'S'
    elif calcular_novamente.upper() == 'N':
        print('Tchau!! Obrigado por usar nossa calculadora :) ')

# Chamando função boas vindas


boasvindas()

# Chamando Função Inicia Processo

IniciaProcesso()

# Chamando Função Novamante
novamente()
