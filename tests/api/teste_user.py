# ToDo: 1 - criar um teste que adicione um usuário
# ToDo: 2 - realizar o login e extrair o token da resposta
# ToDo: 3 - criar uma venda de um pet para un usuário
# ToDo: 4 - consultar os dados do pet que foi vendido
import json

import requests

# variaveis publicas
url = 'https://petstore.swagger.io/v2/user'
headers = {'Content-Type': 'application/json'}


def test_incluir_usuário():
    # Configura
    # Dados de Entrada
    # Dados de entrada provem do user1.json


    # Resultados Esperados
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = 'unknown'
    mensagem_esperada = '13933771'

    # Executa
    resultado_obtido = requests.post(
        url=url,
        headers=headers,
        data=open('C:\\Users\\lynna\\PycharmProjects\\134inicial\\vendors\\json\\user1.jason')
    )

    # Valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['code'] == codigo_esperado
    assert corpo_do_resultado_obtido['type'] == tipo_esperado
    assert corpo_do_resultado_obtido['message'] == mensagem_esperada


def test_incluir():
    # Configura
    # Dados de entrada
    username = 'teste'

    # Resultados Esperados


