import streamlit as st
import pandas as pd

# Título da Página
st.title("🔗 Módulo 2: Conectivos Lógicos e Tabelas-Verdade")
st.markdown("---")

# Introdução
st.write("""
Quando unimos duas ou mais proposições simples usando **conectivos lógicos**, formamos uma **proposição composta**. 
O valor lógico dessa nova proposição depende inteiramente dos valores das proposições simples que a compõem e do tipo de conectivo utilizado.
""")

st.info("💡 **Lembre-se da Fórmula:** Para calcular o número de linhas de uma tabela-verdade, usamos $2^n$, onde $n$ é o número de proposições simples (letras). Para duas proposições ($p$ e $q$), teremos $2^2 = 4$ linhas.")

st.markdown("---")
st.header("Os 5 Conectivos Fundamentais")
st.write("Selecione um conectivo abaixo para estudar sua definição e sua respectiva tabela-verdade:")

# Usando um selectbox para navegar entre os conectivos na mesma página
conectivo = st.selectbox(
    "Escolha o conectivo:",
    ["1. Negação (~ , ¬)", 
     "2. Conjunção (∧)", 
     "3. Disjunção Inclusiva (∨)", 
     "4. Condicional (→)", 
     "5. Bicondicional (↔)"]
)

st.markdown("---")

# 1. NEGAÇÃO
if conectivo.startswith("1"):
    st.subheader("1. Negação ($ ~ $, $\\neg$)")
    st.write("A negação não une proposições, ela atua sobre uma única proposição, invertendo seu valor lógico.")
    st.markdown("**Leitura:** 'Não p'")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        # Criando a tabela-verdade com Pandas
        df_negacao = pd.DataFrame({
            "p": ["V", "F"],
            "~p": ["F", "V"]
        })
        st.dataframe(df_negacao, hide_index=True, use_container_width=True)
    with col2:
        st.success("**Regra Prática:** O que era Verdade vira Falso. O que era Falso vira Verdade.")

# 2. CONJUNÇÃO
elif conectivo.startswith("2"):
    st.subheader("2. Conjunção ($\\wedge$)")
    st.write("A conjunção liga duas proposições com o sentido de 'E' (simultaneidade).")
    st.markdown("**Leitura:** 'p e q'")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        df_conjuncao = pd.DataFrame({
            "p": ["V", "V", "F", "F"],
            "q": ["V", "F", "V", "F"],
            "p ∧ q": ["V", "F", "F", "F"]
        })
        st.dataframe(df_conjuncao, hide_index=True, use_container_width=True)
    with col2:
        st.success("**Regra Prática:** Só é Verdade quando **TUDO for Verdade**.")

# 3. DISJUNÇÃO INCLUSIVA
elif conectivo.startswith("3"):
    st.subheader("3. Disjunção Inclusiva ($\\vee$)")
    st.write("A disjunção liga duas proposições com o sentido de 'OU'. Pelo menos uma delas precisa acontecer (podendo ser ambas).")
    st.markdown("**Leitura:** 'p ou q'")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        df_disjuncao = pd.DataFrame({
            "p": ["V", "V", "F", "F"],
            "q": ["V", "F", "V", "F"],
            "p ∨ q": ["V", "V", "V", "F"]
        })
        st.dataframe(df_disjuncao, hide_index=True, use_container_width=True)
    with col2:
        st.success("**Regra Prática:** Só é Falso quando **TUDO for Falso**.")
        st.info("*(Existe também a Disjunção Exclusiva 'Ou... ou' ($\\veebar$), onde as duas não podem ser verdadeiras ao mesmo tempo).*")

# 4. CONDICIONAL
elif conectivo.startswith("4"):
    st.subheader("4. Condicional ($\\rightarrow$)")
    st.write("A condicional estabelece uma relação de causa (antecedente) e consequência (consequente).")
    st.markdown("**Leitura:** 'Se p, então q'")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        df_condicional = pd.DataFrame({
            "p": ["V", "V", "F", "F"],
            "q": ["V", "F", "V", "F"],
            "p → q": ["V", "F", "V", "V"]
        })
        st.dataframe(df_condicional, hide_index=True, use_container_width=True)
    with col2:
        st.success("**Regra Prática:** Só é Falso na famosa combinação 'Vera Fischer' (Primeira V, Segunda F). Nos demais casos, é Verdade.")

# 5. BICONDICIONAL
elif conectivo.startswith("5"):
    st.subheader("5. Bicondicional ($\\leftrightarrow$)")
    st.write("A bicondicional indica uma dupla implicação. A primeira acarreta a segunda, e a segunda acarreta a primeira.")
    st.markdown("**Leitura:** 'p se, e somente se, q'")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        df_bicondicional = pd.DataFrame({
            "p": ["V", "V", "F", "F"],
            "q": ["V", "F", "V", "F"],
            "p ↔ q": ["V", "F", "F", "V"]
        })
        st.dataframe(df_bicondicional, hide_index=True, use_container_width=True)
    with col2:
        st.success("**Regra Prática:** Só é Verdade quando os valores são **IGUAIS** (V com V, ou F com F). Se forem diferentes, é Falso.")

st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)
st.success("➡️ **Próximo passo:** Vamos aplicar essas tabelas! Acesse a *Atividade 1* no menu.")