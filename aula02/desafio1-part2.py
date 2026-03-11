#Eu preciso testar com operadores de comparação para determinar: maior, o do meio e o menor número.

num1=1 # posso alterar os valores de num1, num2 e num3 para testar com diferentes números
num2=2 # posso alterar os valores de num1, num2 e num3 para testar com diferentes números
num3=3 # posso alterar os valores de num1, num2 e num3 para testar com diferentes números

if num1 == (num1 > num2 and num1 > num3):    # Verifica se num1 é o maior número
    if num2 > num3:                # Verifica se num2 é maior que num3
        print(num3, num2, num1)    # Imprime os números em ordem crescente: num3, num2, num1
    else:                          # Se num3 for maior que num2
        print(num2, num3, num1)    # Imprime os números em ordem crescente: num2, num3, num1
elif num2 == (num2 > num1 and num2 > num3):  # Verifica se num2 é o maior número
    if num1 > num3:                # Verifica se num1 é maior que num3
        print(num3, num1, num2)    # Imprime os números em ordem crescente: num3, num1, num2
    else:                          # Se num3 for maior que num1
        print(num1, num3, num2)    # Imprime os números em ordem crescente: num1, num3, num2
elif num3 == (num3 > num1 and num3 > num2):  # Verifica se num3 é o maior número
    if num1 > num2:                # Verifica se num1 é maior que num2
        print(num2, num1, num3)    # Imprime os números em ordem crescente: num2, num1, num3
    else:                          # Se num2 for maior que num1
        print(num1, num2, num3)    # Imprime os números em ordem crescente: num1, num2, num3