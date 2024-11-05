# Projeto de Assistente IA para Call Centers

## Vídeo pitch
https://youtu.be/nWgQ4H9zJhA

## Foco do Projeto
O objetivo deste projeto é desenvolver uma inteligência artificial (IA) que auxilia operadores de call center na geração de textos a partir de informações dos clientes. Isso permite que os operadores ofereçam um atendimento mais eficiente e personalizado.

## Problema a Resolver
Os operadores de call center frequentemente enfrentam desafios relacionados ao tempo de resposta e à personalização do atendimento. A falta de informações consolidadas sobre os clientes pode levar a interações menos satisfatórias e à perda de oportunidades de venda. A nossa solução visa otimizar esse processo.

## Solução
A IA utiliza um banco de dados contendo informações dos clientes, permitindo a geração automática de textos que ajudam os operadores a se comunicarem de forma mais eficiente. Por exemplo, a IA pode sugerir produtos com base nos interesses e histórico de compras do cliente, facilitando o processo de venda e aumentando a satisfação do cliente.

## Custos de Operação da IA
Os custos de operação da IA incluem:

- **Infraestrutura de Servidor:** Custo mensal para manter servidores que hospedam o modelo de IA.
- **Treinamento do Modelo:** Investimentos em recursos computacionais para treinar a IA.
- **Manutenção e Atualizações:** Custos associados à atualização do modelo e manutenção contínua.

## Estrutura dos Dados
Os dados contém as seguintes colunas, cada uma com suas respectivas funções:

| Coluna                   | Descrição |
|--------------------------|-----------|
| ID                       | Identificador único do cliente |
| Nome                     | Nome completo do cliente |
| CPF                      | Cadastro de Pessoa Física |
| Cliente_ID               | Identificador único do cliente na base de dados |
| Produto                  | Produto adquirido pelo cliente |
| Categoria                | Categoria do produto |
| Data_Compra              | Data da compra realizada |
| Valor_Compra             | Valor total da compra |
| Quantidade_Parcelas      | Número de parcelas do pagamento |
| Data_Última_Compra       | Data da última compra realizada pelo cliente |
| Segmento                 | Segmento de mercado do cliente |
| Produto_Indicado         | Produto sugerido pela IA |
| Status_Indicação         | Status da indicação do produto |
| Interesses               | Interesses do cliente (ex: tecnologia, esportes) |
| Gastos_Mensais           | Valor médio gasto pelo cliente mensalmente |
| Salario                  | Salário do cliente |
| Tipo_Cartao_Credito     | Tipo do cartão de crédito do cliente |
| Gasto_Mensal_Cartao     | Gasto médio mensal no cartão de crédito |
| Viaja_Frequentemente     | Indica se o cliente viaja com frequência |
| Profissao                | Profissão do cliente |
| Renda_Mensal             | Renda mensal do cliente |
| Dependentes              | Número de dependentes do cliente |
| Gênero                   | Gênero do cliente |
| Data_Nascimento          | Data de nascimento do cliente |
| Idade                    | Idade do cliente |

## O que o código faz

Este código implementa uma interface web interativa para o treinamento e avaliação de modelos de machine learning, focada na criação de uma IA para otimizar atendimentos em call centers. Usando o framework Streamlit, o código permite que os operadores visualizem, treinem, e avaliem modelos de classificação com dados pré-processados sobre clientes. O processo inclui:

1. Visualização dos Dados: Exibe os dados tratados, possibilitando que os operadores compreendam melhor as características dos clientes, como perfil de gastos e interesses.

2. Pré-processamento: Realiza a conversão de variáveis categóricas em valores numéricos (ex.: tipos de cartão e planos), preparando os dados para o treinamento dos modelos.

3. Treinamento de Modelos: Treina dois modelos de classificação — Extra Trees e Decision Tree — utilizando um conjunto de dados dividido em treino e teste. Esse processo ajuda a prever categorias de clientes e, consequentemente, as melhores estratégias de atendimento e recomendação.

4. Avaliação do Desempenho: Avalia a precisão dos modelos e gera relatórios de classificação, permitindo a comparação de diferentes algoritmos para identificar o mais eficaz no contexto de atendimento ao cliente.

5. Validação Cruzada: Realiza validação cruzada para testar a estabilidade dos modelos e garantir que suas previsões se generalizam bem para novos dados.

6. Salvamento de Modelos: Possibilita salvar o modelo escolhido para uso posterior em produção, garantindo que os operadores tenham acesso a modelos bem-treinados e prontos para otimizar o atendimento ao cliente.

## Conclusão
Este projeto visa revolucionar a forma como os operadores de call center interagem com os clientes, utilizando tecnologia de ponta para melhorar a eficiência e a qualidade do atendimento.
