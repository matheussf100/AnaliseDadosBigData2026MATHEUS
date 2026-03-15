# 1. Cálculo de Média Escolar para Vários Alunos
# Use o laço for para repetir a lógica de 
# cálculo de média e status (Aprovado/Reprovado/Recuperação) 
# que você fez na Aula 4, agora para 10 estudantes.

#variaveis=> aluno, média, status, aprovado, reprovado, recuperação

#condições=> 1. O que se repete? notas, media, status V
#  2. Quantas vezes? 10 vezes V
#  3. O que muda? alunos e as notas V
#  4. O que guardar? 0, cada aluno e independente.V
#  5. Quando para? depois do decimo aluno V

# Ponto importante come;ar pela logica (if, elif, else) e 
# Depois encaixar ele dentro do laco de repeticao.

for i in range (1, 11):
    print(f"aluno {i}")

    b1 = float(input("Informe a nota do 1º bimestre:"))
    b2 = float(input("Informe a nota do 2º bimestre:"))
    b3 = float(input("Informe a nota do 3º bimestre:"))
    b4 = float(input("Informe a nota do 3º bimestre:"))

    media=(b1+b2+b3+b4)/4

    if media >=6:
        status="Aprovado"
    elif media >=5:
        status= "Recuperação"
    else:
        status= "Reprovado"
    print(f"media do aluno:{media}, condição:{status}")