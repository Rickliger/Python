def voto(ano):
    from datetime import date
    anoatual = date.today().year
    idade = anoatual - ano
    if idade < 16:
        return f'Com idade {idade}: Voto NEGADO'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com idade {idade}: Voto OPCIONAL'
    else:
        return f'Com idade {idade}: Voto OBRIGATORIO'

#print(voto(1999))
nasc = int(input('Ano de nascimento: '))
print(voto(nasc))

