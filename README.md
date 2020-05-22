# ### ## # Calculator in Python

## Message:
Folks here is one of my first code in python, creating a calculator with SOLID principals.

This link that I am providing is very explanatory what are the  **SOLID principals**.

## Same of the code:
Here is a small example to whet your appetite:
https://imgur.com/a/LfGYoqy

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


Obs.: The code is in portuguese, if any question, please reach out.

## Tools used:
- Python 3.8
- atom
- google (research)
