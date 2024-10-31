import streamlit as st
import pandas as pd
from sklearn.metrics import (classification_report)
from sklearn.model_selection import cross_val_score, train_test_split, cross_val_predict
from sklearn.metrics import accuracy_score, classification_report
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import ExtraTreesClassifier, RandomForestClassifier
import matplotlib.pyplot as plt

st.set_page_config(
    page_title='Treinamento do Modelo',
    layout='wide'
)
st.title('Treinamento do Modelo')
st.write('Esta página exibe o treinamento dos modelos usando os dados tratados.')

dados = pd.read_csv('dataset_versions/DatasetIA_Filtrado_v1.0.1.csv')
st.subheader('Dados Processados')
st.write(dados.head())
especificacao_valores_categoricos = dados[['Interesses', 'Tipo_Cartao_Credito', 'Profissao', 'Plano']]
especificacao_valores_numericos = dados[['Gastos_Mensais', 'Salario', 'Gasto_Mensal_Cartao', 'Viaja_Frequentemente', 'Renda_Mensal', 'Dependentes', 'Idade']]

especificacao_valores_numericos['Tipo_Cartao_Credito'] = especificacao_valores_categoricos['Tipo_Cartao_Credito'].replace({"Gold": 1, "Platinum": 2, "Silver": 3})
especificacao_valores_numericos['Plano'] = especificacao_valores_categoricos['Plano'].replace({"Plano Conexão": 1, "Plano Serenidade": 2, "Plano Equilíbrio": 3})
entradas = especificacao_valores_numericos
classes = especificacao_valores_numericos['Plano']
entradas_treino, entradas_teste, classes_treino, classes_teste = train_test_split(entradas, classes, test_size=0.2, random_state=42)

@st.cache_data
def treinar_modelo(entradas_treino, classes_treino):
    modelo_et = ExtraTreesClassifier(bootstrap=False, ccp_alpha=0.0,
                      criterion='gini', max_features='sqrt',
                      min_impurity_decrease=0.0, min_samples_leaf=1,
                      min_samples_split=2, min_weight_fraction_leaf=0.0,
                      n_estimators=100, n_jobs=-1,
                      oob_score=False, random_state=123, verbose=0,
                      warm_start=False)
    modelo_et.fit(entradas_treino, classes_treino)
    return modelo_et

@st.cache_data
def treinar_modelo_rf(entradas_treino, classes_treino):
    modelo_rf = RandomForestClassifier(n_estimators=100, random_state=42)
    modelo_rf.fit(entradas_treino, classes_treino)
    return modelo_rf

@st.cache_data
def treinar_modelo_dt(entradas_treino, classes_treino):
    modelo_dt = DecisionTreeClassifier(random_state=42)
    modelo_dt.fit(entradas_treino, classes_treino)
    return modelo_dt

def avaliar_modelo(modelo, entradas_teste, classes_teste):
    classes_encontradas = modelo.predict(entradas_teste)
    acuracia = accuracy_score(classes_teste, classes_encontradas)
    relatorio_classificacao = classification_report(classes_teste, classes_encontradas, output_dict=True)
    return acuracia, relatorio_classificacao

# Treinamento e avaliação do modelo Extra Trees
modelo_et = treinar_modelo(entradas_treino, classes_treino)
acuracia_et, relatorio_et = avaliar_modelo(modelo_et, entradas_teste, classes_teste)

st.subheader('Resultados do Modelo Extra Trees')
st.write(f'Acurácia: {acuracia_et}')
st.dataframe(pd.DataFrame(relatorio_et).transpose())

cv_scores_et = cross_val_score(modelo_et, entradas, classes, cv=5)
st.subheader('Validação Cruzada (Cross-validation) - Extra Trees')
st.write(f'Acurácias nas dobras: {cv_scores_et}')
st.write(f'Acurácia média: {cv_scores_et.mean()}')

# Treinamento e avaliação do modelo Random Forest
modelo_rf = treinar_modelo_rf(entradas_treino, classes_treino)
acuracia_rf, relatorio_rf = avaliar_modelo(modelo_rf, entradas_teste, classes_teste)

st.subheader('Resultados do Modelo Random Forest')
st.write(f'Acurácia: {acuracia_rf}')
st.dataframe(pd.DataFrame(relatorio_rf).transpose())

cv_scores_rf = cross_val_score(modelo_rf, entradas, classes, cv=5)
st.subheader('Validação Cruzada (Cross-validation) - Random Forest')
st.write(f'Acurácias nas dobras: {cv_scores_rf}')
st.write(f'Acurácia média: {cv_scores_rf.mean()}')

# Treinamento e avaliação do modelo Decision Tree
modelo_dt = treinar_modelo_dt(entradas_treino, classes_treino)
acuracia_dt, relatorio_dt = avaliar_modelo(modelo_dt, entradas_teste, classes_teste)

st.subheader('Resultados do Modelo Decision Tree')
st.write(f'Acurácia: {acuracia_dt}')
st.dataframe(pd.DataFrame(relatorio_dt).transpose())

cv_scores_dt = cross_val_score(modelo_dt, entradas, classes, cv=5)
st.subheader('Validação Cruzada (Cross-validation) - Decision Tree')
st.write(f'Acurácias nas dobras: {cv_scores_dt}')
st.write(f'Acurácia média: {cv_scores_dt.mean()}')
