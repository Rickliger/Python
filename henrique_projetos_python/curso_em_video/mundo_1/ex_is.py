n = input('digite algo: ')
print('O tipo primitivo desse valor é:', type(n))
print('É numerico? ', n.isnumeric())
print('É alfabético? ', n.isalpha())
print('É um digito? ', n.isdigit())
print('É alfa-numerico? ', n.isalnum())
print('É escrito somente com letras minusculas? ', n.islower())
print('É escrito com letras maiusculas? ', n.isupper())
print('É decimal? ', n.isdecimal())
print('É um espaço? ', n.isspace())
print('É capitalizada? ', n.istitle())
