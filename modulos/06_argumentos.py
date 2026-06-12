import streamlit as st
import pandas as pd

st.title("🛡️ Módulo 6: Argumentos e Validade")
st.markdown("---")

st.write("""
Um **Argumento Lógico** é uma sequência de proposições. As proposições iniciais são chamadas de **Premissas** ($P_1, P_2, \dots, P_n$), e a proposição final que derivamos delas é chamada de **Conclusão** ($Q$).
""")

st.info("""
💡 **Validade de um Argumento:** Um argumento é considerado **VÁLIDO** se a conclusão for uma consequência lógica das premissas. Ou seja, **toda vez que todas as premissas forem Verdadeiras, a Conclusão obrigatoriamente tem que ser Verdadeira.**
""")

st.markdown("---")
st.header("1. Provando Validade por Tabela-Verdade")
st.write("Para saber se o argumento $P_1, P_2 \vdash Q$ é válido:")
st.markdown("""
1. Construímos a tabela-verdade com as colunas das Premissas e da Conclusão.
2. Buscamos as linhas onde **todas as premissas são Verdadeiras (V)** ao mesmo tempo.
3. Se nessas linhas a conclusão também for 'V', o argumento é **Válido**. Se houver um único caso onde as premissas são 'V' e a conclusão for 'F', o argumento é **Inválido (Falácia)**.
""")

st.markdown("---")
st.header("2. Regras de Inferência (Dedução)")
st.write("Na prática, usamos estruturas famosas e já provadas para deduzir conclusões rapidamente sem precisar fazer tabelas.")

tab1, tab2, tab3, tab4 = st.tabs(["Modus Ponens", "Modus Tollens", "Silogismos", "Prova por Absurdo"])

with tab1:
    st.subheader("Modus Ponens (Afirmação do Antecedente)")
    st.write("Se temos uma condicional e afirmamos a primeira parte, deduzimos a segunda.")
    st.latex(r"p \rightarrow q, \quad p \quad \vdash \quad q")
    st.caption("Ex: Se chover, a rua molha. Choveu. Logo, a rua molhou.")

with tab2:
    st.subheader("Modus Tollens (Negação do Consequente)")
    st.write("Se temos uma condicional e negamos a segunda parte, deduzimos a negação da primeira.")
    st.latex(r"p \rightarrow q, \quad \sim q \quad \vdash \quad \sim p")
    st.caption("Ex: Se chover, a rua molha. A rua NÃO está molhada. Logo, NÃO choveu.")

with tab3:
    st.subheader("Silogismo Hipotético e Disjuntivo")
    st.write("**Silogismo Hipotético (Regra da Cadeia):**")
    st.latex(r"p \rightarrow q, \quad q \rightarrow r \quad \vdash \quad p \rightarrow r")
    
    st.write("**Silogismo Disjuntivo:**")
    st.latex(r"p \lor q, \quad \sim p \quad \vdash \quad q")

with tab4:
    st.subheader("Redução ao Absurdo (Demonstração Indireta)")
    st.write("""
    Neste método, nós assumimos temporariamente que a conclusão é **FALSA** ($\sim Q$). 
    Se, ao calcularmos, chegarmos a uma **Contradição** (algo como $A \land \sim A$), significa que a nossa suposição estava errada. Logo, se supor que é Falso deu erro, a conclusão original $Q$ tem que ser obrigatoriamente verdadeira!
    """)

st.markdown("<br>", unsafe_allow_html=True)
st.success("🎉 **Parabéns!** A teoria está 100% finalizada. Com esses 6 módulos, a matéria de Lógica Matemática está totalmente coberta.")