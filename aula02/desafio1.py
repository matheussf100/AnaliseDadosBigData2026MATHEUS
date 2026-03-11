# Recebidos 3 números inteiros, crie um programa que os mostre ordenados em ordem crescente.

num1 = 6 # Você pode alterar os valores de num1, num2 e num3 para testar com diferentes números
num2 = 4 # Você pode alterar os valores de num1, num2 e num3 para testar com diferentes números
num3 = 3 # Você pode alterar os valores de num1, num2 e num3 para testar com diferentes números

if num1 < num2 and num1 < num3:    # Verifica se num1 é o menor número
    if num2 < num3:                # Verifica se num2 é menor que num3
        print(num1, num2, num3)    # Imprime os números em ordem crescente: num1, num2, num3
    else:                          # Se num3 for menor que num2
        print(num1, num3, num2)    # Imprime os números em ordem crescente: num1, num3, num2  
elif num2 < num1 and num2 < num3:  # Verifica se num2 é o menor número
    if num1 < num3:                # Verifica se num1 é menor que num3
        print(num2, num1, num3)    # Imprime os números em ordem crescente: num2, num1, num3
    else:                          # Se num3 for menor que num1
        print(num2, num3, num1)    # Imprime os números em ordem crescente: num2, num3, num1
else:                              # Se num3 for o menor número
    if num1 < num2:                # Verifica se num1 é menor que num2
        print(num3, num1, num2)    # Imprime os números em ordem crescente: num3, num1, num2         
    else:                          # Se num2 for menor que num1
        print(num3, num2, num1)    # Imprime os números em ordem crescente: num3, num2, num1