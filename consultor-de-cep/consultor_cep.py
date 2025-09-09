import requests

def consultar_cep(cep):
    
    url = f'https://viacep.com.br/ws/{cep}/json/'

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()
       
        if "erro" in dados:
            return None 
        return dados
    
    except requests.exceptions.RequestException as e:
        print(f'Ocorreu um erro na requisição {e}')
        return None
    
print('--- Bem vindo ao Consultor de CEP ---')
cep_usuario = input('Digite o CEP que deseja consultar (apenas número): ')

endereco_encontrado = consultar_cep(cep_usuario)

if endereco_encontrado:
    print('\n--- Endereço Encontrado ---')
    print(f"Logradouro: {endereco_encontrado['logradouro']}")
    print(f"Bairro: {endereco_encontrado['bairro']}")
    print(f"Cidade: {endereco_encontrado['localidade']}")
    print(f"Estado: {endereco_encontrado['uf']}")
    print(f"CEP: {endereco_encontrado['cep']}")

    cep = endereco_encontrado['cep']
    estado = endereco_encontrado['uf']
    cidade = endereco_encontrado['localidade']
    bairro = endereco_encontrado['bairro']
    logradouro = endereco_encontrado['logradouro']

else:
    print(f"Não foi possível encontrar o endereço para o CEP {cep_usuario}. Verifique se ele está correto.")
