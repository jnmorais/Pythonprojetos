def media(notas):
    if len(notas) != 5:
        return
    else:
        soma = sum(notas)
        media = soma / len(notas)
        return media
notas = [7, 10, 2, 4, 6]
media = media(notas)
print("A média das notas é:", media)
