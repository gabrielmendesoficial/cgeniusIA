import pandas as pd
import pickle
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('/workspaces/cgeniusIA/dataset_versions/DatasetIA_v1.2.0.csv')

# Transformando dados categóricos em numéricos
label_encoder_segmento = LabelEncoder()
label_encoder_cartao = LabelEncoder()
df['Segmento'] = label_encoder_segmento.fit_transform(df['Segmento'])
df['Tipo_Cartao_Credito'] = label_encoder_cartao.fit_transform(df['Tipo_Cartao_Credito'])

# Selecionando as colunas relevantes para o modelo
X = df[['ID', 'Nome', 'CPF', 'Cliente_ID', 'Produto', 'Categoria', 
        'Data_Compra', 'Valor_Compra', 'Quantidade_Parcelas', 'Data_Última_Compra', 
        'Segmento', 'Produto_Indicado', 'Status_Indicação', 'Interesses', 
        'Gastos_Mensais', 'Salario', 'Tipo_Cartao_Credito', 'Gasto_Mensal_Cartao', 
        'Viaja_Frequentemente', 'Profissao', 'Renda_Mensal', 'Dependentes', 
        'Gênero', 'Data_Nascimento', 'Idade']]

y = df['Produto_Indicado']
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)

with open('model/modelo_recomendacao.pkl', 'wb') as file:
    pickle.dump(knn, file)

print("Modelo treinado e salvo como 'modelo_recomendacao.pkl'")
