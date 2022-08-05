import requests
def baixar_arquivo(url, endereco):
    # FAZ REQUISICAO AO SERVIDOR
    resposta = requests.get(url)
    with open(endereco, 'wb') as novo_arquivo:
        novo_arquivo.write(resposta.content)
if __name__ == "__main__":
    baixar_arquivo('https://asdfiles.com/upgrade?f=48CgP''teste.pdf')
