avaliacoes = int(input("Digite o número de avaliações do aluno: "))
alunos = int(input("Digite o número de alunos: "))

alunos = {}

for i in range(alunos):
    nome = input("Digite o nome do aluno {}: ".format(i+1))
    notas = []
    for j in range(avaliacoes):
        nota = float(input("Digite a nota da avaliação {}: ".format(j+1)))
        notas.append(nota)
    media = sum(notas)/avaliacoes
    alunos[nome] = {'notas': notas, 'media': media}

for nome, dados in alunos.items():
    print("Aluno: {}".format(nome))
    print("Média final: {:.2f}".format(dados['media']))

media_turma = sum(dados['media'] for dados in alunos.values()) / alunos
print("Média da turma: {:.2f}".format(media_turma))
