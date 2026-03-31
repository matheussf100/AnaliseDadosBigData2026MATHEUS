import pandas as pd

df_transacoes = pd.read_excel('base_invest.xlsx', sheet_name='Transacoes')

df_hitorico = pd.read_excel('base_invest.xlsx', sheet_name='HistoricoPrecos')

df_participante = pd.read_excel('base_invest.xlsx', sheet_name='Participante')

df_transacoes = df_transacoes['preco']

df_hitorico = df_hitorico['preco']

print(f"Valor minimo da tabela transações =>{df_transacoes.min()}")
print(f"Valor máximo da tabela transações =>{df_transacoes.max()}")
print(f"Valor máximo da tabela historico de preços =>{df_hitorico.max()}")



# print(df_hitorico.max())

# print(df_participante.count())
'''
exercicio exemplo

1- Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser 

https://python.org.br/

https://code.visualstudio.com/

https://www.w3schools.com/

https://git-scm.com/install/windows

---

import pandas as pd

df_transacoes = pd.read_excel('C:\\Users\\douglas.portugal\\Downloads\\base_invest.xlsx', sheet_name='Transacoes')
df_ativo = pd.read_excel('C:\\Users\\douglas.portugal\\Downloads\\base_invest.xlsx', sheet_name='Ativo')

# Pergunta 1: Quais são as máximas e mínimas de operação de compra e venda das transações? ---
# variável nova    tabela[filtro]
df_compra = df_transacoes[df_transacoes['operacao'] == 'compra']
#
df_venda = df_transacoes[df_transacoes['operacao'] == 'venda']
print(df_compra)
print(df_venda)


max_compra_preco = df_compra['preco'].max()
min_compra_preco = df_compra['preco'].min()
max_venda_preco = df_venda['preco'].max()
min_venda_preco = df_venda['preco'].min()

print("--- Preços máximos e mínimos das operações ---")
print(f"Preço máximo de compra: {max_compra_preco}")
print(f"Preço mínimo de compra: {min_compra_preco}")
print(f"Preço máximo de venda: {max_venda_preco}")
print(f"Preço mínimo de venda: {min_venda_preco}")
print("\n")
'''