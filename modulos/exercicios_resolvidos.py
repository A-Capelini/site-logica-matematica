import streamlit as st
import pandas as pd

st.title("📚 Caderno de Exercícios Resolvidos")
st.markdown("---")

st.write("Estude os problemas resolvidos passo a passo para compreender a aplicação prática das regras lógicas.")

# Criando as 6 abas conforme solicitado
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Lista 1", "Lista 2", "Lista 3", "Lista 4", "Lista 5", "Lista 6"
])

# ==========================================
# CONTEÚDO DA LISTA 1
# ==========================================
with tab1:
    st.header("📋 Lista 1: Exercícios Iniciais de Fixação")
    st.write("Confira a resolução detalhada dos problemas lógicos da primeira lista.")
    st.markdown("---")
    
    # Exercicio 1
    st.subheader("Exercício 1: Identificação de Sentenças")
    st.markdown("""
    **Enunciado:** Quais das frases a seguir são sentenças?
    * a) A lua é feita de queijo verde.
    * b) Ele é um homem alto.
    * c) Dois é um número primo.
    * d) O jogo terminará logo?
    """)
    
    with st.expander("🔍 Ver Resolução Passo a Passo"):
        st.markdown("""
        Uma sentença (ou proposição) em lógica matemática é uma declaração afirmativa que possui um valor lógico bem definido (verdadeiro ou falso), sem ambiguidades e sem variáveis livres.
        
        * a) "A lua é feita de queijo verde" - **É uma sentença.** (É uma declaração afirmativa cujo valor lógico é Falso).
        * b) "Ele é um homem alto" - **Não é uma sentença.** (É uma sentença aberta, pois o pronome "Ele" é uma variável livre; não podemos determinar o valor lógico sem saber a quem se refere).
        * c) "Dois é um número primo" - **É uma sentença.** (É uma declaração afirmativa cujo valor lógico é Verdadeiro).
        * d) "O jogo terminará logo?" - **Não é uma sentença.** (Frases interrogativas, exclamativas ou imperativas não possuem valor lógico).
        """)
        
    st.markdown("---")

    # Exercicio 2
    st.subheader("Exercício 2: Antecedente e Consequente")
    st.markdown("""
    **Enunciado:** Indique o antecedente e o consequente de cada uma das seguintes sentenças:
    * a) O crescimento sadio das plantas é consequência de quantidade suficiente de água.
    * b) O crescimento da oferta de computadores é uma condição necessária para o desenvolvimento científico.
    """)

    with st.expander("🔍 Ver Resolução Passo a Passo"):
        st.markdown(r"""
        Na estrutura condicional "Se P, então Q" ($P \rightarrow Q$), $P$ é o antecedente (condição suficiente) e $Q$ é o consequente (condição necessária).
        
        **a) O crescimento sadio das plantas é consequência de quantidade suficiente de água.**
        * Reescrevendo na forma padrão: "Se há quantidade suficiente de água, então ocorre o crescimento sadio das plantas."
        * **Antecedente:** há quantidade suficiente de água.
        * **Consequente:** o crescimento sadio das plantas.
        
        **b) O crescimento da oferta de computadores é uma condição necessária para o desenvolvimento científico.**
        * Reescrevendo na forma padrão: "Se houver o desenvolvimento científico, então ocorreu o crescimento da oferta de computadores."
        * **Antecedente:** o desenvolvimento científico.
        * **Consequente:** o crescimento da oferta de computadores.
        """)

    st.markdown("---")

    # Exercicio 3
    st.subheader("Exercício 3: Tradução para Linguagem Simbólica")
    st.markdown("""
    **Enunciado:** Escreva a seguinte sentença na forma simbólica: "As exportações diminuem ou a inflação aumentará caso haja uma quebra de safra."
    """)

    with st.expander("🔍 Ver Resolução Passo a Passo"):
        st.markdown(r"""
        **Passo 1: Identificar as proposições simples:**
        * $P$: As exportações diminuem.
        * $Q$: A inflação aumentará.
        * $R$: Haja uma quebra de safra.
        
        **Passo 2: Analisar a estrutura da frase:**
        A frase diz: "As exportações diminuem ($P$) ou ($\lor$) a inflação aumentará ($Q$) caso (se) haja uma quebra de safra ($R$)."
        Reescrevendo na ordem natural condicional (Se... então): "Se houver uma quebra de safra, então as exportações diminuem ou a inflação aumentará."
        
        **Passo 3: Montar a expressão simbólica:**
        O antecedente é $R$, e o consequente é a proposição composta $(P \lor Q)$.
        Portanto, a representação correta é:
        """)
        st.latex(r"R \rightarrow (P \lor Q)")

    st.markdown("---")

    # Exercicio 4
    st.subheader("Exercício 4: Valores Lógicos na Condicional")
    st.markdown(r"""
    **Enunciado:** Sabendo que a proposição condicional $P \rightarrow Q$ é falsa, determine os valores lógicos de $\sim P \leftrightarrow Q$ e de $\sim P \land Q$.
    """)

    with st.expander("🔍 Ver Resolução Passo a Passo"):
        st.markdown(r"""
        **Passo 1: Descobrir os valores de $P$ e $Q$.**
        A regra de ouro da condicional ($P \rightarrow Q$) diz que ela só é **Falsa** em um único caso: quando o antecedente ($P$) é Verdadeiro e o consequente ($Q$) é Falso ("Vera Fischer").
        * Logo: $P = V$ e $Q = F$.
        
        **Passo 2: Calcular $\sim P \leftrightarrow Q$.**
        * Se $P = V$, então $\sim P = F$.
        * Substituindo: $F \leftrightarrow F$.
        * Na bicondicional, sinais iguais resultam em Verdadeiro.
        * **Resultado: $V$.**
        
        **Passo 3: Calcular $\sim P \land Q$.**
        * Já sabemos que $\sim P = F$ e $Q = F$.
        * Substituindo: $F \land F$.
        * Na conjunção, basta um Falso para tudo ser Falso.
        * **Resultado: $F$.**
        """)

    st.markdown("---")

    # Exercicio 5
    st.subheader("Exercício 5: Construção de Tabelas-Verdade")
    st.markdown(r"""
    **Enunciado:** Construir as tabelas-verdade das seguintes proposições:
    * a) $P \land (P \lor Q)$
    * b) $P \lor (P \land Q)$
    * c) $\sim(P \land Q) \leftrightarrow (\sim P \lor \sim Q)$
    """)

    with st.expander("🔍 Ver Resolução Passo a Passo"):
        st.markdown(r"**a) Tabela para $P \land (P \lor Q)$**")
        df_5a = pd.DataFrame({
            "P": ["V", "V", "F", "F"],
            "Q": ["V", "F", "V", "F"],
            "P ∨ Q": ["V", "V", "V", "F"],
            "P ∧ (P ∨ Q)": ["V", "V", "F", "F"]
        })
        st.dataframe(df_5a, hide_index=True)
        st.caption("Nota: Esta estrutura resulta no próprio $P$ (Lei da Absorção).")

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(r"**b) Tabela para $P \lor (P \land Q)$**")
        df_5b = pd.DataFrame({
            "P": ["V", "V", "F", "F"],
            "Q": ["V", "F", "V", "F"],
            "P ∧ Q": ["V", "F", "F", "F"],
            "P ∨ (P ∧ Q)": ["V", "V", "F", "F"]
        })
        st.dataframe(df_5b, hide_index=True)
        st.caption("Nota: Novamente, resulta no próprio $P$ (Lei da Absorção).")

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(r"**c) Tabela para $\sim(P \land Q) \leftrightarrow (\sim P \lor \sim Q)$**")
        df_5c = pd.DataFrame({
            "P": ["V", "V", "F", "F"],
            "Q": ["V", "F", "V", "F"],
            "P ∧ Q": ["V", "F", "F", "F"],
            "~(P ∧ Q)": ["F", "V", "V", "V"],
            "~P": ["F", "F", "V", "V"],
            "~Q": ["F", "V", "F", "V"],
            "~P ∨ ~Q": ["F", "V", "V", "V"],
            "~(P ∧ Q) ↔ (~P ∨ ~Q)": ["V", "V", "V", "V"]
        })
        st.dataframe(df_5c, hide_index=True)
        st.caption("Nota: Resulta em uma Tautologia (Demonstra a Lei de De Morgan).")

    st.markdown("---")

    # Exercicio 6
    st.subheader("Exercício 6: Tautologia, Contradição ou Contingência")
    st.markdown(r"""
    **Enunciado:** Classifique as proposições abaixo como Tautologia, Contradição ou Contingência construindo a tabela-verdade:
    * a) $(P \land Q) \land \sim(P \lor Q)$
    * b) $(P \lor \sim Q) \rightarrow (P \rightarrow \sim Q)$
    """)

    with st.expander("🔍 Ver Resolução Passo a Passo"):
        st.markdown(r"**a) Classificando $(P \land Q) \land \sim(P \lor Q)$**")
        df_6a = pd.DataFrame({
            "P": ["V", "V", "F", "F"],
            "Q": ["V", "F", "V", "F"],
            "P ∧ Q": ["V", "F", "F", "F"],
            "P ∨ Q": ["V", "V", "V", "F"],
            "~(P ∨ Q)": ["F", "F", "F", "V"],
            "(P ∧ Q) ∧ ~(P ∨ Q)": ["F", "F", "F", "F"]
        })
        st.dataframe(df_6a, hide_index=True)
        st.info("**Resultado:** Como todos os valores finais são Falsos, a proposição é uma **Contradição**.")

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(r"**b) Classificando $(P \lor \sim Q) \rightarrow (P \rightarrow \sim Q)$**")
        df_6b = pd.DataFrame({
            "P": ["V", "V", "F", "F"],
            "Q": ["V", "F", "V", "F"],
            "~Q": ["F", "V", "F", "V"],
            "A = P ∨ ~Q": ["V", "V", "F", "V"],
            "B = P → ~Q": ["F", "V", "V", "V"],
            "A → B": ["F", "V", "V", "V"]
        })
        st.dataframe(df_6b, hide_index=True)
        st.info("**Resultado:** Como os valores finais variam entre Verdadeiro e Falso, a proposição é uma **Contingência**.")

    st.markdown("---")

    # Exercicio 7
    st.subheader("Exercício 7: Operadores NAND e NOR")
    st.markdown(r"""
    **Enunciado:** Sabendo que as proposições $P$ e $Q$ são verdadeiras ($P=V, Q=V$) e que as proposições $R$ e $S$ são falsas ($R=F, S=F$), determine o valor lógico das seguintes proposições:
    *(Nota: O símbolo $\uparrow$ representa o operador NAND, e $\downarrow$ representa o operador NOR).*
    
    * a) $(\sim P \downarrow Q) \land (Q \uparrow \sim R)$
    * b) $((P \uparrow Q) \lor (Q \downarrow R)) \uparrow (R \downarrow P)$
    * c) $(\sim P \uparrow \sim Q) \leftrightarrow ((Q \downarrow R) \downarrow P)$
    """)

    with st.expander("🔍 Ver Resolução Passo a Passo"):
        st.markdown(r"""
        **Lembrete das Regras:**
        * **NAND ($\uparrow$):** A Negação do 'E'. Só é Falso se ambos forem $V$.
        * **NOR ($\downarrow$):** A Negação do 'OU'. Só é Verdadeiro se ambos forem $F$.
        """)
        
        st.markdown(r"""
        **a) Resolvendo: $(\sim P \downarrow Q) \land (Q \uparrow \sim R)$**
        * $\sim P = F$
        * $(\sim P \downarrow Q) = (F \downarrow V) = F$ (Pois no NOR basta um V para ser falso)
        * Como é uma conjunção ($\land$) e o lado esquerdo deu $F$, o resultado final inteiro é $F$.
        * **Resultado Final: Falso (F).**
        """)

        st.markdown(r"""
        **b) Resolvendo: $((P \uparrow Q) \lor (Q \downarrow R)) \uparrow (R \downarrow P)$**
        * $P \uparrow Q = V \uparrow V = F$
        * $Q \downarrow R = V \downarrow F = F$
        * Lado Esquerdo: $F \lor F = F$
        * Lado Direito: $R \downarrow P = F \downarrow V = F$
        * Expressão Final: $F \uparrow F$. No NAND, a única forma de dar falso é se ambos forem V. Logo, $F \uparrow F = V$.
        * **Resultado Final: Verdadeiro (V).**
        """)

        st.markdown(r"""
        **c) Resolvendo: $(\sim P \uparrow \sim Q) \leftrightarrow ((Q \downarrow R) \downarrow P)$**
        * $\sim P = F$ e $\sim Q = F$
        * Lado Esquerdo: $F \uparrow F = V$ (NAND de falsos é V)
        * $Q \downarrow R = V \downarrow F = F$
        * Lado Direito: $(F) \downarrow P = F \downarrow V = F$
        * Expressão Final: $V \leftrightarrow F$. Na bicondicional, sinais diferentes geram falso.
        * **Resultado Final: Falso (F).**
        """)

    st.markdown("---")

    # Exercício 8
    st.subheader("Exercício 8: Tautologias, Contradições e Contingências com NAND/NOR")
    st.markdown(r"""
    **Enunciado:** Quais das seguintes fórmulas são tautologias, contradições e contingências?
    
    * a) $(P \downarrow Q) \lor (\sim Q \uparrow P)$
    * b) $(P \uparrow (Q \lor R)) \rightarrow \sim R$
    * c) $((P \downarrow \sim P) \lor Q) \downarrow (\sim Q \land \sim R)$
    """)

    with st.expander("🔍 Ver Resolução Passo a Passo"):
        st.markdown(r"""
        **Valores dos Operadores:**
        * **$\uparrow$ (Traço de Sheffer / NAND):** Equivalente a $\sim(X \land Y)$. Só é Falso quando ambos são Verdadeiros.
        * **$\downarrow$ (Seta de Peirce / NOR):** Equivalente a $\sim(X \lor Y)$. Só é Verdadeiro quando ambos são Falsos.
        
        ---
        
        **a) Resolvendo: $(P \downarrow Q) \lor (\sim Q \uparrow P)$**
        * Analisando a combinação P=V e Q=V:
          * $P \downarrow Q = V \downarrow V = F$
          * $\sim Q = F$, logo $\sim Q \uparrow P = F \uparrow V = V$
          * Resultado: $F \lor V = V$
        * Analisando a combinação P=F e Q=F:
          * $P \downarrow Q = F \downarrow F = V$
          * $\sim Q = V$, logo $\sim Q \uparrow P = V \uparrow F = V$
          * Resultado: $V \lor V = V$
        * *Conclusão:* Como para qualquer caso o conectivo "OU" vai encontrar ao menos um "V", a expressão será sempre Verdadeira. Trata-se de uma **Tautologia**.
        
        ---
        
        **b) Resolvendo: $(P \uparrow (Q \lor R)) \rightarrow \sim R$**
        * Teste 1: Se R = F, então $\sim R = V$. A condicional termina em Verdadeiro.
        * Teste 2: Se R = V e P = F. 
          * $Q \lor R$ é V. 
          * $P \uparrow (Q \lor R) \Rightarrow F \uparrow V = V$. 
          * A condicional fica $V \rightarrow F$, resultando em Falso.
        * *Conclusão:* Como encontramos um caso "V" e um caso "F", trata-se de uma **Contingência**.
        
        ---
        
        **c) Resolvendo: $((P \downarrow \sim P) \lor Q) \downarrow (\sim Q \land \sim R)$**
        * Simplificando $(P \downarrow \sim P)$: NOR é a negação do OU. $P \lor \sim P$ é Tautologia (V). A negação disso é Contradição (F). Logo, $(P \downarrow \sim P) = F$.
        * Substituindo na esquerda: $(F \lor Q) = Q$.
        * A expressão se torna: $Q \downarrow (\sim Q \land \sim R)$.
        * Aplicando equivalências, equivale a: $\sim(Q \lor (\sim Q \land \sim R))$.
        * Pela Distributiva e Absorção, $Q \lor (\sim Q \land \sim R) \equiv Q \lor \sim R$.
        * Negando isso (De Morgan): $\sim Q \land R$.
        * Como $\sim Q \land R$ varia conforme os valores lógicos de Q e R, trata-se de uma **Contingência**.
        """)

# ==========================================
# CONTEÚDO DA LISTA 2
# ==========================================
with tab2:
    st.header("📋 Lista 2: Formas Normais e Argumentos Lógicos")
    st.write("Confira a resolução detalhada dos problemas algébricos e deduções lógicas da segunda lista.")
    st.markdown("---")

    # Exercicio 1
    st.subheader("Exercício 1: FNC (Forma Normal Conjuntiva)")
    st.markdown(r"**Enunciado:** Determine a FNC da proposição: $\sim(((P \lor Q) \land \sim Q) \lor (Q \land R))$")
    
    with st.expander("🔍 Ver Resolução Passo a Passo"):
        st.markdown(r"""
        Para encontrar a FNC, devemos simplificar a expressão utilizando as leis da álgebra proposicional (Leis de De Morgan, Distributiva, etc.) até obtermos uma **conjunção de disjunções**.
        
        1. **Expressão original:** $\sim(((P \lor Q) \land \sim Q) \lor (Q \land R))$
        2. Vamos simplificar a parte interna primeiro: $(P \lor Q) \land \sim Q$.
           Aplicando a lei distributiva: $(P \land \sim Q) \lor (Q \land \sim Q)$
        3. Sabemos que $(Q \land \sim Q)$ é uma contradição (Falso).
           Logo: $(P \land \sim Q) \lor F \equiv P \land \sim Q$
        4. Substituindo de volta na expressão principal:
           $\sim((P \land \sim Q) \lor (Q \land R))$
        5. Agora aplicamos a Lei de De Morgan no operador de negação externo:
           $\sim(P \land \sim Q) \land \sim(Q \land R)$
        6. Aplicamos De Morgan novamente em cada termo isolado:
           $(\sim P \lor \sim(\sim Q)) \land (\sim Q \lor \sim R)$
        7. Eliminando a dupla negação:
           $(\sim P \lor Q) \land (\sim Q \lor \sim R)$
        
        **Resultado (FNC):** $(\sim P \lor Q) \land (\sim Q \lor \sim R)$
        *(A expressão é composta por conjunções de disjunções, cumprindo a regra da FNC).*
        """)

    st.markdown("---")

    # Exercicio 2
    st.subheader("Exercício 2: FND (Forma Normal Disjuntiva)")
    st.markdown(r"**Enunciado:** Determine a FND da proposição: $\sim(((P \lor Q) \land \sim Q) \lor (Q \land R))$")
    
    with st.expander("🔍 Ver Resolução Passo a Passo"):
        st.markdown(r"""
        A FND é uma **disjunção de conjunções**. Podemos partir do resultado já simplificado do Exercício 1:
        
        1. **Expressão do Ex. 1:** $(\sim P \lor Q) \land (\sim Q \lor \sim R)$
        2. Para transformar em FND, aplicamos a propriedade distributiva ('chuveirinho'):
           $(\sim P \land (\sim Q \lor \sim R)) \lor (Q \land (\sim Q \lor \sim R))$
        3. Distribuindo novamente (multiplicando os termos):
           $(\sim P \land \sim Q) \lor (\sim P \land \sim R) \lor (Q \land \sim Q) \lor (Q \land \sim R)$
        4. O termo $(Q \land \sim Q)$ é uma contradição (Falso), então podemos removê-lo da disjunção.
           $(\sim P \land \sim Q) \lor (\sim P \land \sim R) \lor F \lor (Q \land \sim R)$
        
        **Resultado (FND):** $(\sim P \land \sim Q) \lor (\sim P \land \sim R) \lor (Q \land \sim R)$
        """)

    st.markdown("---")

    # Exercicio 3
    st.subheader("Exercício 3: Determinar a Fórmula via Tabela-Verdade")
    st.markdown(r"**Enunciado:** Determine a fórmula $\alpha$ correspondente à seguinte tabela-verdade:")
    
    df_ex3 = pd.DataFrame({"P": [1, 1, 0, 0], "Q": [1, 0, 1, 0], "α": [0, 1, 1, 0]})
    st.dataframe(df_ex3, hide_index=True)
    
    with st.expander("🔍 Ver Resolução Passo a Passo"):
        st.markdown(r"""
        Pela tabela-verdade, a proposição $\alpha$ é Verdadeira (1) apenas quando P e Q têm valores lógicos diferentes. Trata-se da porta lógica XOR (Ou Exclusivo), $\alpha = P \oplus Q$.
        
        Podemos extrair a fórmula algébrica pelas linhas verdadeiras (FND) ou falsas (FNC):
        
        * **Pela FND (soma de mintermos):** Olhamos para as linhas onde $\alpha = 1$.
            * Linha 2 (P=1, Q=0): $P \land \sim Q$
            * Linha 3 (P=0, Q=1): $\sim P \land Q$
            * Logo: $\alpha = (P \land \sim Q) \lor (\sim P \land Q)$
            
        * **Pela FNC (produto de maxtermos):** Olhamos para as linhas onde $\alpha = 0$.
            * Linha 1 (P=1, Q=1): negamos para obter a soma, fica $(\sim P \lor \sim Q)$
            * Linha 4 (P=0, Q=0): negamos para obter a soma, fica $(P \lor Q)$
            * Logo: $\alpha = (\sim P \lor \sim Q) \land (P \lor Q)$
        
        **Resultado (FNC):** $\alpha = (\sim P \lor \sim Q) \land (P \lor Q)$
        """)

    st.markdown("---")

    # Exercicio 4
    st.subheader("Exercício 4: Demonstração Pelo Absurdo")
    st.markdown(r"**Enunciado:** Demonstrar pelo método do absurdo a Lei da adição: $P \Rightarrow (P \lor Q)$")
    
    with st.expander("🔍 Ver Resolução Passo a Passo"):
        st.markdown(r"""
        O método de prova por absurdo consiste em assumir que a premissa é verdadeira e que a conclusão é falsa, e então chegar a uma contradição.
        
        1. **Hipótese para o absurdo:** Assumimos que a condicional $P \rightarrow (P \lor Q)$ é **Falsa**.
        2. Uma condicional só é falsa se o antecedente for Verdadeiro e o consequente for Falso. Portanto, assumimos:
            * $P$ é Verdadeiro (V).
            * $(P \lor Q)$ é Falso (F).
        3. Analisando $(P \lor Q)$ = Falso:
            * Uma disjunção só é falsa se **ambas** as proposições forem falsas.
            * Logo, $P$ deve ser Falso e $Q$ deve ser Falso.
        4. **Contradição:** No passo 2, assumimos que $P$ é Verdadeiro. No passo 3, deduzimos que $P$ tem que ser Falso. É impossível que $P$ seja Verdadeiro e Falso simultaneamente ($P \land \sim P \equiv F$).
        5. **Conclusão:** Como a suposição de que a lei é falsa nos levou a um absurdo lógico, a proposição original $P \Rightarrow (P \lor Q)$ é necessariamente Verdadeira.
        """)

    st.markdown("---")

    # Exercicio 5
    st.subheader("Exercício 5: Prova por Álgebra de Proposições")
    st.markdown(r"**Enunciado:** Use a álgebra de proposições e prove por equivalências que $(A \lor B) \land (A \lor \sim B)$ equivale a $A$.")
    
    with st.expander("🔍 Ver Resolução Passo a Passo"):
        st.markdown(r"""
        Partimos da expressão: $(A \lor B) \land (A \lor \sim B)$
        
        1. Podemos aplicar a **Lei Distributiva** (no sentido inverso, fatorando o termo comum $A \lor$):
           $$A \lor (B \land \sim B)$$
        2. Aplicamos a **Lei da Contradição (ou Complementaridade)**. Sabemos que uma proposição não pode ser verdadeira e falsa ao mesmo tempo, logo $(B \land \sim B)$ é Falso ($F$).
           $$A \lor F$$
        3. Aplicamos a **Lei da Identidade**. Qualquer proposição ligada pelo conectivo "OU" a um valor Falso resulta na própria proposição.
           $$A$$
           
        **Conclusão:** $(A \lor B) \land (A \lor \sim B) \equiv A$ (C.Q.D.)
        """)

    st.markdown("---")

    # Exercicio 6
    st.subheader("Exercício 6: Prova de Validade (Regras de Inferência)")
    st.markdown(r"**Enunciado:** Usando lógica proposicional, prove o seguinte argumento: $A, \quad B \rightarrow C, \quad [(A \land B) \rightarrow (D \lor \sim C)], \quad B \quad \vdash \quad D$")
    
    with st.expander("🔍 Ver Resolução Passo a Passo"):
        st.markdown(r"""
        Vamos listar as premissas e deduzir a conclusão $D$ passo a passo usando regras de inferência:
        
        1. $A$ $\quad$ *(Premissa)*
        2. $B \rightarrow C$ $\quad$ *(Premissa)*
        3. $(A \land B) \rightarrow (D \lor \sim C)$ $\quad$ *(Premissa)*
        4. $B$ $\quad$ *(Premissa)*
        ---
        5. $A \land B$ $\quad$ *(Regra da Conjunção entre 1 e 4)*
        6. $D \lor \sim C$ $\quad$ *(Modus Ponens entre 3 e 5. Se o antecedente é V, o consequente é V)*
        7. $C$ $\quad$ *(Modus Ponens entre 2 e 4)*
        8. $\sim(\sim C)$ $\quad$ *(Dupla Negação do passo 7)*
        9. $D$ $\quad$ *(Silogismo Disjuntivo entre 6 e 8. Temos $D \lor \sim C$. Como sabemos que $\sim C$ é falso, $D$ tem que ser verdadeiro).*
        
        **Conclusão:** O argumento foi provado como válido. $\vdash D$.
        """)

    st.markdown("---")

    # Exercicio 7
    st.subheader("Exercício 7: O Mistério de Percule Hoirot (Puzzle Lógico)")
    st.markdown(r"""
    **Enunciado:** O famoso detetive Percule Hoirot foi chamado para resolver o assassinato de Lord Charles. Deduza quem é o assassino com base nestas premissas:
    * a) Lord Charles foi morto com uma pancada de castiçal.
    * b) Ou Lady Camila ou a empregada Sara estavam na sala de jantar no momento do crime.
    * c) Se o cozinheiro estava na cozinha, então o açougueiro o matou com uma dose letal de arsênico.
    * d) Se Lady Camila estivesse na sala de jantar, então o motorista matou Lord Charles.
    * e) Se o cozinheiro não estava na cozinha, então Sara não estava na sala de jantar.
    * f) Se Sara estava na sala de jantar, o ajudante pessoal o matou.
    """)
    
    with st.expander("🔍 Ver Resolução Passo a Passo"):
        st.markdown(r"""
        **Variáveis:**
        * $LC$: Lady Camila na sala
        * $S$: Sara na sala
        * $C$: Cozinheiro na cozinha
        * $A$: Açougueiro matou com arsênico
        * $M$: Motorista matou
        
        **Premissas Formalizadas:**
        * a) Ocorreu pancada, não veneno $\Rightarrow \sim A$
        * b) $LC \lor S$
        * c) $C \rightarrow A$
        * d) $LC \rightarrow M$
        * e) $\sim C \rightarrow \sim S$
        
        **Dedução (Passo a Passo):**
        1. Pela premissa (a), Lord Charles não foi envenenado. Logo, **$\sim A$ é Verdadeiro.**
        2. Olhando para a premissa (c) "$C \rightarrow A$". Pela regra do *Modus Tollens*, se $\sim A$ é verdade, então o antecedente também deve ser negado. Logo, **$\sim C$ é Verdadeiro** (O cozinheiro não estava na cozinha).
        3. Olhando para a premissa (e) "$\sim C \rightarrow \sim S$". Como sabemos que $\sim C$ é verdade (passo 2), aplicamos o *Modus Ponens*, resultando que **$\sim S$ é Verdadeiro** (Sara não estava na sala de jantar).
        4. Olhando para a premissa (b) "$LC \lor S$". Como sabemos que Sara não estava na sala ($\sim S$), aplicamos o *Silogismo Disjuntivo*. Logo, **$LC$ é Verdadeiro** (Lady Camila estava na sala).
        5. Olhando para a premissa (d) "$LC \rightarrow M$". Como Lady Camila estava na sala ($LC$ é verdade pelo passo 4), aplicamos o *Modus Ponens*.
        
        **Resposta Final:** Sim, é possível deduzir quem o matou. A dedução termina afirmando que **$M$ é verdadeiro**, logo, o assassino é o **motorista**.
        """)

# ABAS SECUNDÁRIAS (Placeholders)
with tab3:
    st.header("📋 Lista 3")
    st.info("Espaço reservado para a resolução dos exercícios da Lista 3 da ementa.")

with tab4:
    st.header("📋 Lista 4")
    st.info("Espaço reservado para a resolução dos exercícios da Lista 4 da ementa.")

with tab5:
    st.header("📋 Lista 5")
    st.info("Espaço reservado para a resolução dos exercícios da Lista 5 da ementa.")

with tab6:
    st.header("📋 Lista 6")
    st.info("Espaço reservado para a resolução dos exercícios da Lista 6 da ementa.")