import os
import pandas as pd
import plotly.express as px

lista_arquivos = os.listdir(r"C:\Users\usuario\PycharmProjects\gitcodes\Vendas")
tabela_total = pd.DataFrame()

for arquivos in lista_arquivos:
    if 'Vendas' in arquivos:
        tabela = pd.read_csv(fr"C:\Users\usuario\PycharmProjects\gitcodes\Vendas\{arquivos}")
        tabela_total = pd.concat([tabela_total, tabela])  # Corrigido aqui

tabela_produtos = tabela_total.groupby('Produto').sum()
tabela_produtos = tabela_produtos[['Quantidade Vendida']].sort_values(by='Quantidade Vendida', ascending=False)


tabela_total['Faturamento'] = tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario']
tabela_faturamento = tabela_total.groupby('Produto').sum()

tabela_faturamento = tabela_faturamento[['Faturamento']].sort_values(by='Faturamento', ascending=False)
#print(tabela_faturamento)

tabela_lojas = tabela_total.groupby('Loja').sum()
tabela_lojas = tabela_lojas[['Faturamento']]
#print(tabela_lojas)


grafico = px.bar(tabela_lojas.reset_index(), x='Loja', y='Faturamento')
grafico.show()


