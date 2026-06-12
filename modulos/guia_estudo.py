import streamlit as st
import pandas as pd

# Define a largura máxima para simular a tela do NotebookLM
st.markdown("""
<style>
    /* Estilização para simular cards e a interface do NotebookLM */
    .card-header { font-weight: 600; font-size: 1.1em; margin-bottom: 10px; }
    .notebook-title { font-size: 1.5em; font-weight: bold; padding-bottom: 15px;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="notebook-title">Guia de Estudo: Lógica Matemática (Visão NotebookLM)</div>', unsafe_allow_html=True)
st.markdown("---")

# Layout Principal dividido em duas colunas assimétricas (Esquerda: Resumo, Direita: Chat/FAQ)
col_esq, col_dir = st.columns([2, 1.2], gap="large")

# COLUNA ESQUERDA: O "Resumo do Guia de Estudo" (Painel Central do NotebookLM)
with col_esq:
    st.subheader("Resumo do Guia de Estudo")
    
    # Simulando o player de áudio (Visão Geral em Áudio)
    st.info("▶️ **Visão Geral em Áudio** (Recurso simulado - Em breve!)")
    
    st.write("""
    Este guia explora os fundamentos da Lógica Matemática, partindo de proposições simples e conectivos básicos, avançando para a construção e análise de tabelas-verdade, e culminando no estudo da operação **Bicondicional ($\leftrightarrow$)** e regras de inferência.
    """)
    
    # Expanders imitando os tópicos do resumo do NotebookLM
    with st.expander("📝 1. Proposições e Princípios Fundamentais", expanded=True):
        st.write("**Proposição:** Sentença declarativa com valor V (Verdadeiro) ou F (Falso).")
        st.write("**Princípios:**")
        st.markdown("- **Identidade:** Uma proposição é igual a ela mesma ($P = P$).")
        st.markdown("- **Não-Contradição:** Impossível ser V e F simultaneamente.")
        st.markdown("- **Terceiro Excluído:** Toda proposição é V ou F, não há terceira opção.")

    with st.expander("🔗 2. Conectivos Lógicos e Tabelas-Verdade"):
        st.write("A união de proposições simples forma proposições compostas. O valor final depende do conectivo:")
        st.markdown("- **$\sim$ (Negação):** Inverte o valor.")
        st.markdown("- **$\land$ (Conjunção - E):** Só é V se todas forem V.")
        st.markdown("- **$\vee$ (Disjunção Inclusiva - OU):** Só é F se todas forem F.")
        st.markdown("- **$\\rightarrow$ (Condicional - Se... então):** Falsa apenas quando V $\\rightarrow$ F.")
        
    with st.expander("🎯 3. Foco na Operação Bicondicional ($\\leftrightarrow$)"):
        st.write("A **Bicondicional** ('se, e somente se') indica equivalência estrita entre as partes.")
        st.success("**Regra Própria:** $p \\leftrightarrow q$ é Verdadeira (V) apenas quando $p$ e $q$ possuem valores lógicos **IGUAIS** (ambos V ou ambos F).")
        
        # Tabela demonstrativa
        df_bi = pd.DataFrame({"p": ["V", "V", "F", "F"], "q": ["V", "F", "V", "F"], "p ↔ q": ["V", "F", "F", "V"]})
        st.dataframe(df_bi, hide_index=True, use_container_width=True)

    with st.expander("🧮 4. Tautologia, Contradição e Equivalência"):
        st.write("- **Tautologia:** Tabela-verdade resulta apenas em V.")
        st.write("- **Contradição:** Tabela-verdade resulta apenas em F.")
        st.write("- **Equivalência Lógica:** Duas fórmulas possuem tabelas-verdade idênticas (ex: $p \\rightarrow q \\equiv \sim p \vee q$).")


# COLUNA DIREITA: Área de Interação (Simulando o Bate-papo do NotebookLM)
with col_dir:
    st.subheader("Bate-papo e Dicas Rápidas")
    
    # Caixa simulando o chat
    with st.container(border=True):
        st.markdown("<div class='card-header'>Dicas Geradas (FAQ)</div>", unsafe_allow_html=True)
        
        # Simulando uma conversa/pergunta sugerida
        st.chat_message("user").write("Como calcular o número de linhas de uma tabela-verdade?")
        st.chat_message("assistant").write("Utilize a fórmula **$2^n$**, onde *n* é o número de proposições simples distintas. Por exemplo, para as variáveis *p* e *q*, teremos $2^2 = 4$ linhas.")
        
        st.chat_message("user").write("O que são Conectivos de Scheffer?")
        st.chat_message("assistant").write("São conectivos (NAND e NOR) que, isoladamente, conseguem substituir todas as outras operações lógicas. São amplamente usados em circuitos digitais.")

    # Simulando a caixa de digitação inferior
    st.markdown("<br>", unsafe_allow_html=True)
    st.text_input("Faça uma pergunta sobre o material...", placeholder="Ex: O que é Modus Ponens?")
    st.caption("Aviso: Esta é uma simulação visual da interface do NotebookLM.")