from main import somar, dividir, multiplicar, subtrair


def teste_somar():
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