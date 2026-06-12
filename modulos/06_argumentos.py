import streamlit as st
import pandas as pd

st.title("🛡️ Módulo 6: Argumentos e Validade")
st.markdown("---")

st.write(r"""
Um **Argumento Lógico** é uma sequência de proposições. As proposições iniciais são chamadas de **Premissas** ($P_1, P_2, \dots, P_n$), e a proposição final que derivamos delas é chamada de **Conclusão** ($Q$).
""")

st.info(r"""
💡 **Validade de um Argumento:** Um argumento é considerado **VÁLIDO** se a conclusão for uma consequência lógica das premissas. Ou seja, **toda vez que todas as premissas forem Verdadeiras, a Conclusão obrigatoriamente tem que ser Verdadeira.**
""")

st.markdown("---")
st.header("1. Provando Validade por Tabela-Verdade")
st.write(r"Para saber se o argumento $P_1, P_2 \vdash Q$ é válido:")
st.markdown(r"""
1. Construímos a tabela-verdade com as colunas das Premissas e da Conclusão.
2. Buscamos as linhas onde **todas as premissas são Verdadeiras (V)** ao mesmo tempo.
3. Se nessas linhas a conclusão também for 'V', o argumento é **Válido**. Se houver um único caso onde as premissas são 'V' e a conclusão for 'F', o argumento é **Inválido (Falácia)**.
""")

st.markdown("---")
st.header("2. Argumentos Válidos Fundamentais")
st.write("Conforme a Álgebra das Proposições, existem argumentos básicos que funcionam como **Regras de Inferência**. Eles nos permitem deduzir conclusões rapidamente sem precisar de tabelas-verdade.")

# Separando em abas para organizar os 9 argumentos do seu material
tab1, tab2, tab3, tab4 = st.tabs(["Regras Básicas", "Regras Modus", "Silogismos e Dilema", "Prova por Absurdo"])

with tab1:
    st.subheader("Regras Básicas de Construção")
    
    st.markdown("**1. Adição (Ad):** Se $P$ é verdade, $P \lor Q$ também é (podemos 'adicionar' qualquer coisa com OU).")
    st.latex(r"P \quad \vdash \quad P \lor Q \quad \text{ou} \quad Q \quad \vdash \quad P \lor Q")
    
    st.markdown("**2. Simplificação (Simp):** Se $P \land Q$ é verdade, podemos separar e afirmar cada parte isoladamente.")
    st.latex(r"P \land Q \quad \vdash \quad P \quad \text{e} \quad P \land Q \quad \vdash \quad Q")
    
    st.markdown("**3. Conjunção (Con):** Se temos duas premissas verdadeiras separadas, podemos juntá-las com 'E'.")
    st.latex(r"P, \quad Q \quad \vdash \quad P \land Q")

    st.markdown("**4. Absorção (Abs):** A condicional absorve a conjunção do antecedente com o consequente.")
    st.latex(r"P \rightarrow Q \quad \vdash \quad P \rightarrow (P \land Q)")

with tab2:
    st.subheader("Regras Modus (Modo)")
    
    st.markdown("**5. Modus Ponens (Mp):** Afirmação do antecedente.")
    st.latex(r"P \rightarrow Q, \quad P \quad \vdash \quad Q")
    st.caption("Ex: Se chover (P), a rua molha (Q). Choveu (P). Logo, a rua molhou (Q).")
    
    st.markdown("**6. Modus Tollens (Mt):** Negação do consequente.")
    st.latex(r"P \rightarrow Q, \quad \sim Q \quad \vdash \quad \sim P")
    st.caption("Ex: Se chover, a rua molha. A rua NÃO está molhada (~Q). Logo, NÃO choveu (~P).")

with tab3:
    st.subheader("Silogismos e Dilemas")
    
    st.markdown("**7. Silogismo Disjuntivo (Sd):** Se temos uma disjunção (OU) e negamos um lado, o outro sobra.")
    st.latex(r"P \lor Q, \quad \sim P \quad \vdash \quad Q \quad \text{ou} \quad P \lor Q, \quad \sim Q \quad \vdash \quad P")
    
    st.markdown("**8. Silogismo Hipotético (Sh):** Regra da cadeia transitiva.")
    st.latex(r"P \rightarrow Q, \quad Q \rightarrow R \quad \vdash \quad P \rightarrow R")

    st.markdown("**9. Dilema Construtivo (Dc):**")
    st.latex(r"(P \rightarrow Q) \land (R \rightarrow S), \quad P \lor R \quad \vdash \quad Q \lor S")

with tab4:
    st.subheader("Redução ao Absurdo (Demonstração Indireta)")
    st.write(r"""
    Neste método de demonstração, nós assumimos temporariamente que a conclusão final pretendida é **FALSA** ($\sim Q$). 
    Se, ao operar com as premissas, chegarmos a uma **Contradição Matemática** (como $P \land \sim P$), significa que a nossa suposição estava errada. Logo, se supor que $Q$ é Falso gerou um absurdo, a conclusão original $Q$ tem que ser obrigatoriamente Verdadeira!
    """)

st.markdown("<br>", unsafe_allow_html=True)
st.success("🎉 **Parabéns!** A teoria está 100% finalizada. Com esses 6 módulos, a matéria de Lógica Matemática está totalmente coberta.")