from Calculadora import *

def menu():
    menu = '''
        +--------------+
        | {:.2f} |
        +--------------+
        (+) somar
        (-) subtrair
        (/) dividir
        (*) multiplicar
        (r) resetar
        (d) desfazer
        (s) sair
        ---------------\n'''.format(calculadora.registrador)

    print(menu)
    
calculadora = Calculadora()

dicionario = {
    '+': 'somar',
    '-': 'subtrair',
    '/': 'dividir',
    '*': 'multiplicar',
    'r': 'resetar',
    'd': 'desfazer',
    's': 'sair'
}

operacao = 'entrar'
while operacao != 'sair':
    menu()
    operacao = input('Operação: ')

    if operacao != 'r' and operacao != 'd' and operacao != 's':
        valor = float(input('Valor: '))
        operacao = dicionario[operacao]
        string = 'calculadora.' + operacao + '(' + str(valor) + ')'
        exec(string)
    else:
        operacao = dicionario[operacao]
        string = 'calculadora.' + operacao + '()'
        exec(string)   

print('\nObrigado por utilizar!')
