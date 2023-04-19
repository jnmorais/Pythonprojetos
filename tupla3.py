def intercalar(tupla1, tupla2):
    nova_tupla = ()
    for i in range(4):
        nova_tupla += (tupla1[i],)
        nova_tupla += (tupla2[i],)
    return nova_tupla
tupla1 = (1, 2, 3, 4)
tupla2 = ('j', 'e', 'a','n')
nova_tupla = intercalar(tupla1, tupla2)
print(nova_tupla)
