from Python.henrique_projetos_python.curso_em_video.mundo_3.modulos.modulos1 import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos R$ {moeda.aumentar(p, 10)}')
print(f'Diminuido 13%, temos R$ {moeda.diminuir(p, 13)}')
