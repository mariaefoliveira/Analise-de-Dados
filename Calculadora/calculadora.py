import Operacoes


def menu():
    print('CALCULADORA:\n')
    print("Selecione a operação desejada:")

    print("1 - Soma")

    print("2 - Subtração")

    print("3 - Multiplicação")

    print("4 - Divisão")

    print("5 - Potenciação")

    print("6 - Raiz Quadrada")

    print('7 - Logaritmo')

    print('0 - Sair')

    return int(input('Opção: '))


opcao = menu()

if (opcao == 6 or opcao == 7):
    valor1 = float(input('Adicione o valor desejado: '))

    if (opcao == 6):  # Raiz quadrada
        print(Operacoes.quadrada(valor1))

    elif (opcao == 7):  # Logaritmo
        print(Operacoes.logaritmo(valor1))
else:
    valor1 = int(input('Adicione o valor1 desejado: '))
    valor2 = int(input('Adicione o valor2 desejado: '))

    if (opcao == 1):  # soma
        print(Operacoes.soma(valor1, valor2))
    elif (opcao == 2):  # subtração
        print(Operacoes.subtracao(valor1, valor2))
    elif (opcao == 3):  # multiplicação
        print(Operacoes.multiplicacao(valor1, valor2))
    elif (opcao == 4):  # divisão
        print(Operacoes.divisao(valor1, valor2))
    elif (opcao == 5):  # potenciação
        print(Operacoes.potencia(valor1, valor2))
