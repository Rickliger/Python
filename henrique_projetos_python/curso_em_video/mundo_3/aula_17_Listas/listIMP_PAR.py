listaI = list()
listaP = list()
listaG = list()
num = ''
r = ''
while True:
    num = int(input('Digite um numero: '))
    listaG.append(num)
    if num % 2 == 0:
        listaP.append(num)
    else:
        listaI.append(num)
#for i, v in enumerate(listaG):
 #  if v % 2 == 0:
  #     listaP.append(v)
  # elif v % 2 == 1:
  # listaI.append(v)
    r = str(input('Quer continuar ? '))
    if r in 'nN':
        break
    print(f"Lista Geral: {listaG}\n"
          f"Lista de Pares: {listaP}\n"
          f"Lista de Impares {listaI}")