import streamlit as st
import pandas as pd

st.title("⚖️ Módulo 3: Equivalências Lógicas")
st.markdown("---")

st.write(r"""
Dizemos que duas proposições compostas são **logicamente equivalentes** quando as suas tabelas-verdade são absolutamente idênticas. 
Usamos o símbolo $\equiv$ ou $\Leftrightarrow$ para indicar que uma fórmula pode ser substituída pela outra sem alterar o seu significado lógico.
""")

st.subheader("Exemplo Prático na Tabela-Verdade")
st.write(r"Vamos provar que a condicional $p \rightarrow q$ é equivalente a $\sim p \lor q$:")

# Gerando dataframe para provar a equivalência
df_equiv = pd.DataFrame({
    "p": ["V", "V", "F", "F"],
    "q": ["V", "F", "V", "F"],
    "~p": ["F", "F", "V", "V"],
    "p → q": ["V", "F", "V", "V"],
    "~p ∨ q": ["V", "F", "V", "V"]
})

# Destacando as colunas idênticas
st.dataframe(df_equiv, hide_index=True, use_container_width=True)
st.success(r"💡 Veja que as colunas **$p \rightarrow q$** e **$\sim p \lor q$** são iguais linha por linha! Provado: $p \rightarrow q \equiv \sim p \lor q$.")

st.markdown("---")
st.header("Principais Leis de Equivalência (Álgebra Proposicional)")
st.write("Estas são as propriedades mais cobradas e utilizadas para simplificar expressões lógicas:")

# Organizando as leis em colunas para impacto visual
col1, col2 = st.columns(2)

with col1:
    st.info(r"""
    **1. Leis de De Morgan (Negação de Compostas)**
    * Negação do 'E':
      $$\sim(p \land q) \equiv \sim p \lor \sim q$$
    * Negação do 'OU':
      $$\sim(p \lor q) \equiv \sim p \land \sim q$$
    
    **2. Equivalências da Condicional**
    * Condicional para Disjunção (Regra do Neymar):
      $$p \rightarrow q \equiv \sim p \lor q$$
    * Contrapositiva (Inverte negando):
      $$p \rightarrow q \equiv \sim q \rightarrow \sim p$$
    """)

with col2:
    st.info(r"""
    **3. Leis Distributivas**
    * Distribuição do E sobre o OU:
      $$p \land (q \lor r) \equiv (p \land q) \lor (p \land r)$$
    * Distribuição do OU sobre o E:
      $$p \lor (q \land r) \equiv (p \lor q) \land (p \lor r)$$
      
    **4. Lei da Dupla Negação e Absorção**
    * Dupla negação:
      $$\sim(\sim p) \equiv p$$
    * Absorção:
      $$p \land (p \lor q) \equiv p$$
    """)

st.markdown("<br>", unsafe_allow_html=True)
st.success("➡️ **Próximo passo:** Entenda como usar essas leis para padronizar fórmulas no *Módulo 4: Formas Normais*.")