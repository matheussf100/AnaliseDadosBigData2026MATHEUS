# Exercicio 1

# 1. Cálculo de Lâmpadas:
# 1.1 calcular e imprimir o número de lâmpadas necessárias para
# iluminar um determinado cômodo de uma residência. 

# 1.2 Dados de entrada: a potência da lâmpada utilizada (em watts), as dimensões (largura e comprimento, em metros) do
# cômodo. 

# 2.3 Considere que a potência necessária é de 3 watts por metro quadrado e a cada
# 3m² existe um bocal para uma lâmpada.

# Variáveis: potência (watts), largura e comprimento (metros)

potencia= int(input("Informe a potencia:")) # usuário declarando as variáveis necessárias para a execução
largura= int(input("Informe a largura:")) # usuário declarando as variáveis necessárias para a execução
comprimento= int(input("Informe o comprimento:"))  #usuário declarando as variáveis necessárias para a execução
dimensao= largura * comprimento #parte do verificador.

if potencia>=3 and dimensao==9: # verificação de condição => verdadeira
    print("1 lampada ilumina o comodo") # Retorno da condição verdadeira
elif potencia>=3 and dimensao<9: #verificação de condição => falsa.
    print("precisa de mais uma lampada/bocal por comodo") # Retorno da condição falsa
elif potencia<3 and dimensao==9: #verificação de condição => falsa
    print("potencia insuficiente") # Retorno da condição falsa.
else: #Nenhuma das condições atendidas.
    print("Potencia e dimensões insuficientes!") #retorno da exceção