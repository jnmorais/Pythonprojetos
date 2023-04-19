def operar(tupla):
    operacao, num1, num2 = tupla
    if operacao == 'SOMA':
        return num1 + num2
    if operacao == 'SUB':
        return num1 - num2
    if operacao == 'MULT':
        return num1 * num2
    if operacao == 'DIV':
        return num1 / num2
    else:
        return None
tupla1 = ('SOMA', 40, 3)
resultado1 = operar(tupla1)
print(resultado1)

tupla2 = ('SUB', 7, 3)
resultado4 = operar(tupla2)
print(resultado4)

tupla3 = ('MULT', 50, 5)
resultado2 = operar(tupla3)
print(resultado2)

tupla4 = ('DIV', 10, 4)
resultado3 = operar(tupla4)
print(resultado3)

tupla5 = ('EXP', 3, 4)
resultado5 = operar(tupla5)
print(resultado5)
