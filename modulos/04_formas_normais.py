import streamlit as st

st.title("🧮 Módulo 4: Formas Normais (FNC e FND)")
st.markdown("---")

st.write(r"""
Na lógica proposicional, as **Formas Normais** são maneiras padronizadas de escrever qualquer fórmula lógica. 
Elas são fundamentais na computação e na análise de dados para simplificar expressões e otimizar algoritmos de decisão (como satisfatibilidade booleana).

Toda fórmula possui duas representações canônicas principais:
""")

# Usando duas abas para separar FND e FNC de forma limpa
tab1, tab2 = st.tabs(["Forma Normal Disjuntiva (FND)", "Forma Normal Conjuntiva (FNC)"])

with tab1:
    st.subheader("Soma de Produtos (Disjunção de Conjunções)")
    st.write(r"""
    A **FND** é uma estrutura onde temos vários blocos unidos pelo conectivo **OU** ($\lor$), e dentro de cada bloco as letras estão unidas pelo conectivo **E** ($\land$).
    
    $$\text{Estrutura:} \quad (\text{Bloco}_1) \lor (\text{Bloco}_2) \lor (\text{Bloco}_3)$$
    
    * **Exemplo:** $(p \land q) \lor (\sim p \land r)$
    * **Como obter pela Tabela-Verdade:** Olhamos apenas para as linhas onde o resultado final da fórmula foi **Verdadeiro (V)**. Para cada linha V, criamos um termo com $\land$ (se a variável for F na linha, colocamos um $\sim$ nela) e juntamos todos os termos com $\lor$.
    """)
    st.info("💡 **Dica de associação:** Lembre-se de uma soma de multiplicações na álgebra comum: $(A \times B) + (C \times D)$.")

with tab2:
    st.subheader("Produto de Somas (Conjunção de Disjunções)")
    st.write(r"""
    A **FNC** é o exato oposto da FND. É uma estrutura onde temos vários blocos unidos pelo conectivo **E** ($\land$), e dentro de cada bloco as letras estão unidas pelo conectivo **OU** ($\lor$).
    
    $$\text{Estrutura:} \quad (\text{Bloco}_1) \land (\text{Bloco}_2) \land (\text{Bloco}_3)$$
    
    * **Exemplo:** $(p \lor \sim q) \land (\sim p \lor r)$
    * **Como obter pela Tabela-Verdade:** Olhamos para as linhas onde o resultado final foi **Falso (F)**. Negamos os valores das variáveis daquela linha e as unimos com $\lor$. Por fim, juntamos todos os blocos com $\land$.
    """)
    st.info("💡 **Dica de associação:** Lembra uma multiplicação de somas na álgebra comum: $(A + B) \times (C + D)$.")

st.markdown("---")
st.header("🔍 Conectivos de Scheffer")
st.write(r"""
O final do seu material introduz um conceito avançado: os operadores universais de Scheffer. Eles provam que você não precisa de todos os 5 conectivos para fazer lógica; basta apenas um deles!
""")

col1, col2 = st.columns(2)
with col1:
    st.markdown(r"""
    **NAND (Barra de Scheffer $|$)** Representa a negação da conjunção (Não E).
    * Definição: $p \mid q \equiv \sim(p \land q)$
    * É capaz de substituir sozinho a negação e a conjunção.
    """)

with col2:
    st.markdown(r"""
    **NOR (Seta de Peirce $\downarrow$)** Representa a negação da disjunção (Não OU).
    * Definição: $p \downarrow q \equiv \sim(p \lor q)$
    * É o conectivo base das memórias computacionais.
    """)

st.markdown("<br>", unsafe_allow_html=True)
st.success("➡️ **Roteiro de aulas concluído!** Você concluiu toda a base teórica. Siga para as abas de *Atividades* para testar seus conhecimentos.")