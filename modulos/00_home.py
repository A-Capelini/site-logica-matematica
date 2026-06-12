import streamlit as st

st.title("🧠 Lógica Matemática")
st.markdown("---")

# Container para os dados da matéria e do autor
with st.container():
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("Sobre o Portal")
        st.write("""
        Bem-vindo(a) ao portal interativo de Lógica Matemática!  
        Este ambiente foi projetado para facilitar o estudo da disciplina, oferecendo o conteúdo 
        estruturado em uma ordem lógica: desde os princípios fundamentais até o método dedutivo.
        """)
    
    with col2:
        st.info("""
        **Autor:** Anderson Capelini Andrade  
        **Curso:** Ciência de Dados (4º Semestre)  
        **Instituição:** FATEC Cotia
        """)

st.markdown("### 📌 Como utilizar este site")
st.write("""
Recomendamos que você utilize o menu lateral para navegar. Siga esta ordem para um melhor aproveitamento:
1. **Roteiro de Aprendizagem:** Estude os módulos sequencialmente, pois a Lógica é cumulativa.
2. **Atividades:** Teste seus conhecimentos resolvendo as questões de fixação.
3. **Mapa Mental:** Utilize como ferramenta de revisão rápida antes de provas.
""")

st.success("⬅️ Utilize o menu à esquerda para iniciar seus estudos!")