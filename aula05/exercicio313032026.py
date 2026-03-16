contador=0
limite=3
usuario="admin"
codigo=1234

while contador < limite:
    login=str(input("digite o login:"))
    senha=int(input("digite a senha:"))

    if login==usuario and senha==codigo:
        print("Login realizado com sucesso!")
        break
    else: 
        contador=contador + 1
        chances= limite - contador
        if chances > 0:
            print(f"Usuario ou senha invalidos! chances restantes:{chances}")
else:
        print("limite atingido!")