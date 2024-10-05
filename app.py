# app.py
import random
import pandas as pd
import pickle
import streamlit as st
import matplotlib.pyplot as plt

# Carregar o modelo treinado
with open('model/modelo_recomendacao.pkl', 'rb') as file:
    modelo = pickle.load(file)

# Carregar o dataset
df = pd.read_csv('/workspaces/cgeniusIA/dataset_versions/Dataset_Cliente_v1.1.0.csv')

# Título da aplicação
st.title('Elite Sales - Recomendações de Call Center')

# Inputs do usuário
cpf = st.text_input('Digite o CPF do Cliente')

# Função para buscar o cliente pelo CPF
def buscar_cliente_por_cpf(cpf):
    cliente = df[df['CPF'] == cpf]
    return cliente

# Se o CPF for preenchido, buscar o cliente
if cpf:
    cliente_info = buscar_cliente_por_cpf(cpf)
    
    if not cliente_info.empty:
        # Exibindo o nome do cliente
        nome_cliente = cliente_info['Nome'].values[0]
        st.subheader(f'Informações do Cliente: {nome_cliente}')
        
        # Exibindo as informações do cliente
        st.write(f'CPF: {cpf}')
        st.write(f'Gastos Mensais: R${cliente_info["Gastos_Mensais"].values[0]}')
        st.write(f'Renda Mensal: R${cliente_info["Renda_Mensal"].values[0]}')
        st.write(f'Idade: {cliente_info["Idade"].values[0]} anos')
        st.write(f'Segmento: {cliente_info["Segmento"].values[0]}')
        st.write(f'Tipo de Cartão de Crédito: {cliente_info["Tipo_Cartao_Credito"].values[0]}')

        st.subheader('Abordagem Simulada:')

        abordagens = [
            f"Olá, {nome_cliente}! Como você está? Temos uma nova recomendação que pode se encaixar perfeitamente no seu estilo de vida e perfil financeiro.",
            f"Oi, {nome_cliente}! Esperamos que você esteja tendo um ótimo dia. Identificamos uma oportunidade que pode ser interessante, que tal dar uma olhada?",
            f"Bom dia, {nome_cliente}! Com base nas suas preferências e no seu perfil, encontramos um produto que pode agregar valor às suas experiências diárias. Vamos conversar?",
            f"Olá, {nome_cliente}! Notamos que você tem interesses relacionados a {', '.join(cliente_info['Interesses'].values[0])}. Temos algo especial que pode chamar sua atenção!",
            f"Oi, {nome_cliente}! Acreditamos que um produto do seu interesse poderia otimizar ainda mais suas experiências. Que tal descobrir mais sobre ele?",
        ]

        st.write(random.choice(abordagens))

        # Exibindo gráficos
        st.subheader('Análise Gráfica do Cliente')
        
        # Gráfico de Gastos Mensais vs Renda Mensal
        fig, ax = plt.subplots()
        ax.bar(['Gastos Mensais', 'Renda Mensal'], [cliente_info['Gastos_Mensais'].values[0], cliente_info['Renda_Mensal'].values[0]], color=['blue', 'green'])
        ax.set_ylabel('Valores em R$')
        ax.set_title('Gastos Mensais vs Renda Mensal')
        st.pyplot(fig)

        # Gráfico de Interesses
        interesses = cliente_info['Interesses'].values[0]  # Supondo que os interesses sejam uma lista no formato de string
        interesses_lista = eval(interesses)  # Converte a string de interesses em uma lista, se necessário

        # Contar a frequência de cada interesse
        interesse_contagem = {interesse: 1 for interesse in interesses_lista}  # Cada interesse conta como 1

        # Separando os rótulos e valores para o gráfico
        labels = list(interesse_contagem.keys())
        sizes = list(interesse_contagem.values())

        # Criando o gráfico de pizza
        fig2, ax2 = plt.subplots()
        ax2.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        ax2.set_title('Distribuição de Interesses do Cliente')

        # Exibindo o gráfico
        st.pyplot(fig2)

        # Preparando dados para recomendação
        gastos_mensais = cliente_info['Gastos_Mensais'].values[0]
        renda_mensal = cliente_info['Renda_Mensal'].values[0]
        idade = cliente_info['Idade'].values[0]
        segmento = cliente_info['Segmento'].values[0]
        tipo_cartao = cliente_info['Tipo_Cartao_Credito'].values[0]

        # Converter segmento e tipo de cartão para valores numéricos
        segmento_valor = 0 if segmento == 'Standard' else 1
        tipo_cartao_valor = 0 if tipo_cartao == 'Gold' else 1

        # Preparando os dados para a previsão
        input_data = [[gastos_mensais, renda_mensal, idade, segmento_valor, tipo_cartao_valor]]
        produto_recomendado = modelo.predict(input_data)

        # Exibindo o produto recomendado
        st.subheader('Recomendação de Produto:')
        st.write(f'Com base nos dados fornecidos, recomendamos o seguinte produto: **{produto_recomendado[0]}**')

    else:
        st.write('Cliente não encontrado. Verifique o CPF inserido.')

# Mostrando a tabela de dados completa
st.subheader('Dados dos Clientes')
st.dataframe(df)
