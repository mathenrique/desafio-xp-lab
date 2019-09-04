import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#mapeando o caminho (É NECESSARIO INSERIR O CAMINHO DA PASTA PARA RODAR O PROGRAMA)
xlsx = pd.ExcelFile(r"C:\Users\Usuario\Desktop\XPLAB\dados.xlsx")

#transformando as abas em diferentes dataframes
dfO = pd.read_excel(xlsx, 'orcado')
dfRt = pd.read_excel(xlsx, 'realizado')

#transposição do dataframe "realizado"
dfR = dfRt.T

#renomeando as colunas para a key durante o merge
dfR.columns = ['mês', 'realizado']
dfR = dfR.drop('Unnamed: 0')

#fazendo o merge usando a key "mês"
df = pd.merge(dfO, dfR, on='mês')

#diferenca das colunas orcado e realizado
df['diff'] = df['orcado'] - df['realizado']

#exportando dados de saída pra csv (É IMPORTANTE INSERIR O CAMINHO DE ONDE DESEJA SALVAR)
df.to_csv(r'C:\Users\Usuario\Desktop\XPLAB\dados_saida_matheus.csv')



#GRAFICO

#editando legenda do eixo X
x_axis = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
x = np.array([0,1,2,3,4,5,6,7,8,9,10,11])

#ajustando uma melhor proporção para a visualização do grafico
plt.rcParams['figure.figsize'] = (15,9) 

#barras do gráfico
df["orcado"].plot.bar(x_axis, stacked=True, color='#1F77B4', label='Orçado')
df["realizado"].plot.bar(x_axis, stacked=True, color='#FF7F0E', label='Realizado')

#infos do gráfico
plt.ylabel('$')
plt.xlabel('mês')
plt.title('Gráfico Orçamento')
plt.xticks(x, x_axis)   
plt.legend(['Orçado','Realizado'])

#exportando grafico pra png (É IMPORTANTE INSERIR O CAMINHO DE ONDE DESEJA SALVAR)
plt.savefig(r'C:\Users\Usuario\Desktop\XPLAB\figura_matheus.png')