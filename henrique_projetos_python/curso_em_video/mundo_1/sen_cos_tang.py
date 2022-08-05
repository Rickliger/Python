'''seno → sen α  = cateto oposto a α / hipotenusa
cosseno → cos α  = cateto adjacente a α / hipotenusa
tangente → tan α  =   cateto oposto a α / cateto adjacente a α
sen alfa = c/a, cos alfa = b/a, tang alfa = c/a.
sen beta = b/a, cos beta = c/a, tang alfa = b/c'''
from math import radians, cos, sin, tan
angulo = float(input('Digite o valor de qualquer ângulo: '))
sen = sin(radians(angulo))
print('O angulo de {} tem seno igual a: {:.2f}.'.format(angulo, sen))
cosseno = cos(radians(angulo))
print('O angulo {} ten cosseno igual a: {:.2f}.'.format(angulo, cosseno))
tangene = tan(radians(angulo))
print('O angulo de {} tem tangente igual a: {:.2f}.'.format(angulo, tangene))
