# app.py
import random
import pandas as pd
import pickle
import streamlit as st
import matplotlib.pyplot as plt

with open('model/modelo_recomendacao.pkl', 'rb') as file:
    modelo = pickle.load(file)

df = pd.read_csv('/workspaces/cgeniusIA/dataset_versions/Dataset_Cliente_v1.2.0.csv')
st.title('Elite Sales - Recomendações de Call Center')
cpf = st.text_input('Digite o CPF do Cliente')

def buscar_cliente_por_cpf(cpf):
    cliente = df[df['CPF'] == cpf]
    return cliente
if cpf:
    cliente_info = buscar_cliente_por_cpf(cpf)
    
    if not cliente_info.empty:
        # Exibindo o nome do cliente
        nome_cliente = cliente_info['Nome'].values[0]
        produto_indicado = cliente_info['Produto_Indicado'].values[0]
        idade = cliente_info['Idade'].values[0]
        salario = cliente_info['Salario'].values[0]
        gastos_mensais = cliente_info["Gastos_Mensais"].values[0]
        renda_mensal = cliente_info["Renda_Mensal"].values[0]
        idade = cliente_info["Idade"].values[0]
        segmento = cliente_info["Segmento"].values[0]
        data_ultima_compra = cliente_info["Data_Última_Compra"].values[0]
        tipo_cartao_credito = cliente_info["Tipo_Cartao_Credito"].values[0]
        data_compra = cliente_info["Data_Compra"].values[0]
        valor_compra = cliente_info["Valor_Compra"].values[0]
        status_indicacao = cliente_info["Status_Indicação"].values[0]
        quantidade_parcelas = cliente_info["Quantidade_Parcelas"].values[0]
        st.subheader(f'Informações do Cliente: {nome_cliente}')
        
        # Exibindo as informações do cliente
        st.write(f'CPF: {cpf}')
        st.write(f'Gastos Mensais: R${gastos_mensais}')
        st.write(f'Renda Mensal: R${renda_mensal}')
        st.write(f'Idade: {idade} anos')
        st.write(f'Segmento: {segmento}')
        st.write(f'Ultima Compra: {data_ultima_compra}')
        st.write(f'Tipo de Cartão de Crédito: {tipo_cartao_credito}')

        st.subheader('Abordagem Simulada:')

        # Precisa organizar o "Interesse" que vem em uma ['']
        abordagens = [
            f"Oi, {nome_cliente}! Estou feliz em falar com você novamente. Considerando seu histórico de compras e interesses, notamos que você tem uma renda de {renda_mensal} e realiza gastos mensais de {gastos_mensais}. Temos uma nova indicação que pode se encaixar perfeitamente com suas necessidades e estilo de vida. Vamos conhecer essa nova opção?",
        #     f"Olá, {nome_cliente}! Espero que você esteja bem. Percebi que sua última compra foi um **{produto_indicado}** em **{data_compra}**, custando R$ {valor_compra:.2f}, com {quantidade_parcelas} parcelas. Você pertence ao segmento **{segmento}**, e atualmente, suas preferências incluem {', '.join(cliente_info['Interesses'].values[0])}. Considerando seus gastos mensais de R$ {gastos_mensais:.2f} e uma renda mensal de R$ {renda_mensal:.2f}, gostaria de compartilhar uma nova indicação que pode se alinhar perfeitamente ao seu estilo de vida.",
        #     f"Oi, {nome_cliente}! É sempre um prazer falar com você. Notamos que seu cartão de crédito é **{tipo_cartao_credito}** e você costuma gastar em média R$ {gastos_mensais:.2f} por mês. Além disso, seu histórico mostra que você viaja frequentemente, o que é maravilhoso! Com base na sua última compra em **{data_ultima_compra}**, estamos animados para recomendar algo que pode complementar suas experiências de viagem e lazer. Vamos explorar juntos essa nova oportunidade!",
        #     f"Bom dia, {nome_cliente}! Com base nas suas informações, como sua idade de {idade} anos e seu status de indicação **{status_indicacao}**, identificamos um produto que pode ser muito valioso para você. Você mencionou interesse em {', '.join(cliente_info['Interesses'].values[0])}, e com sua renda mensal de R$ {renda_mensal:.2f}, temos certeza de que essa recomendação vai te surpreender! Que tal conhecer mais sobre essa opção?",
        #     f"Olá, {nome_cliente}! É sempre bom conversar com alguém tão antenado em novas tendências como você. Sabemos que você possui um perfil financeiro interessante, com um salário de R$ {salario:.2f} e gastos mensais que giram em torno de R$ {gastos_mensais:.2f}. Recentemente, fizemos uma análise e notamos que o produto que você adquiriu foi o **{produto_indicado}**. Temos uma sugestão de um produto que pode não apenas atender suas expectativas, mas também melhorar seu dia a dia. Que tal saber mais sobre isso?",
        #     f"Oi, {nome_cliente}! Notamos que você está sempre em busca de novas experiências e, com base em seus interesses em {', '.join(cliente_info['Interesses'].values[0])}, temos algo especial para compartilhar. Além do mais, sua última compra foi um **{produto_indicado}**, e isso mostra que você aprecia qualidade. Dado que você é do segmento **{segmento}**, achamos que esta nova indicação pode realmente fazer a diferença no seu cotidiano. Vamos conversar sobre isso?",
        #     f"Bom dia, {nome_cliente}! Como você está hoje? Temos um produto que acreditamos que se encaixa perfeitamente com o seu estilo de vida. Com base no seu histórico de compras, como a aquisição do **{produto_indicado}** em **{data_compra}**, e seus interesses em {', '.join(cliente_info['Interesses'].values[0])}, estamos certos de que esta nova recomendação pode agregar muito valor ao seu dia a dia. Vamos explorar juntos essa nova possibilidade?",
        #     f"Olá, {nome_cliente}! Espero que sua semana esteja sendo produtiva. Recentemente, vimos que você fez uma compra de um **{produto_indicado}** e estamos aqui para lhe mostrar algo que pode ser ainda mais interessante. Com uma renda mensal de R$ {renda_mensal:.2f} e um gasto mensal de R$ {gastos_mensais:.2f}, acreditamos que a nova recomendação pode encaixar-se perfeitamente no seu planejamento financeiro e nas suas preferências.",
        #     f"Oi, {nome_cliente}! Sabemos que você é um(a) profissional ativo(a) e gosta de explorar novas opções de produtos. Considerando seus interesses em {', '.join(cliente_info['Interesses'].values[0])} e o fato de que você costuma viajar frequentemente, gostaríamos de apresentar uma indicação que pode se adaptar ao seu estilo de vida dinâmico. Estamos certos de que será algo que você vai amar!",
        #     f"Bom dia, {nome_cliente}! A sua trajetória com a gente tem sido incrível, e estamos sempre em busca de melhorias para te surpreender. Com seu perfil financeiro e seus interesses diversos, como **{', '.join(cliente_info['Interesses'].values[0])}**, encontramos um produto que acreditamos que irá adicionar um valor significativo ao seu dia a dia. Que tal conhecê-lo?",
        #     f"Olá, {nome_cliente}! Como você está se sentindo hoje? Sabemos que você é alguém que aprecia novas experiências e, com base no seu histórico de compras e interesses, estamos animados para compartilhar uma nova recomendação. Dado seu salário de R$ {salario:.2f} e seus gastos mensais, esta é uma oportunidade que certamente se encaixa no que você procura!",
        #     f"Oi, {nome_cliente}! Percebi que você fez uma compra recente de um **{produto_indicado}**, e gostaria de discutir algo que poderia potencializar ainda mais essa experiência. Com uma renda mensal de R$ {renda_mensal:.2f}, seus gastos mensais de R$ {gastos_mensais:.2f} e seus interesses variados em {', '.join(cliente_info['Interesses'].values[0])}, tenho certeza de que essa nova recomendação vai te surpreender positivamente.",
        #     f"Bom dia, {nome_cliente}! Espero que sua rotina esteja fluindo bem. Com seus interesses diversificados em {', '.join(cliente_info['Interesses'].values[0])}, e considerando que sua última compra foi em **{data_ultima_compra}**, estamos prontos para lhe apresentar uma nova indicação que pode tornar sua experiência ainda mais satisfatória. Vamos conversar mais sobre isso?",
        #     f"Olá, {nome_cliente}! Como vai? Recentemente, analisamos seu perfil e notamos que você está sempre em busca de inovações, especialmente em relação ao seu cartão **{tipo_cartao_credito}**. Sua última compra foi um **{produto_indicado}**, e achamos que uma nova recomendação pode se encaixar perfeitamente com seus interesses, que incluem {', '.join(cliente_info['Interesses'].values[0])}. Vamos explorar isso juntos?",
        #     f"Oi, {nome_cliente}! Estou feliz em falar com você novamente. Com seu salário de R$ {salario:.2f} e seus gastos mensais, estamos sempre buscando formas de aprimorar sua experiência. Notamos que você possui interesses em {', '.join(cliente_info['Interesses'].values[0])} e gostaríamos de apresentar uma nova indicação que pode te interessar. Vamos descobrir mais sobre isso?",
        #     f"Bom dia, {nome_cliente}! Que alegria poder te contatar! Ao analisarmos seu histórico de compras, percebemos que você adquire produtos que realmente fazem a diferença no seu cotidiano. A última compra que você fez foi um **{produto_indicado}**, e achamos que temos uma recomendação que vai se alinhar perfeitamente aos seus interesses, como **{', '.join(cliente_info['Interesses'].values[0])}**. Vamos conhecer juntos essa nova opção?",
        #     f"Olá, {nome_cliente}! Como você está? Observamos que você tem interesse em produtos relacionados a **{', '.join(cliente_info['Interesses'].values[0])}**, e isso nos trouxe uma ideia incrível para te apresentar. Sabemos que sua última compra foi em **{data_ultima_compra}** e gostaríamos de sugerir um produto que não só atende suas necessidades, mas que também pode melhorar sua experiência com compras futuras. Vamos conversar?",
        #     f"Oi, {nome_cliente}! Espero que esteja tendo um ótimo dia. Sabemos que você está sempre em busca de inovação e qualidade, especialmente em relação ao seu cartão de crédito **{tipo_cartao_credito}**. Considerando seus gastos mensais de R$ {gastos_mensais:.2f} e sua renda de R$ {renda_mensal:.2f}, temos algo que pode ser muito interessante para você. Vamos conhecer essa nova indicação?",
        #     f"Bom dia, {nome_cliente}! Que bom que estamos juntos novamente. Ao revisitar seu histórico de compras, notamos que você fez uma aquisição de um **{produto_indicado}** recentemente. Levando em conta seu estilo de vida e seus interesses em {', '.join(cliente_info['Interesses'].values[0])}, acreditamos que temos uma recomendação que pode tornar sua experiência ainda mais gratificante. Vamos explorar isso?",
        #     f"Olá, {nome_cliente}! Como você está se sentindo hoje? Sua trajetória conosco tem sido muito inspiradora, e com seu histórico financeiro, que inclui uma renda de R$ {renda_mensal:.2f}, temos a certeza de que podemos oferecer algo que realmente vai se encaixar no que você procura. Que tal conhecer uma nova sugestão que pode atender seus interesses em {', '.join(cliente_info['Interesses'].values[0])}?",
        #     f"Oi, {nome_cliente}! Espero que seu dia esteja maravilhoso. Com sua experiência no segmento **{segmento}** e seu último produto adquirido, temos certeza de que uma nova recomendação pode ser exatamente o que você precisa para aprimorar sua jornada. Vamos conversar sobre isso?",
        #     f"Bom dia, {nome_cliente}! Como você está? Sabemos que você gosta de produtos que fazem a diferença, e sua última compra foi um **{produto_indicado}**. Temos uma nova sugestão que pode ser ideal para você, especialmente com seus interesses em {', '.join(cliente_info['Interesses'].values[0])}. Que tal explorarmos isso juntos?",
        #     f"Olá, {nome_cliente}! Como anda sua rotina? Sabemos que você possui um perfil financeiro bem definido, com uma renda mensal de R$ {renda_mensal:.2f} e gastos mensais de R$ {gastos_mensais:.2f}. Com base nas suas preferências em {', '.join(cliente_info['Interesses'].values[0])}, estamos prontos para te apresentar uma nova indicação que pode agregar muito à sua experiência. Vamos conhecer?",
        #     f"Oi, {nome_cliente}! Que bom falar com você! Sua trajetória conosco tem sido valiosa, e sempre buscamos maneiras de te surpreender. Notamos que você viaja frequentemente e que seu cartão é **{tipo_cartao_credito}**. Com isso em mente, temos uma recomendação que pode se encaixar perfeitamente em seu estilo de vida. Vamos conversar?",
        #     f"Bom dia, {nome_cliente}! Espero que você esteja bem. Ao revisitar seu perfil, notamos que sua última compra foi um **{produto_indicado}**. Além disso, sua renda mensal e gastos mensais são relevantes para que possamos oferecer algo que atenda suas expectativas. Com seus interesses em {', '.join(cliente_info['Interesses'].values[0])}, que tal conhecermos uma nova opção juntos?",
        #     f"Olá, {nome_cliente}! Como você se sente hoje? Notamos que você está sempre buscando novas experiências, e com sua última compra em **{data_ultima_compra}**, temos uma recomendação que pode muito bem se alinhar com seus interesses em {', '.join(cliente_info['Interesses'].values[0])}. Vamos descobrir mais sobre isso?",
        #     f"Oi, {nome_cliente}! Estou feliz em falar com você novamente. Considerando seu histórico de compras e interesses, notamos que você tem uma renda de R$ {renda_mensal:.2f} e realiza gastos mensais de R$ {gastos_mensais:.2f}. Temos uma nova indicação que pode se encaixar perfeitamente com suas necessidades e estilo de vida. Vamos conhecer essa nova opção?",
        #     f"Bom dia, {nome_cliente}! Que alegria poder te contatar! Ao analisarmos seu perfil, percebemos que você adquire produtos que realmente fazem a diferença no seu cotidiano. A última compra que você fez foi um **{produto_indicado}**, e achamos que temos uma recomendação que vai se alinhar perfeitamente aos seus interesses, como **{', '.join(cliente_info['Interesses'].values[0])}**. Vamos conhecer juntos essa nova opção?",
        #     f"Olá, {nome_cliente}! Como você está? Observamos que você tem interesse em produtos relacionados a **{', '.join(cliente_info['Interesses'].values[0])}**, e isso nos trouxe uma ideia incrível para te apresentar. Sabemos que sua última compra foi em **{data_ultima_compra}** e gostaríamos de sugerir um produto que não só atende suas necessidades, mas que também pode melhorar sua experiência com compras futuras. Vamos conversar?",
        #     f"Oi, {nome_cliente}! Espero que esteja tendo um ótimo dia. Sabemos que você está sempre em busca de inovação e qualidade, especialmente em relação ao seu cartão de crédito **{tipo_cartao_credito}**. Considerando seus gastos mensais de R$ {gastos_mensais:.2f} e sua renda de R$ {renda_mensal:.2f}, temos algo que pode ser muito interessante para você. Vamos conhecer essa nova indicação?",
        #     f"Bom dia, {nome_cliente}! Que bom que estamos juntos novamente. Ao revisitar seu histórico de compras, notamos que você fez uma aquisição de um **{produto_indicado}** recentemente. Levando em conta seu estilo de vida e seus interesses em {', '.join(cliente_info['Interesses'].values[0])}, acreditamos que temos uma recomendação que pode tornar sua experiência ainda mais gratificante. Vamos explorar isso?",
        #     f"Olá, {nome_cliente}! Como você está se sentindo hoje? Sua trajetória conosco tem sido muito inspiradora, e com seu histórico financeiro, que inclui uma renda de R$ {renda_mensal:.2f}, temos a certeza de que podemos oferecer algo que realmente vai se encaixar no que você procura. Que tal conhecer uma nova sugestão que pode atender seus interesses em {', '.join(cliente_info['Interesses'].values[0])}?",
        #     f"Oi, {nome_cliente}! Espero que seu dia esteja maravilhoso. Com sua experiência no segmento **{segmento}** e seu último produto adquirido, temos certeza de que uma nova recomendação pode ser exatamente o que você precisa para aprimorar sua jornada. Vamos conversar sobre isso?",
        #     f"Bom dia, {nome_cliente}! Como você está? Sabemos que você gosta de produtos que fazem a diferença, e sua última compra foi um **{produto_indicado}**. Temos uma nova sugestão que pode ser ideal para você, especialmente com seus interesses em {', '.join(cliente_info['Interesses'].values[0])}. Que tal explorarmos isso juntos?",
        #     f"Olá, {nome_cliente}! Como anda sua rotina? Sabemos que você possui um perfil financeiro bem definido, com uma renda mensal de R$ {renda_mensal:.2f} e gastos mensais de R$ {gastos_mensais:.2f}. Com base nas suas preferências em {', '.join(cliente_info['Interesses'].values[0])}, estamos prontos para te apresentar uma nova indicação que pode agregar muito à sua experiência. Vamos conhecer?",
        #     f"Oi, {nome_cliente}! Que bom falar com você! Sua trajetória conosco tem sido valiosa, e sempre buscamos maneiras de te surpreender. Notamos que você viaja frequentemente e que seu cartão é **{tipo_cartao_credito}**. Com isso em mente, temos uma recomendação que pode se encaixar perfeitamente em seu estilo de vida. Vamos conversar?",
        #     f"Bom dia, {nome_cliente}! Espero que você esteja bem. Ao revisitar seu perfil, notamos que sua última compra foi um **{produto_indicado}**. Além disso, sua renda mensal e gastos mensais são relevantes para que possamos oferecer algo que atenda suas expectativas. Com seus interesses em {', '.join(cliente_info['Interesses'].values[0])}, que tal conhecermos uma nova opção juntos?",
        #     f"Olá, {nome_cliente}! Como você se sente hoje? Notamos que você está sempre buscando novas experiências, e com sua última compra em **{data_ultima_compra}**, temos uma recomendação que pode muito bem se alinhar com seus interesses em {', '.join(cliente_info['Interesses'].values[0])}. Vamos descobrir mais sobre isso?",
        #     f"Bom dia, {nome_cliente}! Que alegria poder te contatar! Ao analisarmos seu perfil, percebemos que você adquire produtos que realmente fazem a diferença no seu cotidiano. A última compra que você fez foi um **{produto_indicado}**, e achamos que temos uma recomendação que vai se alinhar perfeitamente aos seus interesses, como **{', '.join(cliente_info['Interesses'].values[0])}**. Vamos conhecer juntos essa nova opção?",
        #     f"Olá, {nome_cliente}! Como você está? Observamos que você tem interesse em produtos relacionados a **{', '.join(cliente_info['Interesses'].values[0])}**, e isso nos trouxe uma ideia incrível para te apresentar. Sabemos que sua última compra foi em **{data_ultima_compra}** e gostaríamos de sugerir um produto que não só atende suas necessidades, mas que também pode melhorar sua experiência com compras futuras. Vamos conversar?",
        #     f"Oi, {nome_cliente}! Espero que esteja tendo um ótimo dia. Sabemos que você está sempre em busca de inovação e qualidade, especialmente em relação ao seu cartão de crédito **{tipo_cartao_credito}**. Considerando seus gastos mensais de R$ {gastos_mensais:.2f} e sua renda de R$ {renda_mensal:.2f}, temos algo que pode ser muito interessante para você. Vamos conhecer essa nova indicação?",
        #     f"Bom dia, {nome_cliente}! Que bom que estamos juntos novamente. Ao revisitar seu histórico de compras, notamos que você fez uma aquisição de um **{produto_indicado}** recentemente. Levando em conta seu estilo de vida e seus interesses em {', '.join(cliente_info['Interesses'].values[0])}, acreditamos que temos uma recomendação que pode tornar sua experiência ainda mais gratificante. Vamos explorar isso?",
        #     f"Olá, {nome_cliente}! Como você está se sentindo hoje? Sua trajetória conosco tem sido muito inspiradora, e com seu histórico financeiro, que inclui uma renda de R$ {renda_mensal:.2f}, temos a certeza de que podemos oferecer algo que realmente vai se encaixar no que você procura. Que tal conhecer uma nova sugestão que pode atender seus interesses em {', '.join(cliente_info['Interesses'].values[0])}?",
        #     f"Oi, {nome_cliente}! Espero que seu dia esteja maravilhoso. Com sua experiência no segmento **{segmento}** e seu último produto adquirido, temos certeza de que uma nova recomendação pode ser exatamente o que você precisa para aprimorar sua jornada. Vamos conversar sobre isso?",
        #     f"Bom dia, {nome_cliente}! Como você está? Sabemos que você gosta de produtos que fazem a diferença, e sua última compra foi um **{produto_indicado}**. Temos uma nova sugestão que pode ser ideal para você, especialmente com seus interesses em {', '.join(cliente_info['Interesses'].values[0])}. Que tal explorarmos isso juntos?",
        #     f"Olá, {nome_cliente}! Como anda sua rotina? Sabemos que você possui um perfil financeiro bem definido, com uma renda mensal de R$ {renda_mensal:.2f} e gastos mensais de R$ {gastos_mensais:.2f}. Com base nas suas preferências em {', '.join(cliente_info['Interesses'].values[0])}, estamos prontos para te apresentar uma nova indicação que pode agregar muito à sua experiência. Vamos conhecer?",
        #     f"Oi, {nome_cliente}! Que bom falar com você! Sua trajetória conosco tem sido valiosa, e sempre buscamos maneiras de te surpreender. Notamos que você viaja frequentemente e que seu cartão é **{tipo_cartao_credito}**. Com isso em mente, temos uma recomendação que pode se encaixar perfeitamente em seu estilo de vida. Vamos conversar?",
        #     f"Bom dia, {nome_cliente}! Espero que você esteja bem. Ao revisitar seu perfil, notamos que sua última compra foi um **{produto_indicado}**. Além disso, sua renda mensal e gastos mensais são relevantes para que possamos oferecer algo que atenda suas expectativas. Com seus interesses em {', '.join(cliente_info['Interesses'].values[0])}, que tal conhecermos uma nova opção juntos?",
        #     f"Olá, {nome_cliente}! Como você se sente hoje? Notamos que você está sempre buscando novas experiências, e com sua última compra em **{data_ultima_compra}**, temos uma recomendação que pode muito bem se alinhar com seus interesses em {', '.join(cliente_info['Interesses'].values[0])}. Vamos descobrir mais sobre isso?",
        #     f"Oi, {nome_cliente}! Estou feliz em falar com você novamente. Considerando seu histórico de compras e interesses, notamos que você tem uma renda de R$ {renda_mensal:.2f} e realiza gastos mensais de R$ {gastos_mensais:.2f}. Temos uma nova indicação que pode se encaixar perfeitamente com suas necessidades e estilo de vida. Vamos conhecer essa nova opção?",
        #     f"Bom dia, {nome_cliente}! Que alegria poder te contatar! Ao analisarmos seu perfil, percebemos que você adquire produtos que realmente fazem a diferença no seu cotidiano. A última compra que você fez foi um **{produto_indicado}**, e achamos que temos uma recomendação que vai se alinhar perfeitamente aos seus interesses, como **{', '.join(cliente_info['Interesses'].values[0])}**. Vamos conhecer juntos essa nova opção?",
        #     f"Olá, {nome_cliente}! Como você está? Observamos que você tem interesse em produtos relacionados a **{', '.join(cliente_info['Interesses'].values[0])}**, e isso nos trouxe uma ideia incrível para te apresentar. Sabemos que sua última compra foi em **{data_ultima_compra}** e gostaríamos de sugerir um produto que não só atende suas necessidades, mas que também pode melhorar sua experiência com compras futuras. Vamos conversar?",
        #     f"Oi, {nome_cliente}! Espero que esteja tendo um ótimo dia. Sabemos que você está sempre em busca de inovação e qualidade, especialmente em relação ao seu cartão de crédito **{tipo_cartao_credito}**. Considerando seus gastos mensais de R$ {gastos_mensais:.2f} e sua renda de R$ {renda_mensal:.2f}, temos algo que pode ser muito interessante para você. Vamos conhecer essa nova indicação?",
        #     f"Bom dia, {nome_cliente}! Que bom que estamos juntos novamente. Ao revisitar seu histórico de compras, notamos que você fez uma aquisição de um **{produto_indicado}** recentemente. Levando em conta seu estilo de vida e seus interesses em {', '.join(cliente_info['Interesses'].values[0])}, acreditamos que temos uma recomendação que pode tornar sua experiência ainda mais gratificante. Vamos explorar isso?",
        #     f"Olá, {nome_cliente}! Como você está se sentindo hoje? Sua trajetória conosco tem sido muito inspiradora, e com seu histórico financeiro, que inclui uma renda de R$ {renda_mensal:.2f}, temos a certeza de que podemos oferecer algo que realmente vai se encaixar no que você procura. Que tal conhecer uma nova sugestão que pode atender seus interesses em {', '.join(cliente_info['Interesses'].values[0])}?",
        #     f"Oi, {nome_cliente}! Espero que seu dia esteja maravilhoso. Com sua experiência no segmento **{segmento}** e seu último produto adquirido, temos certeza de que uma nova recomendação pode ser exatamente o que você precisa para aprimorar sua jornada. Vamos conversar sobre isso?",
        #     f"Bom dia, {nome_cliente}! Como você está? Sabemos que você gosta de produtos que fazem a diferença, e sua última compra foi um **{produto_indicado}**. Temos uma nova sugestão que pode ser ideal para você, especialmente com seus interesses em {', '.join(cliente_info['Interesses'].values[0])}. Que tal explorarmos isso juntos?",
        #     f"Olá, {nome_cliente}! Como anda sua rotina? Sabemos que você possui um perfil financeiro bem definido, com uma renda mensal de R$ {renda_mensal:.2f} e gastos mensais de R$ {gastos_mensais:.2f}. Com base nas suas preferências em {', '.join(cliente_info['Interesses'].values[0])}, estamos prontos para te apresentar uma nova indicação que pode agregar muito à sua experiência. Vamos conhecer?",
        #     f"Oi, {nome_cliente}! Que bom falar com você! Sua trajetória conosco tem sido valiosa, e sempre buscamos maneiras de te surpreender. Notamos que você viaja frequentemente e que seu cartão é **{tipo_cartao_credito}**. Com isso em mente, temos uma recomendação que pode se encaixar perfeitamente em seu estilo de vida. Vamos conversar?",
        #     f"Bom dia, {nome_cliente}! Espero que você esteja bem. Ao revisitar seu perfil, notamos que sua última compra foi um **{produto_indicado}**. Além disso, sua renda mensal e gastos mensais são relevantes para que possamos oferecer algo que atenda suas expectativas. Com seus interesses em {', '.join(cliente_info['Interesses'].values[0])}, que tal conhecermos uma nova opção juntos?",
        #     f"Olá, {nome_cliente}! Como você se sente hoje? Notamos que você está sempre buscando novas experiências, e com sua última compra em **{data_ultima_compra}**, temos uma recomendação que pode muito bem se alinhar com seus interesses em {', '.join(cliente_info['Interesses'].values[0])}. Vamos descobrir mais sobre isso?"
        #     f"Oi, {nome_cliente}! Estou feliz em falar com você novamente. Considerando seu histórico de compras e interesses, notamos que você tem uma renda de R$ {renda_mensal:.2f} e realiza gastos mensais de R$ {gastos_mensais:.2f}. Temos uma nova indicação que pode se encaixar perfeitamente com suas necessidades e estilo de vida. Vamos conhecer essa nova opção?",
        #     f"Bom dia, {nome_cliente}! Que alegria poder te contatar! Ao analisarmos seu perfil, percebemos que você adquire produtos que realmente fazem a diferença no seu cotidiano. A última compra que você fez foi um **{produto_indicado}**, e achamos que temos uma recomendação que vai se alinhar perfeitamente aos seus interesses, como **{', '.join(cliente_info['Interesses'].values[0])}**. Vamos conhecer juntos essa nova opção?",
        #     f"Olá, {nome_cliente}! Como você está? Observamos que você tem interesse em produtos relacionados a **{', '.join(cliente_info['Interesses'].values[0])}**, e isso nos trouxe uma ideia incrível para te apresentar. Sabemos que sua última compra foi em **{data_ultima_compra}** e gostaríamos de sugerir um produto que não só atende suas necessidades, mas que também pode melhorar sua experiência com compras futuras. Vamos conversar?",
        #     f"Oi, {nome_cliente}! Espero que esteja tendo um ótimo dia. Sabemos que você está sempre em busca de inovação e qualidade, especialmente em relação ao seu cartão de crédito **{tipo_cartao_credito}**. Considerando seus gastos mensais de R$ {gastos_mensais:.2f} e sua renda de R$ {renda_mensal:.2f}, temos algo que pode ser muito interessante para você. Vamos conhecer essa nova indicação?",
        #     f"Bom dia, {nome_cliente}! Que bom que estamos juntos novamente. Ao revisitar seu histórico de compras, notamos que você fez uma aquisição de um **{produto_indicado}** recentemente. Levando em conta seu estilo de vida e seus interesses em {', '.join(cliente_info['Interesses'].values[0])}, acreditamos que temos uma recomendação que pode tornar sua experiência ainda mais gratificante. Vamos explorar isso?",
        #     f"Olá, {nome_cliente}! Como você está se sentindo hoje? Sua trajetória conosco tem sido muito inspiradora, e com seu histórico financeiro, que inclui uma renda de R$ {renda_mensal:.2f}, temos a certeza de que podemos oferecer algo que realmente vai se encaixar no que você procura. Que tal conhecer uma nova sugestão que pode atender seus interesses em {', '.join(cliente_info['Interesses'].values[0])}?",
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

        interesses = cliente_info['Interesses'].values[0]
        interesses_lista = interesses.split(", ")
        def gerar_porcentagens_aleatorias(n):
            random_values = [random.random() for _ in range(n)]
            soma = sum(random_values)
            return [valor / soma for valor in random_values]

        # Gerar as porcentagens aleatórias para cada interesse
        tamanhos_aleatorios = gerar_porcentagens_aleatorias(len(interesses_lista))

        # Separando os rótulos e valores para o gráfico
        labels = interesses_lista
        sizes = [tam * 100 for tam in tamanhos_aleatorios]  # Multiplicando por 100 para converter em porcentagens

        # Criando o gráfico de pizza
        fig2, ax2 = plt.subplots()
        ax2.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax2.axis('equal')
        ax2.set_title('Distribuição Aleatória de Interesses do Cliente')
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
