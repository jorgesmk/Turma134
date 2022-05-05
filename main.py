import pytest



def imprimir_oi(nome):
    print(f'Oi, {nome}')



def somar(numero_a, numero_b):
    return numero_a + numero_b



def dividir(numero_a, numero_b):
    try:
        return numero_a / numero_b
    except ZeroDivisionError:
        return 'Não dividiras por zero'



def multiplicar(numero_a, numero_b):
    return numero_a * numero_b



def subtrair(numero_a, numero_b):
    return numero_a - numero_b



if __name__ == '__main__':
    imprimir_oi('Luciana')



    resultado = somar(7, 6)
    print(f'A soma: {resultado}')



    resultado = dividir(27, 0)
    print(f'A divisão: {resultado}')



    resultado = multiplicar(3, 3)
    print(f'A multiplicação: {resultado}')



    resultado = subtrair(3, 3)
    print(f'A subtração: {resultado}')





