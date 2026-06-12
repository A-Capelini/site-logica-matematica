import streamlit as st
import pandas as pd

st.title("✍️ Atividade 2: Exercícios Avançados")
st.markdown("---")

st.write("""
Nesta etapa, vamos elevar o nível. As questões abaixo envolvem a análise de proposições compostas mais complexas, com foco na operação **Bicondicional ($\leftrightarrow$)** e em equivalências lógicas.
""")

# Questão 1: Análise de Tabela-Verdade (Bicondicional)
st.header("Questão 1: Operação Bicondicional")
st.write("Analise a tabela-verdade incompleta abaixo para a proposição composta: $(p \land q) \leftrightarrow p$")

# Criando a tabela incompleta para visualização
df_q1 = pd.DataFrame({
    "p": ["V", "V", "F", "F"],
    "q": ["V", "F", "V", "F"],
    "p ∧ q": ["V", "F", "F", "F"],
    "(p ∧ q) ↔ p": ["?", "?", "?", "?"]
})
st.table(df_q1)

st.write("Quais são, respectivamente, os valores lógicos (de cima para baixo) que completam a última coluna?")

q1_resp = st.radio(
    "Escolha a sequência correta:",
    [
        "A) V, V, V, V (Tautologia)",
        "B) V, F, V, V",
        "C) F, F, V, V",
        "D) V, F, F, F"
    ],
    key="atv2_q1"
)

if st.button("Verificar Resposta - Q1"):
    if q1_resp.startswith("B"):
        st.success("✅ **Correto!** Vamos analisar linha por linha:")
        st.write("""
        * **Linha 1:** $V \leftrightarrow V$ resulta em **V**
        * **Linha 2:** $F \leftrightarrow V$ resulta em **F**
        * **Linha 3:** $F \leftrightarrow F$ resulta em **V**
        * **Linha 4:** $F \leftrightarrow F$ resulta em **V**
        """)
    else:
        st.error("❌ **Incorreto.** Lembre-se da regra da Bicondicional: só é verdadeiro quando os dois lados são **iguais**.")

st.markdown("---")

# Questão 2: Equivalência Lógica
st.header("Questão 2: Equivalências Notáveis")
st.write("Uma das propriedades mais importantes da Lógica é a **Equivalência**. Duas proposições são equivalentes se possuem a mesma tabela-verdade.")
st.write("A proposição condicional $p \\rightarrow q$ é logicamente equivalente a qual das expressões abaixo?")

q2_resp = st.radio(
    "Selecione a expressão equivalente:",
    [
        "A) $\sim p \land q$",
        "B) $q \\rightarrow p$",
        "C) $\sim p \\vee q$",
        "D) $\sim q \land \sim p$"
    ],
    key="atv2_q2"
)

if st.button("Verificar Resposta - Q2"):
    if q2_resp.startswith("C"):
        st.success("✅ **Correto!** Esta é a famosa regra do 'Neymar' (Nega a primeira OU mantém a segunda). A condicional $p \\rightarrow q$ é equivalente à disjunção $\sim p \\vee q$.")
    else:
        st.error("❌ **Incorreto.** Dica: para transformar uma condicional em disjunção (OU), você precisa negar a primeira parte e manter a segunda.")

st.markdown("---")

# Questão 3: Tautologia, Contradição ou Contingência
st.header("Questão 3: Classificação")
st.write("Ao resolver a tabela-verdade da proposição composta $(p \\vee \sim p)$, verificamos que a última coluna apresentará apenas valores Verdadeiros (V).")
st.write("Como classificamos uma proposição que é **sempre verdadeira**, independentemente dos valores de suas proposições simples?")

q3_resp = st.radio(
    "Escolha a classificação:",
    [
        "A) Contingência",
        "B) Falácia",
        "C) Contradição",
        "D) Tautologia"
    ],
    key="atv2_q3"
)

if st.button("Verificar Resposta - Q3"):
    if q3_resp.startswith("D"):
        st.success("✅ **Correto!** Toda proposição cujo resultado final (última coluna da tabela-verdade) for composto apenas por 'V' é chamada de Tautologia.")
    else:
        st.error("❌ **Incorreto.** Revise os conceitos de classificação de fórmulas lógicas.")

st.markdown("<br>", unsafe_allow_html=True)
st.success("➡️ **Próximo passo:** Vamos consolidar tudo na aba *Mapa Mental*.")