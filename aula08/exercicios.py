"""
1. Controle de Pesca
Crie um programa que ajude um pescador a controlar sua produtividade. Toda vez que ele
traz um peso de peixes maior que o estabelecido pelo regulamento (100 quilos), ele deve
pagar uma multa de R$ 4,00 por quilo excedente.
● O programa deve ler o peso de peixes (em quilos) pescado no dia.
● Você deve criar uma função (ex: calcular_multa(peso_total)) que recebe o peso e
retorna o valor da multa (que pode ser 0.0 se estiver dentro do limite).
● Se o valor da multa retornado for maior que zero, mostre a multa.
● Caso contrário, mostre a mensagem "Peso dentro do limite. Nenhuma multa a
pagar."
● Pergunte o peso de várias pescarias feitas ao longo da semana. O loop para quando
o usuário digitar 0. Ao final, mostre o total de multa acumulado no dia.
"""
# def calcular_multa(peso_total):
#     limite_peso = 100
#     valor_multa_por_quilo = 4.00
#     if peso_total > limite_peso:
#         excesso = peso_total - limite_peso
#         multa = excesso * valor_multa_por_quilo
#         return multa
#     else:
#         return 0.0
# peso=int(input('informe o peso dos peixes pescados: '))
# limite_peso=100
# multa=calcular_multa(peso)
# if multa > 0:
#     print(f"Multa a pagar: R$ {multa:.2f}")
# else:
#     print("Peso dentro do limite. Nenhuma multa a pagar.")
# total_multa = 0.0
# while True:
#     peso = int(input('Informe o peso dos peixes pescados ao longo da semana (ou 0 para encerrar): '))
#     if peso == 0:
#         break
#     multa = calcular_multa(peso)
#     total_multa += multa
# print(f"Total de multa acumulado: R$ {total_multa:.2f}")

"""
2. Calculadora de IMC
Crie um programa que leia a altura e o peso de N pessoas (pergunte ao usuário quantas
pessoas são). Para cada pessoa, mostre seu IMC e a classificação.
● Fórmula: IMC = PESO / (ALTURA * ALTURA)
● Obrigatório (Função 1): Crie uma função calcular_imc(peso, altura) que receberá
os valores e retornará o IMC calculado.
● Obrigatório (Função 2): Crie outra função obter_classificacao(imc) que recebe o
valor do IMC (calculado pela função 1) e retorna uma string com a classificação.
○ Valores de Referência:
■ Menor que 18.5: "Abaixo do peso"
■ 18.5 a 24.9: "Peso normal"
■ 25.0 a 29.9: "Sobrepeso"
■ 30.0 ou mais: "Obesidade"
● O programa principal deve pedir N, fazer um loop N vezes, pedir peso e altura,
chamar as duas funções e imprimir o resultado formatado.
"""

# def calcular_imc(peso, altura):
#     imc = peso / (altura * altura)
#     return imc

# def obter_classificacao(imc):
#     if imc < 18.5:
#         return "Abaixo do peso"
#     elif 18.5 <= imc < 25.0:
#         return "Peso normal"
#     elif 25.0 <= imc < 30.0:
#         return "Sobrepeso"
#     else:
#         return "Obesidade"
# n = int(input("Quantas pessoas deseja calcular o IMC? "))
# for i in range(1, n + 1):
#     peso = float(input(f"Informe o peso da pessoa {i} (em kg): "))
#     altura = float(input(f"Informe a altura da pessoa {i} (em metros): "))
#     imc = calcular_imc(peso, altura)
#     classificacao = obter_classificacao(imc)
#     print(f"Pessoa {i}: IMC = {imc:.2f} - Classificação: {classificacao}")

"""
3. Conversor de Temperatura
Crie um programa que permita ao usuário converter temperaturas entre Celsius e
Fahrenheit.
● Função 1: Crie uma função celsius_para_fahrenheit(temp_c) que recebe a
temperatura em Celsius e retorna o valor em Fahrenheit.
○ Fórmula: F = (C * 9/5) + 32
● Função 2: Crie uma função fahrenheit_para_celsius(temp_f) que recebe a
temperatura em Fahrenheit e retorna o valor em Celsius.
○ Fórmula: C = (F - 32) * 5/9
● O programa principal deve perguntar ao usuário qual conversão ele quer fazer (ex:
"1 para C->F" ou "2 para F->C"), pedir o valor, chamar a função correta e mostrar o
resultado.
Desafio: Criar uma única função que faça qualquer uma das conversões,
sempre perguntando ao usuário qual é desejada.
"""
# def celsius_para_fahrenheit(temp_c):
#     temp_f = (temp_c * 9/5) + 32
#     return temp_f

# def fahrenheit_para_celsius(temp_f):
#     temp_c = (temp_f - 32) * 5/9
#     return temp_c
# conversao = input("Digite '1' para converter de Celsius para Fahrenheit ou '2' para converter de Fahrenheit para Celsius: ")
# if conversao == '1':
#     temp_c = float(input("Informe a temperatura em Celsius: "))
#     temp_f = celsius_para_fahrenheit(temp_c)
#     print(f"{temp_c:.2f}°C é igual a {temp_f:.2f}°F")
# elif conversao == '2':
#     temp_f = float(input("Informe a temperatura em Fahrenheit: "))
#     temp_c = fahrenheit_para_celsius(temp_f)
#     print(f"{temp_f:.2f}°F é igual a {temp_c:.2f}°C")
# else:
#     print("Opção inválida.")

"""
1. Verificador de Ano Bissexto
Crie uma função chamada eh_bissexto(ano):
● A função deve receber um ano (inteiro) como parâmetro.
● Ela deve retornar True (Booleano) se o ano for bissexto, e False caso contrário.
● Regras do ano bissexto: É divisível por 4, exceto para anos divisíveis por 100, a
menos que sejam também divisíveis por 400. (Ex: 2000 e 2400 são bissextos; 1900
e 2100 não são).
● No programa principal, peça um ano ao usuário e imprima "O ano X É bissexto" ou
"O ano X NÃO é bissexto", baseado no retorno da função.
"""
# def eh_bissexto(ano):
#     if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
#         return True
#     else:
#         return False
# ano = int(input("Informe um ano para verificar se é bissexto: "))
# if eh_bissexto(ano):
#     print(f"O ano {ano} É bissexto")
# else:
#     print(f"O ano {ano} NÃO é bissexto")

"""
2. Contagem de Caracteres
Crie uma função chamada contar_caractere(texto, caractere_procurado):
● A função deve receber uma string texto e uma string caractere_procurado (de um só
caractere).
● Ela deve retornar o número de vezes que o caractere_procurado aparece no texto.
(Não diferencie maiúsculas de minúsculas!)
● Dica: Use um loop for para percorrer o texto e use .lower() para tratar os caracteres.
● No programa principal, peça ao usuário uma frase e uma letra, e mostre o resultado
da contagem.
"""
# def contar_caractere(texto, caractere_procurado):
#     contador = 0
#     texto = texto.lower()
#     caractere_procurado = caractere_procurado.lower()
#     for char in texto:
#         if char == caractere_procurado:
#             contador += 1
#     return contador
# frase = input("Informe uma frase: ")
# letra = input("Informe um caractere para contar: ")
# resultado = contar_caractere(frase, letra)
# print(f"A letra '{letra}' aparece {resultado} vezes na frase.")

"""
3. Simulador de Dado
Usando o módulo random, crie uma função rolar_dado(lados).
● A função deve receber o número de lados do dado (ex: 6, 10, 20).
● Ela deve retornar um número aleatório entre 1 e o número de lados (use
random.randint(1, lados)).
● No programa principal, crie um "simulador de batalha":
○ Peça ao usuário para "Rolar para o Ataque (d20)". Chame a função
rolar_dado(20).
○ Peça ao usuário para "Rolar para o Dano (d8)". Chame a função
rolar_dado(8).
○ Imprima os resultados de cada rolagem.
"""


from random import randint


def rolar_dado(lados):
    return randint(1, lados)

print("Simulador de Batalha")
ataque = rolar_dado(20)
dano = rolar_dado(8)
print(f"Rolar para o Ataque (d20): {ataque}")
print(f"Rolar para o Dano (d8): {dano}")
