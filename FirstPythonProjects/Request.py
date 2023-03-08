import requests

def RetornaDados(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    print(response.status_code) #Se voltar 200 é pq deu certo
    print(response.text)

    dados = response.json()
    print("Logradouro: {}".format(dados['logradouro']))

    return dados

if __name__ == '__main__':
    RetornaDados('05345000')

