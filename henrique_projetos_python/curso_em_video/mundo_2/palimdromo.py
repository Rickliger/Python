frase = str(input('Escreva uma frase: ')).strip().upper()
#Tira os espaços entre as palavras e coloca todas os caracteres em maiúsulos
palavras = frase.split()
#Separa todas as palavras em vetores
junto = ''.join(palavras)
#Junta todas as palavras em uma única string
inverso = ''
#Sera usada para inverter a frase
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
    #Vai até o último caractere da string e volta invertendo todos os caracteres

if inverso == junto:
    print('{} é um palídromo'.format(frase))
    #Verifica se os valores são iguais ou não
elif inverso != junto:
    print('{} não é um palídromo.'.format(frase))
