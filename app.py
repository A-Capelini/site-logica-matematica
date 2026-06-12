import streamlit as st

# Configuração global da página
st.set_page_config(
    page_title="Lógica Matemática | FATEC",
    page_icon="🧠",
    layout="wide"
)

# Definição das Páginas
home = st.Page("modulos/00_home.py", title="Página Inicial", icon="🏠", default=True)

# Roteiro de Aulas
mod1 = st.Page("modulos/01_fundamentos.py", title="Módulo 1: Fundamentos", icon="📖")
mod2 = st.Page("modulos/02_conectivos.py", title="Módulo 2: Conectivos e Tabelas", icon="🔗")
mod3 = st.Page("modulos/03_equivalencias.py", title="Módulo 3: Equivalências Lógicas", icon="⚖️")
mod4 = st.Page("modulos/04_formas_normais.py", title="Módulo 4: Formas Normais", icon="🧮")
mod5 = st.Page("modulos/05_propriedades.py", title="Módulo 5: Propriedades", icon="📏")
mod6 = st.Page("modulos/06_argumentos.py", title="Módulo 6: Argumentos", icon="🛡️")

# Prática e Revisão
ex_resolvidos = st.Page("modulos/exercicios_resolvidos.py", title="Exercícios Resolvidos", icon="📚")
atv1 = st.Page("modulos/atv1.py", title="Atividade 1", icon="📝")
atv2 = st.Page("modulos/atv2.py", title="Atividade 2", icon="✍️")
mapa = st.Page("modulos/mapa_mental.py", title="Mapa Mental Interativo", icon="🗺️")

# Agrupamento no Menu Lateral
paginas = {
    "Apresentação": [home],
    "Roteiro de Aprendizagem": [mod1, mod2, mod3, mod4, mod5, mod6],
    "Prática & Revisão": [ex_resolvidos, atv1, atv2, mapa]
}

# Inicializa a navegação
pg = st.navigation(paginas)

# Executa a página selecionada
pg.run()