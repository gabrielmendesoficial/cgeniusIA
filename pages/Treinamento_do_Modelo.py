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

dados = pd.read_csv('dataset_versions\DatasetIA_Filtrado_v1.0.1.csv')
st.subheader('Dados Processados')
st.write(dados.head())
# especificacao = dados[['Interesses', 'Gastos_Mensais', 'Salario', 'Tipo_Cartao_Credito', 'Gasto_Mensal_Cartao', 'Viaja_Frequentemente', 'Profissao', 'Renda_Mensal', 'Dependentes', 'Idade', 'Plano']]
# especificacao.loc[:, 'Viaja_Frequentemente'] = especificacao['Viaja_Frequentemente'].replace({"Sim": 1, "Não": 0})
# especificacao.loc[:, 'Dependentes'] = especificacao['Dependentes'].replace({"1\"": 1, "0\"": 0, "2\"": 2, "3\"": 3})
#dados['Viaja_Frequentemente'] = dados['Viaja_Frequentemente'].replace({"Sim": 1, "Não": 0})
especificacao = dados[['Gastos_Mensais','Interesses', 'Tipo_Cartao_Credito', 'Profissao', 'Plano', 'Salario', 'Gasto_Mensal_Cartao', 'Viaja_Frequentemente', 'Renda_Mensal', 'Dependentes', 'Idade']]

especificacao_valores_categoricos = especificacao[['Interesses', 'Tipo_Cartao_Credito', 'Profissao', 'Plano']]
especificacao_valores_numericos = especificacao[['Gastos_Mensais', 'Salario', 'Gasto_Mensal_Cartao', 'Viaja_Frequentemente', 'Renda_Mensal', 'Dependentes', 'Idade']]

especificacao_valores_numericos['Tipo_Cartao_Credito'] = especificacao_valores_categoricos['Tipo_Cartao_Credito'].replace({"Gold": 1, "Platinum": 2, "Silver": 3})
especificacao_valores_numericos['Plano'] = especificacao_valores_categoricos['Plano'].replace({"Plano Conexão": 1, "Plano Serenidade": 2, "Plano Equilíbrio": 3})
entradas = especificacao_valores_numericos
classes = especificacao_valores_numericos['Plano']
entradas_treino, entradas_teste, classes_treino, classes_teste = train_test_split(entradas, classes, test_size=0.2, random_state=42)

modelo_et = ExtraTreesClassifier(bootstrap=False, ccp_alpha=0.0, class_weight=None,
                      criterion='gini', max_depth=None, max_features='sqrt',
                      max_leaf_nodes=None, max_samples=None,
                      min_impurity_decrease=0.0, min_samples_leaf=1,
                      min_samples_split=2, min_weight_fraction_leaf=0.0,
                      monotonic_cst=None, n_estimators=100, n_jobs=-1,
                      oob_score=False, random_state=123, verbose=0,
                      warm_start=False)

modelo_et.fit(entradas_treino, classes_treino)
classes_encontradas_et = modelo_et.predict(entradas_teste)
acuracia_et = accuracy_score(classes_teste, classes_encontradas_et)

cv_scores_et = cross_val_score(modelo_et, entradas, classes, cv=5)
st.subheader('Validação Cruzada (Cross-validation) - Extra Trees')
st.write(f'Acurácias nas dobras: {cv_scores_et}')
st.write(f'Acurácia média: {cv_scores_et.mean()}')

st.subheader('Resultados do Modelo Extra Trees')
st.write(f'Acurácia: {acuracia_et}')
st.dataframe(pd.DataFrame(classification_report(classes_teste, classes_encontradas_et, output_dict=True)).transpose())


modelo_rf = RandomForestClassifier(bootstrap=True, ccp_alpha=0.0, class_weight=None,
                       criterion='gini', max_depth=None, max_features='sqrt',
                       max_leaf_nodes=None, max_samples=None,
                       min_impurity_decrease=0.0, min_samples_leaf=1,
                       min_samples_split=2, min_weight_fraction_leaf=0.0,
                       monotonic_cst=None, n_estimators=100, n_jobs=-1,
                       oob_score=False, random_state=123, verbose=0,
                       warm_start=False)

modelo_rf.fit(entradas_treino, classes_treino)
classes_encontradas_rf = modelo_rf.predict(entradas_teste)
acuracia_rf = accuracy_score(classes_teste, classes_encontradas_rf)

cv_scores_rf = cross_val_score(modelo_rf, entradas, classes, cv=5)
st.subheader('Validação Cruzada (Cross-validation) - Random Forest')
st.write(f'Acurácias nas dobras: {cv_scores_rf}')
st.write(f'Acurácia média: {cv_scores_rf.mean()}')

st.subheader('Resultados do Modelo Random Forest')
st.write(f'Acurácia: {acuracia_rf}')
st.dataframe(pd.DataFrame(classification_report(classes_teste, classes_encontradas_rf, output_dict=True)).transpose())




