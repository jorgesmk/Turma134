import csv

import pytest

from main import somar, dividir, multiplicar, subtrair


def ler_csv(arquivo_csv):
    dados_csv = []
    try:
        with open(arquivo_csv, newline='') as massa:
            campos = csv.reader(massa, delimiter=',')
            next(campos)
            for linha in campos:
                dados_csv.append(linha)
        return dados_csv
    except FileNotFoundError:
        print(f'arquivo não encontrado: {arquivo_csv}')
    except Exception as fail:
        print(f'falha imprevista: {fail}')


def test_somar():
    # 1 - Configura
    numero_a = 10
    numero_b = 3
    resultado_esperado = 13

    # 2 - Executa
    resultado_obtido = somar(numero_a, numero_b)

    # 3 - Valida
    assert resultado_esperado == resultado_obtido


def test_dividir_positivo():
    # 1 - Configura
    # 1.1 - Dados de entrada
    numero_a = 27
    numero_b = 3

    # 1.2 - Resultados esperados
    resultado_esperado = 9

    # 2 - Executa
    resultado_obtido = dividir(numero_a, numero_b)

    # 3 - Valida
    assert resultado_obtido == resultado_esperado


def test_dividir_negativo():
    # 1 - Configura
    # 1.1 - Dados de entrada
    numero_a = 27
    numero_b = 0

    # 1.2 - Resultados esperados
    resultado_esperado = 'Não dividiras por zero'

    # 2 - Executa
    resultado_obtido = dividir(numero_a, numero_b)

    # 3 - Valida
    assert resultado_obtido == resultado_esperado


def test_multiplicar():
    # 1 - Configura
    # 1.1 - Dados de entrada
    numero_a = 3
    numero_b = 3

    # 1.2 - Resultados esperados
    resultado_esperado = 9

    # 2 - Executa
    resultado_obtido = multiplicar(numero_a, numero_b)

    # 3 - Valida
    assert resultado_obtido == resultado_esperado


def test_subtrair():
    # 1 - Configura
    # 1.1 - Dados de entrada
    numero_a = 3
    numero_b = 3

    # 1.2 - Resultados esperados
    resultado_esperado = 0

    # 2 - Executa
    resultado_obtido = subtrair(numero_a, numero_b)

    # 3 - Valida
    assert resultado_obtido == resultado_esperado


@pytest.mark.parametrize('numero_a, numero_b, resultado_esperado', ler_csv(
    'C:\\Users\\lynna\\PycharmProjects\\134inicial\\vendors\\csv\\massa_teste_subtrair_positivo.csv'))
def test_subtrair_leitura_csv(numero_a, numero_b, resultado_esperado):
    # 1 - Configura
    # utilizamos o csv como massa de testes

    # 2 - Executa
    resultado_obtido = subtrair(int(numero_a), int(numero_b))

    # 3 - Valida
    assert resultado_obtido == int(resultado_esperado)


# Lista para uso como massa de teste
lista_de_valores = [
    (8, 7, 15),
    (20, 30, 50),
    (25, 0, 25),
    (-5, 12, 7),
    (6, -3, 3),
    (7, 3, 4)
]


@pytest.mark.parametrize('numero_a, numero_b, resultado_esperado', lista_de_valores)
def teste_somar_leitura_de_lista(numero_a, numero_b, resultado_esperado):
    # 1 - Configura
    # utilizamos a lista como massa de testes

    # 2 - Executa
    resultado_obtido = somar(numero_a, numero_b)

    # 3 - Valida
    assert resultado_obtido == resultado_esperado


@pytest.mark.parametrize('numero_a, numero_b, resultado_esperado', ler_csv('C:\\Users\\lynna\PycharmProjects\\134inicial\\vendors\\csv\\massa_teste_somar_positivo.csv'))
def teste_somar_leitura_de_csv(numero_a, numero_b, resultado_esperado):
    # 1 - Configura
    # utilizamos o csv como massa de testes

    # 2 - Executa
    resultado_obtido = somar(int(numero_a), int(numero_b))

    # 3 - Valida
    assert resultado_obtido == int(resultado_esperado)
