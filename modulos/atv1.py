import streamlit as st

st.title("📝 Atividade 1: Fixação de Conceitos")
st.markdown("---")

st.write("""
Teste seus conhecimentos sobre proposições e conectivos lógicos. 
Responda às questões abaixo e clique em 'Verificar Resposta' para ver a resolução.
""")

# Questão 1: Identificação de Proposições
st.header("Questão 1")
st.write("Qual das alternativas abaixo **NÃO** representa uma proposição lógica?")

q1_resp = st.radio(
    "Escolha uma opção:",
    [
        "A) A Terra gira em torno do Sol.",
        "B) O número 5 é par.",
        "C) Leia as instruções antes de começar a prova.",
        "D) 10 + 5 = 15."
    ],
    key="q1"
)

if st.button("Verificar Resposta - Q1"):
    if q1_resp.startswith("C"):
        st.success("✅ **Correto!** Frases imperativas (ordens) não possuem valor lógico (V ou F), portanto não são proposições.")
    else:
        st.error("❌ **Incorreto.** Lembre-se: ordens, perguntas e exclamações não são proposições.")

st.markdown("---")

# Questão 2: Tradução para Linguagem Simbólica
st.header("Questão 2")
st.write("""
Dadas as proposições:
* **p:** 'Marcos estuda.'
* **q:** 'Marcos passa de ano.'

Como traduzimos a frase: *"Se Marcos estuda, então ele passa de ano"* para a linguagem simbólica?
""")

q2_resp = st.radio(
    "Escolha a alternativa que representa a Condicional:",
    [
        "A) $p \land q$",
        "B) $p \\vee q$",
        "C) $p \\leftrightarrow q$",
        "D) $p \\rightarrow q$"
    ],
    key="q2"
)

if st.button("Verificar Resposta - Q2"):
    if q2_resp.startswith("D"):
        st.success("✅ **Correto!** A estrutura 'Se... então' é representada pelo conectivo Condicional ($\\rightarrow$).")
    else:
        st.error("❌ **Incorreto.** Revise os conectivos lógicos no Módulo 2.")

st.markdown("---")

# Questão 3: Tabela-Verdade (Bicondicional)
st.header("Questão 3")
st.write("Na tabela-verdade do conectivo **Bicondicional ($p \\leftrightarrow q$)**, a proposição composta será avaliada como **Verdadeira (V)** quando:")

q3_resp = st.radio(
    "Selecione a regra correta:",
    [
        "A) As proposições p e q tiverem valores lógicos diferentes.",
        "B) As proposições p e q tiverem valores lógicos iguais.",
        "C) Apenas quando ambas forem falsas.",
        "D) Apenas quando a primeira for verdadeira e a segunda falsa."
    ],
    key="q3"
)

if st.button("Verificar Resposta - Q3"):
    if q3_resp.startswith("B"):
        st.success("✅ **Correto!** A Bicondicional ('se, e somente se') exige que ambas as proposições tenham o mesmo valor (V com V, ou F com F) para ser verdadeira.")
    else:
        st.error("❌ **Incorreto.** A Bicondicional é a regra da 'igualdade' lógica.")

st.markdown("<br>", unsafe_allow_html=True)
st.success("➡️ **Próximo passo:** Continue para a *Atividade 2* ou revise o *Mapa Mental*.")