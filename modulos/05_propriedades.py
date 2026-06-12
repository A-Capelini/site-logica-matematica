import streamlit as st

st.title("📏 Módulo 5: Propriedades das Operações Lógicas")
st.markdown("---")

st.write("""
Assim como na matemática básica nós temos regras (como $2 \\times 3 = 3 \\times 2$), na Lógica Proposicional também temos uma **Álgebra das Proposições**. 
Essas propriedades nos permitem manipular e simplificar fórmulas complexas sem precisar construir tabelas-verdade gigantes.
""")

st.header("Principais Propriedades")

col1, col2 = st.columns(2)

with col1:
    with st.expander("1. Idempotência", expanded=True):
        st.write("Uma proposição operada com ela mesma resulta nela mesma.")
        st.latex(r"p \lor p \equiv p")
        st.latex(r"p \land p \equiv p")

    with st.expander("2. Comutativa"):
        st.write("A ordem das proposições não altera o resultado (válido para E, OU, Bicondicional).")
        st.latex(r"p \lor q \equiv q \lor p")
        st.latex(r"p \land q \equiv q \land p")
        st.latex(r"p \leftrightarrow q \equiv q \leftrightarrow p")

    with st.expander("3. Associativa"):
        st.write("Podemos agrupar conectivos iguais da forma que acharmos melhor.")
        st.latex(r"(p \lor q) \lor r \equiv p \lor (q \lor r)")
        st.latex(r"(p \land q) \land r \equiv p \land (q \land r)")

with col2:
    with st.expander("4. Distributiva", expanded=True):
        st.write("Semelhante ao 'chuveirinho' da matemática.")
        st.latex(r"p \land (q \lor r) \equiv (p \land q) \lor (p \land r)")
        st.latex(r"p \lor (q \land r) \equiv (p \lor q) \land (p \lor r)")

    with st.expander("5. Absorção"):
        st.write("Uma variável 'engole' a expressão inteira se a estrutura for mista (E/OU) com repetição.")
        st.latex(r"p \lor (p \land q) \equiv p")
        st.latex(r"p \land (p \lor q) \equiv p")

    with st.expander("6. Elemento Neutro"):
        st.write("Comportamento com Tautologias (V) e Contradições (F).")
        st.latex(r"p \land V \equiv p \quad \text{(V é neutro no E)}")
        st.latex(r"p \lor F \equiv p \quad \text{(F é neutro no OU)}")

st.markdown("<br>", unsafe_allow_html=True)
st.success("➡️ **Próximo passo:** Vamos usar tudo isso para validar raciocínios no *Módulo 6: Argumentos*.")