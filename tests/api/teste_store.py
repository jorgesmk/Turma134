# ToDo: 3 - criar uma venda de um pet para un usuário
# ToDo: 4 - consultar os dados do pet que foi vendido
import requests

url = 'https://petstore.swagger.io/v2/store/order'
headers = {'Content-Type': 'application/json-'}

def teste_vender_pet():
    # Configura
    # Dados de entrada
    #Virao do arquivo pedido1.jason

    # Resultados esperados
    status_code_esperado = 200
    pedido_id_esperado = 9481343
    pet_id_esperado = 3771393
    status_pedido = 'placed'

    #Executa
    resultado_obtido = requests.post(
        url=url,
        headers=headers
        data=open('C:\\Users\\lynna\\PycharmProjects\\134inicial\\tests\api\teste_store.py')
    )

    #valida