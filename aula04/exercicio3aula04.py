#Exercicio 3

# 3. Rendimento do Taxista:
# 3.1 Um motorista de táxi deseja calcular o rendimento de seu carro na praça.
# 3.2 Sabendo-se que o preço do combustível é de R$ 6,15
# 3.3 Escreva um programa para ler: a marcação do odômetro (km) no início do dia
# 3.4 A marcação (km) no final do dia
# 3.5 O número de litros de combustível gasto
# 3.6 O valor total (R$) recebido dos passageiros. 
# 3.7 Calcular e escrever: a média do consumo em km/L e o lucro (líquido) do dia.

#Variaveis => combustivel, odometro (inicio, fim), combustivel_gasto, valor_total, media_consumo,lucro_liq, valor recebido

combustivel= 6.15
odometro_inicio = float(input("Informe a marcação do odometro do inicio do dia (em KM):"))
odometro_final = float(input("Informe a marcação do odometro do final do dia (em KM):"))
combustivel_gasto = float(input("Informe a quantidade de litros de combustivel gastos:"))
valor_recebido = float(input("Informe o valor total recebido pelos passageiros (em R$):"))

km_percorridos = odometro_final - odometro_inicio #distancia percorrida
media_consumo = km_percorridos / combustivel_gasto
custo_combustivel = combustivel_gasto * combustivel
lucro_liq = valor_recebido - custo_combustivel

print(lucro_liq)