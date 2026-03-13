# Exercício 2

# 2.1 Escreva um programa para ler as dimensões de uma cozinha retangular (comprimento,
# largura e altura) V
# 2.2 calcular e escrever a quantidade de caixas de azulejos para se colocar em todas as suas paredes (considere que não será descontada a área ocupada por portas e
# janelas). 
# 2.3 Cada caixa de azulejos possui 1,5 m²

#variaveis => dimensões, caixas de azulejos, 

comprimento= float(input("Informe o comprimento: "))
largura= float(input("Informe a largura: "))
altura= float(input("Informe a altura: "))
perimetro= 2 * (comprimento + largura)
area_paredes= perimetro * altura
q_caixas= area_paredes/1.5

if q_caixas >=0 and area_paredes >=0:
    print(f"quantidade de caixas: {q_caixas:.2f}")
else:
    print("Os valores são inválidos")
