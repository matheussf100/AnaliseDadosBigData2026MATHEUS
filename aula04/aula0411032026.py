
# carro=False
# combustivel=False

# #Qual a condição para que este carro funcione?
# if not carro and not combustivel: #<< Ambas as condições são verdadeiras => com o not = false. O not inverte o operador lógico.
#     print ("Meu fusquinha está rodando") # Caso as condições forem alcançadas vai exibir esse print.
# elif carro==False or combustivel==False: # 
#     print("Não sobrou nada para o fusquinha")
# else:
#     print("Não sobrou nada para o fusquinha")


# if not carro and not combustivel:
#     print ("Meu fusquinha está rodando")
# elif carro==False or combustivel==False:
#     print("Não sobrou nada para o fusquinha")
# else:
#     print("Não sobrou nada para o fusquinha")

try:
    semana = int(input("informe o dia:"))
    if semana == 1:
        print("Domingo")
    elif semana == 2:
        print("Segunda-feira")
    elif semana == 3:
        print("Terça-feira")
    elif semana == 4:
        print("Quarta-feira")
    elif semana == 5:
        print("Quinta-feira")
    elif semana == 6:
            print("Sexta-feira")
    elif semana == 7:
        print("Sábado")
    else: # O 'else' funciona como o 'default'
        print("Dia inválido")
except ValueError:
    print("input invalido")

#laços de repetição

# intervalo1=range(10)
# print(intervalo1)

# print("***")

# for numero in range(10):
#     print("numero:")
#     print(numero)













#match case:
# try:
#     mes=int(input("informe o mês:"))
#     match mes:
#         case 1:
#             print("Janeiro")
#         case 2:
#             print("Fevereiro")
#         case 3:
#             print("Março")
#         case 4:
#             print("Abril")
#         case 5:
#             print("Maio")
#         case 6:
#             print("Junho")
#         case 7:
#             print("Julho")
#         case 8:
#             print("Agosto")
#         case 9:
#             print("Setembro")
#         case 10:
#             print("Outubro")
#         case 11:
#             print("Novembro")
#         case 12:
#             print("Dezembro")
#         case _: # O underline ( _ ) funciona como o 'default' ou 'else'
#             print("Mês inválido")
# except:
#     print("Erro desconhecido")