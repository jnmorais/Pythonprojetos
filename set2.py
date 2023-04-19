meu_set = {1, 2, 3, 4, 1}
meu_set_2 = set([1, 2, 8, 9, 10])


uniao = meu_set.union(meu_set_2)
print("União: ", uniao)

intersecao = meu_set.intersection(meu_set_2)
print("Interseção: ", intersecao)

diferenca = meu_set.difference(meu_set_2)
print("Diferença: ", diferenca)

diferenca_simetrica = meu_set.symmetric_difference(meu_set_2)
print("Diferença simétrica: ", diferenca_simetrica)
