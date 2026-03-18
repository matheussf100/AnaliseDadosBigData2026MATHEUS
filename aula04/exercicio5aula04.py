# variaveis => entrada(nota1, nota2, optativa) , calculo (media) , saida (resultado)

nota1= float(input("Digite a nota da primeira prova"))
nota2= float(input("Digite a nota da segunda prova"))
opt= abs(float(input("Digite a nota da optativa:")))

if opt != -1:
    if nota1 < nota2:
        nota1 = opt  
    else:
        nota2 = opt  

media = (nota1 + nota2) / 2

if media >= 6.0:
    resultado = "Aprovado"
elif media < 3.0:
    resultado = "Reprovado"
else:
    resultado = "Recuperação"

print(f"\nMédia final: {media:.1f}")
print(f"Situação: {resultado}")