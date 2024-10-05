# treinamento_modelo.py
import pandas as pd
import pickle
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder

# Carregando o dataset
df = pd.read_csv('/workspaces/cgeniusIA/dataset_versions/DatasetIA_v1.1.0.csv')

# Transformando dados categóricos em numéricos (ex: Segmento, Tipo_Cartao_Credito)
label_encoder_segmento = LabelEncoder()
df['Segmento'] = label_encoder_segmento.fit_transform(df['Segmento'])

label_encoder_cartao = LabelEncoder()
df['Tipo_Cartao_Credito'] = label_encoder_cartao.fit_transform(df['Tipo_Cartao_Credito'])

# Selecionando as colunas relevantes para o modelo
X = df[['Gastos_Mensais', 'Renda_Mensal', 'Idade', 'Segmento', 'Tipo_Cartao_Credito']]
y = df['Produto_Indicado']

# Treinamento do modelo de recomendação (KNN)
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)

# Salvando o modelo treinado em um arquivo .pkl
with open('model/modelo_recomendacao.pkl', 'wb') as file:
    pickle.dump(knn, file)

print("Modelo treinado e salvo como 'modelo_recomendacao.pkl'")
