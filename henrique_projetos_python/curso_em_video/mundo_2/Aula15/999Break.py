c = s = 0

while True:
    n = int(input('Digite o numero: '))
    if n == 999:
        break
    c += 1
    s += n
print(f'Voce digitou {c} valores e a soma total é {s}.')
