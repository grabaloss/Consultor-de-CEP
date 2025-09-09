import requests

cep = input('Digite o CEP (apenas números): ')
url = f'https://viacep.com.br/ws/{cep}/json/'

resposta = requests.get(url)

if resposta.status_code == 200: 
    dados = resposta.json()
    print('CEP:', dados['cep'])
    print('Logradouro:', dados['logradouro'])
    print('Bairro:', dados['bairro'])
    print('Cidade:', dados['localidade'])
    print('Estado:', dados['uf'])
else: 
    print('CEP não encontrado.')