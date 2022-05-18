# bibliotecas
import json

import pytest
import requests

# variaveis publicas
url = 'https://petstore.swagger.io/v2/pet'
headers = {'Content-Type': 'application/json'}


# Defininições das funções (defs)

def test_incluir_pet():
    # Configura
    # dados de entrada provem do pet.jason

    # Resultados esperados
    status_code_esperado = 200
    pet_id_esperado = 3771393
    pet_nome_esperado = "Bud"
    pet_nome_categoria_esperado = "cachorro"
    pet_nome_tag_esperado = "vacinado"

    # Executa
    resultado_obtido = requests.post(
        url=url,
        headers=headers,
        data=open('C:\\Users\\lynna\\PycharmProjects\\134inicial\\vendors\\json\\pet1.json')
    )

    # Valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(corpo_do_resultado_obtido)

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido ['id'] == pet_id_esperado
    assert corpo_do_resultado_obtido ['name'] == pet_nome_esperado
    assert corpo_do_resultado_obtido['category']['name'] == pet_nome_categoria_esperado
    assert corpo_do_resultado_obtido['tags'][0]['name'] == pet_nome_tag_esperado

def test_consulta_pet():
    #configura
    #entrada
    pet_id = '3771393'

    #Resultados esperados
    status_code_esperado = 200
    pet_id_esperado = 3771393
    pet_nome_esperado = "Bud"
    pet_nome_categoria_esperado = "cachorro"
    pet_nome_tag_esperado = "vacinado"

    #executa
    resultado_obtido = requests.get(
        url=url + '/' + pet_id,
        headers=headers
    )
    #valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido ['id'] == pet_id_esperado
    assert corpo_do_resultado_obtido ['name'] == pet_nome_esperado
    assert corpo_do_resultado_obtido['category']['name'] == pet_nome_categoria_esperado
    assert corpo_do_resultado_obtido['tags'][0]['name'] == pet_nome_tag_esperado

def test_alterar_pet():
    # configura
    # dados de entrada provem do pet2.jason

    # Resultados esperados
    status_code_esperado = 200
    tipo_esperado = 'unknown'
    mensagem_esperada = '3771393'

    # Executa
    resultado_obtido = requests.put(
        url=url,
        headers=headers,
        data=open('C:\\Users\\lynna\\PycharmProjects\\134inicial\\vendors\\json\\pet2.json')
    )
    # Valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))
"""
    assert resultado_obtido == status_code_esperado
    assert corpo_do_resultado_obtido['code'] == str(status_code_esperado)
    assert corpo_do_resultado_obtido['type'] == tipo_esperado
    assert corpo_do_resultado_obtido['message'] == mensagem_esperada
