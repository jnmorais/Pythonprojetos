n1 = int(input("Digite sua 1° nota: "))
n2 = int(input("Digite sua 2° nota: "))
n3 = int(input("Digite sua 3° nota: "))

if (0 > n1 or n1 > 10) or (0 > n2 or n2 > 10) or (0 > n3 or n3 > 10):
    print("Nota invalida")

def notas(n1 , n2 , n3):
    if (0 < n1 or n1 < 10) or (0 < n2 or n2 < 10) or (0 < n3 or n3 < 10):
        media = ((n1 * 4) + (n2 * 4) + (n3 * 2))/10
        return media
def Valormedia(media):
    if (0 > media or media > 10):
        print("Nota invalida")
    else:
         if (media < 6):
            print("Reprovado")
         else:
            print("Aprovado")

def Maiornota (n1, n2, n3):
    if n1 > n3 and n1 > n2:
        print("A 1° nota é a maior")
    else:
        if n2 > n3 and n2 > n1:
            print("A 2° nota é a maior")
        else:
            print("A 3° nota é a maior")


a = notas(n1, n2, n3)
print(f"A media é {a}")
Valormedia(notas(n1, n2, n3))
Maiornota(n1, n2, n3)



