contador=0
limite=12

while contador < limite:
    ano=int(input("informe o ano de nascimento:"))
    idade =2026-ano
    if idade < 18:
        print("participação negada")
    else:
        telefone=int(input("Informe um telefone de contato:"))
        email=str(input("Informe o seu email:"))
    contador= contador + 1