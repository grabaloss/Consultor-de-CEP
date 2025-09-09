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

if __name__ == '__main__':

    print('--- Bem vindo ao Consultor de CEP ---')
    print('(Digite "sair" a qualquer momento para encerrar)')
    
while True:
    cep_usuario = input('\nDigite o CEP que deseja consultar: ')
    
    if cep_usuario.lower() == 'sair':
        break
    if len(cep_usuario) != 8 or not cep_usuario.isdigit():
        print('Erro: CEP inválido. Por favor, digite apenas 8 números.')
        continue 
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
        try: 
            with open('enderecos_salvos.txt', 'a', encoding='utf-8') as arquivo:
                arquivo.write('----------------------------------------\n')
                arquivo.write(f"CEP Consultado: {cep}\n")
                arquivo.write(f"Logradouro: {logradouro}\n")
                arquivo.write(f"Bairro: {bairro}\n")
                arquivo.write(f"Cidade/UF: {cidade}/{estado}\n")
                arquivo.write("----------------------------------------\n\n")
            print(f'\n Endereço salvo com sucesso no arquivo "enderecos_salvos.txt"')
        except IOError as e: 
            print(f'\n Ocorreu um erro ao tentar salvar o arquivo: {e}')            
    else:
        print(f"Não foi possível encontrar o endereço para o CEP {cep_usuario}. Verifique se ele está correto.")
print('\nObrigado por usar o Consultor de CEP!')
print('\nPrograma encerrado.')
