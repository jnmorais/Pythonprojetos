def entre_x_y(x, y):
    if x <= y:
        return list(range(x, y+1))
    else:
        return list(range(y, x+1))
lista1 = entre_x_y(10, 7)
print(lista1)

lista2 = entre_x_y(7, 3)
print(lista2)

