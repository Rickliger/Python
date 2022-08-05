n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) /2
#while media > 10:
 #   print('Digite um valor válido.')
if media < 5:
    print('Atenção! Sua media foi de {:.1f} pontos. Você está reprovado.'.format(media))
elif media >= 5 and media <= 7:
    print('Sua média foi de {:.1f} pontos. Você esta em recuperação.'.format(media))
else:
    print('Parabéns sua media foi de {:.1f} pontos. Voce foi aprovado.'.format(media))
