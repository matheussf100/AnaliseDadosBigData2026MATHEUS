"""
Exercicio 1.
Média Escolar para 5 Estudantes
Use um for loop para iterar 5 vezes.
Dentro do loop, realize a leitura das notas e a decisão
(if/elif/else) da média.
Crie uma lista vazia (resultados = []). 
A cada repetição, adicione uma string (ex: "Aluno 1 - Aprovado") a esta lista usando .append().
"""
#Criando a lista vazia
resultados = []
#Definindo o laco
for i in range (1, 6): 
    nota1=int(input("informe a primeira nota: ")) 
    nota2=int(input("informe a segunda nota: "))
    media=(nota1+nota2)/2    
#Definindo a logica
    if media <4:
        resultados.append(f"Aluno {i} - Reprovado (Media:{media})")
    elif media >=4 and media <6:
        resultados.append(f"Aluno {i} - Recuperacao (Media:{media})")
    else:
        resultados.append(f"Aluno {i} - Aprovado (Media:{media})")
    print(resultados[-1])

""""
Exercicio 2.
Cadastro Seletivo de Candidatos
Use um for loop para iterar 5 vezes. Dentro do loop, use um if/else para checar se o
candidato é menor de 18 anos (rejeição). Crie uma lista principal: candidatos_validos = [].
Se o candidato for válido, crie um Dicionário (ex: candidato = {'nome': '...', 'email': '...'}).
Adicione este Dicionário à lista: candidatos_validos.append(candidato).
"""