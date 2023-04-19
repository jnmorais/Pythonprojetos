def somar(lista1, lista2):
    if len(lista1) != 3 or len(lista2) != 3:
        return
    else:
        resultado = []
        for i in range(3):
            soma = lista1[i] + lista2[i]
            resultado.append(soma)
        return resultado
lista1 = [10, 2, 6]
lista2 = [4, 30, 6]
resultado = somar(lista1, lista2)
print(resultado)
