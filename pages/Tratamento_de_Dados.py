from matplotlib import pyplot as plt
import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
from sklearn.preprocessing import OneHotEncoder

st.set_page_config(
    page_title='Analisando os Dados',
    layout='wide'
)
st.title('Tratamento de Dados')
st.write('Esta página exibe o tratamento de dados realizado no arquivo tratamento_dados.ipynb.')

st.header('Exibindo os Dados')

dados = pd.read_csv('dataset_versions/DatasetIA_v1.0.0.csv')
st.subheader('Dados Processados')
st.write(dados.head())

dados['Data_Nascimento'] = pd.to_datetime(dados['Data_Nascimento'])
dados['Dependentes'] = dados['Dependentes'].replace({"1\"": 1, "0\"": 0, "2\"": 2, "3\"": 3})

especificacao = dados[['Interesses', 'Gastos_Mensais', 'Salario', 'Tipo_Cartao_Credito', 'Gasto_Mensal_Cartao', 'Viaja_Frequentemente', 'Profissao', 'Renda_Mensal', 'Dependentes', 'Idade', 'Plano']]
st.subheader('Dados Especificados')
st.write(especificacao.head())

st.subheader('Valores Ausentes')
st.write(especificacao.isnull().sum())

st.subheader('Informações do DataSet')
st.write('Dimensões do DataFrame:')
st.write(f'Linhas: {especificacao.shape[0]}, Colunas: {especificacao.shape[1]}')

st.subheader('Estatísticas Descritivas')
st.write(especificacao.describe())

especificacao_valores_categoricos = especificacao[['Interesses', 'Tipo_Cartao_Credito', 'Profissao', 'Plano']]
especificacao_valores_numericos = especificacao[['Gastos_Mensais', 'Salario', 'Gasto_Mensal_Cartao', 'Viaja_Frequentemente', 'Renda_Mensal', 'Dependentes', 'Idade']]
#especificacao_valores_numericos['Tipo_Cartao_Credito'] = especificacao_valores_categoricos['Tipo_Cartao_Credito'].replace({"Gold": 1, "Platinum": 2, "Silver": 3})

st.subheader('Histogramas')
st.write('Distribuição dos dados numéricos:')
for coluna in especificacao_valores_numericos:
    st.write(f'**{coluna}**')
    fig = px.histogram(especificacao, x=coluna, nbins=30, title=f'Distribuição de {coluna}')
    st.plotly_chart(fig, use_container_width=True)

st.subheader('Boxplots')
st.write('Boxplots dos dados numéricos:')
for coluna in especificacao_valores_numericos:
    st.write(f'**{coluna}**')
    fig = px.box(especificacao, y=coluna, points='all', title=f'Box Plot de {coluna}')
    st.plotly_chart(fig, use_container_width=True)

st.subheader('Distribuições das Variáveis Categóricas')
for coluna in especificacao_valores_categoricos:
    st.write(f'**{coluna}**')
    fig = px.histogram(especificacao, x=coluna, title=f'Distribuição de {coluna}')
    st.plotly_chart(fig, use_container_width=True)

especificacao_exploded = especificacao['Interesses'].str.replace(r"[\[\]']", '', regex=True).str.split(', ', expand=True).stack().reset_index(level=1, drop=True).to_frame('Interesse')
st.subheader('Distribuições das Variáveis de Interesses')
valores_unicos = especificacao_exploded['Interesse'].value_counts().reset_index()
valores_unicos.columns = ['Interesse', 'Contagem']
st.write(valores_unicos)

especificacao['Interesses'] = especificacao['Interesses'].str.replace(r"[\[\]']", '', regex=True)
especificacao_exploded = especificacao['Interesses'].str.split(', ', expand=True).stack().reset_index(level=1, drop=True).to_frame('Interesse')

contagem_interesses = especificacao_exploded['Interesse'].value_counts().reset_index()
contagem_interesses.columns = ['Interesse', 'Contagem']

fig = px.bar(contagem_interesses, x='Interesse', y='Contagem', title='Contagem de Interesses')
st.plotly_chart(fig, use_container_width=True)

correlation_matrix = especificacao_valores_numericos.corr().round(2)
fig, ax = plt.subplots(figsize=(10, 10))
sns.heatmap(data=correlation_matrix, annot=True, linewidths=.5, ax=ax)
st.write(fig)

numeric_features = ['Gastos_Mensais', 'Salario', 'Gasto_Mensal_Cartao', 'Viaja_Frequentemente', 'Renda_Mensal', 'Dependentes', 'Idade']
categorical_features = ['Profissao']
encoder = OneHotEncoder(sparse_output=False)
encoded_categorical = encoder.fit_transform(dados[categorical_features])
encoded_categorical_df = pd.DataFrame(encoded_categorical, columns=encoder.get_feature_names_out(categorical_features))
df_encoded = pd.concat([dados[numeric_features], encoded_categorical_df], axis=1)
correlation_matrix = df_encoded.corr().round(2)
fig, ax = plt.subplots(figsize=(30, 30))
sns.heatmap(data=correlation_matrix, annot=True, linewidths=.5, ax=ax)
st.write(fig)

numeric_features = ['Gastos_Mensais', 'Salario', 'Gasto_Mensal_Cartao', 'Viaja_Frequentemente', 'Renda_Mensal', 'Dependentes', 'Idade']
categorical_features = ['Plano']
encoder = OneHotEncoder(sparse_output=False)
encoded_categorical = encoder.fit_transform(dados[categorical_features])
encoded_categorical_df = pd.DataFrame(encoded_categorical, columns=encoder.get_feature_names_out(categorical_features))
df_encoded = pd.concat([dados[numeric_features], encoded_categorical_df], axis=1)
correlation_matrix = df_encoded.corr().round(2)
fig, ax = plt.subplots(figsize=(30, 30))
sns.heatmap(data=correlation_matrix, annot=True, linewidths=.5, ax=ax)
st.write(fig)

colors = {'Plano Conexão': 'red', 'Plano Serenidade': 'blue', 'Plano Equilíbrio': 'green'}
fig, ax = plt.subplots()
ax.scatter(especificacao['Gastos_Mensais'], especificacao['Salario'], c=especificacao['Plano'].map(colors), label=colors)
ax.set_title('Gastos Mensais vs Salário')
ax.set_xlabel('Gastos Mensais')
ax.set_ylabel('Salário')
ax.legend(handles=[plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10) for color in colors.values()], labels=colors.keys())
st.pyplot(fig)

colors = {'Plano Conexão': 'red', 'Plano Serenidade': 'blue', 'Plano Equilíbrio': 'green'}
fig, ax = plt.subplots()
ax.scatter(especificacao['Gasto_Mensal_Cartao'], especificacao['Renda_Mensal'], c=especificacao['Plano'].map(colors), label=colors)
ax.set_title('Gasto Mensal no Cartão vs Renda Mensal')
ax.set_xlabel('Gasto Mensal no Cartão')
ax.set_ylabel('Renda Mensal')
ax.legend(handles=[plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10) for color in colors.values()], labels=colors.keys())
st.pyplot(fig)

fig, ax = plt.subplots()
sns.violinplot(y='Plano', x='Gastos_Mensais', data=especificacao, inner='quartile', ax=ax)
st.pyplot(fig)

fig, ax = plt.subplots()
sns.violinplot(y='Plano', x='Salario', data=especificacao, inner='quartile', ax=ax)
st.pyplot(fig)

fig, ax = plt.subplots()
sns.violinplot(y='Plano', x='Gasto_Mensal_Cartao', data=especificacao, inner='quartile', ax=ax)
st.pyplot(fig)

fig, ax = plt.subplots()
sns.violinplot(y='Plano', x='Renda_Mensal', data=especificacao, inner='quartile', ax=ax)
st.pyplot(fig)

st.subheader('Análise')
st.write("""
#### Correlação entre Profissões e Gastos:
- A profissão Programador tem uma correlação positiva com Gastos Mensais (0.28) e Salário (0.31), indicando que programadores tendem a ter salários e gastos mensais mais altos.
- A profissão Chef tem uma correlação negativa com Gastos Mensais (-0.22) e Salário (-0.18), sugerindo que chefs podem ter salários e gastos mensais mais baixos.
""")

st.write("""
#### Correlação entre Planos e Gastos:
- O plano Plano Conexão tem uma correlação positiva com Gastos Mensais (0.48) e Salário (0.43), indicando que pessoas com este plano tendem a ter salários e gastos mensais mais altos.
- O plano Plano Serenidade tem uma correlação negativa com Gastos Mensais (-0.34) e Salário (-0.33), sugerindo que pessoas com este plano tendem a ter salários e gastos mensais mais baixos.
""")

st.write("""
#### Correlacao Forte entre Gastos Mensais e Salario:
- A correlacao entre Gastos Mensais e Salario e muito alta (0.92), indicando que pessoas com salarios mais altos tendem a ter gastos mensais mais altos.
""")

st.write("""
#### Correlacao entre Gastos Mensais e Gasto Mensal no Cartao:
- A correlacao entre Gastos Mensais e Gasto Mensal Cartao e moderada (0.69), sugerindo que uma parte significativa dos gastos mensais pode ser feita atraves do cartao de credito.
""")

st.write("""
#### Correlacao entre Salario e Renda Mensal:
- A correlacao entre Salario e Renda Mensal e perfeita (1.00), o que faz sentido, pois a renda mensal geralmente inclui o salario.
""")

st.write("""
#### Correlacao entre Viajar Frequentemente e Outras Variaveis:
- Viaja Frequentemente tem correlacoes moderadas com Gastos Mensais (0.44), Salario (0.40), e Gasto Mensal Cartao (0.37). Isso sugere que pessoas que viajam frequentemente tendem a ter maiores gastos mensais, salarios e gastos no cartao.
""")

st.write("""
#### Correlacao entre Planos e Gastos:
- Plano Plano Conexao tem uma correlacao positiva com Gastos Mensais (0.48) e Salario (0.43), indicando que pessoas com este plano tendem a ter salarios e gastos mensais mais altos.
- Plano Plano Serenidade tem uma correlacao negativa com Gastos Mensais (-0.34) e Salario (-0.33), sugerindo que pessoas com este plano tendem a ter salarios e gastos mensais mais baixos.
""")

st.write("""
#### Correlacao entre Dependentes e Outras Variaveis:
- Dependentes tem correlacoes muito baixas com a maioria das outras variaveis, exceto uma correlacao ligeiramente negativa com Viaja Frequentemente (-0.15). Isso pode indicar que pessoas com mais dependentes tendem a viajar menos frequentemente.
""")

st.write("""
#### Correlacao entre Idade e Variáveis Financeiras:
- Idade tem correlacoes moderadas com Gastos Mensais (0.38) e Salario (0.40), sugerindo que pessoas mais velhas tendem a ter maiores salarios e gastos mensais.
""")