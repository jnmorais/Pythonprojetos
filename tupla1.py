def verificar(tupla):
    primeiro = tupla[0]
    ultimo = tupla[-1]
    if primeiro == ultimo:
        return True

tupla1 = (1, 2, 3, 4, 5, 1)
resultado1 = verificar(tupla1)
print(resultado1)

