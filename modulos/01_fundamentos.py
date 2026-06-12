import streamlit as st

# Título da Página
st.title("📖 Módulo 1: Fundamentos da Lógica")
st.markdown("---")

# Introdução
st.header("O que é uma Proposição?")
st.write("""
Na Lógica Matemática, o conceito mais básico é o de **Proposição**. 
Uma proposição é uma sentença declarativa, expressa em palavras ou símbolos, que pode ser avaliada como **Verdadeira (V)** ou **Falsa (F)**, mas nunca ambas ao mesmo tempo.
""")

# Exemplos de Proposições
col1, col2 = st.columns(2)

with col1:
    st.success("✅ **SÃO Proposições:**")
    st.write("- Brasília é a capital do Brasil. *(Valor: V)*")
    st.write("- $2 + 2 = 5$ *(Valor: F)*")
    st.write("- A lua é feita de queijo. *(Valor: F)*")

with col2:
    st.error("❌ **NÃO SÃO Proposições:**")
    st.write("- Que horas são? *(Pergunta/Interrogativa)*")
    st.write("- Feche a porta! *(Ordem/Imperativa)*")
    st.write("- $x + 5 = 10$ *(Sentença aberta, depende de 'x')*")

st.markdown("---")

# Princípios Fundamentais
st.header("Os 3 Princípios Fundamentais")
st.write("A Lógica Clássica se baseia em três pilares inquebráveis. Sem eles, as regras e tabelas-verdade não funcionariam:")

# Usando abas (tabs) para organizar os princípios
tab1, tab2, tab3 = st.tabs(["Identidade", "Não-Contradição", "Terceiro Excluído"])

with tab1:
    st.subheader("1. Princípio da Identidade")
    st.write("Uma proposição verdadeira é verdadeira; uma proposição falsa é falsa.")
    st.info("💡 **Em resumo:** Se $P$ é verdadeiro, então $P$ é verdadeiro. $P = P$")

with tab2:
    st.subheader("2. Princípio da Não-Contradição")
    st.write("Uma proposição não pode ser verdadeira e falsa ao mesmo tempo.")
    st.info("💡 **Em resumo:** É impossível que $P$ e $\sim P$ (não $P$) sejam verdadeiros simultaneamente.")

with tab3:
    st.subheader("3. Princípio do Terceiro Excluído")
    st.write("Toda proposição ou é verdadeira ou é falsa, não havendo uma terceira possibilidade (um meio-termo).")
    st.info("💡 **Em resumo:** Para qualquer proposição $P$, ou $P$ é Verdadeiro ou $P$ é Falso. Não existe 'talvez'.")

st.markdown("---")

# Representação Simbólica
st.header("Representação Simbólica")
st.write("""
Para facilitar o cálculo lógico, não usamos frases inteiras. Representamos as proposições usando letras minúsculas (geralmente $p, q, r, s, t$).
""")

st.markdown("> **Exemplo:** \n> $p$: 'O céu é azul'  \n> $q$: 'A grama é verde'")

st.write("No próximo módulo, veremos como juntar essas 'letrinhas' usando os **Conectivos Lógicos** para formar proposições compostas!")

# Dica de navegação
st.markdown("<br>", unsafe_allow_html=True)
st.success("➡️ **Próximo passo:** Acesse o *Módulo 2: Conectivos e Tabelas* no menu lateral.")