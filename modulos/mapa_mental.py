import streamlit as st
import streamlit.components.v1 as components

st.title("🗺️ Mapa Mental Interativo (Visão de Grafos)")
st.markdown("---")

st.write("Explore a rede de conceitos de Lógica Matemática. **Clique nos temas principais (ex: Argumentos, Conectivos) para abrir ou fechar suas ramificações.**")

# Código HTML e JavaScript integrando a biblioteca Vis.js com lógica de expandir/recolher
vis_js_html = """
<!DOCTYPE html>
<html>
<head>
    <script type="text/javascript" src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>
    <style type="text/css">
        #mynetwork {
            width: 100%;
            height: 600px;
            background-color: #1e1e1e; /* Fundo escuro */
            border-radius: 12px;
            border: 1px solid #444;
        }
    </style>
</head>
<body>
<div id="mynetwork"></div>
<script type="text/javascript">
    // 1. Definindo os NÓS
    // Adicionamos a propriedade "parent" para saber quem é filho de quem, 
    // e "hidden: true" para que os subtópicos iniciem escondidos.
    var nodeArray = [
        { id: 1, label: '🧠 Lógica\\nMatemática', color: '#1f77b4', font: {color: 'white', size: 22, bold: true}, shape: 'box' },
        
        // Tópicos Principais (Sempre Visíveis)
        { id: 2, label: '📖 Fundamentos', color: '#ff7f0e', font: {color: 'white', size: 16} },
        { id: 3, label: '⚙️ Conectivos', color: '#2ca02c', font: {color: 'white', size: 16} },
        { id: 4, label: '🧮 Classificação', color: '#d62728', font: {color: 'white', size: 16} },
        { id: 5, label: '⚖️ Equivalências', color: '#9467bd', font: {color: 'white', size: 16} },
        { id: 6, label: '📝 Formas Normais', color: '#8c564b', font: {color: 'white', size: 16} },
        { id: 7, label: '🛡️ Argumentos', color: '#e377c2', font: {color: 'white', size: 16} },

        // Subtópicos: Fundamentos (Iniciam Ocultos)
        { id: 21, label: 'Proposições', color: '#333333', font: {color: '#cccccc'}, parent: 2, hidden: true },
        { id: 22, label: 'Identidade', color: '#333333', font: {color: '#cccccc'}, parent: 2, hidden: true },
        { id: 23, label: 'Não-Contradição', color: '#333333', font: {color: '#cccccc'}, parent: 2, hidden: true },
        { id: 24, label: 'Terceiro Excluído', color: '#333333', font: {color: '#cccccc'}, parent: 2, hidden: true },

        // Subtópicos: Conectivos (Iniciam Ocultos)
        { id: 31, label: 'Negação (~)', color: '#333333', font: {color: '#cccccc'}, parent: 3, hidden: true },
        { id: 32, label: 'Conjunção (∧)', color: '#333333', font: {color: '#cccccc'}, parent: 3, hidden: true },
        { id: 33, label: 'Disjunção (∨)', color: '#333333', font: {color: '#cccccc'}, parent: 3, hidden: true },
        { id: 34, label: 'Condicional (→)', color: '#333333', font: {color: '#cccccc'}, parent: 3, hidden: true },
        { id: 35, label: 'Bicondicional (↔)', color: '#333333', font: {color: '#cccccc'}, parent: 3, hidden: true },

        // Subtópicos: Classificação (Iniciam Ocultos)
        { id: 41, label: 'Tautologia', color: '#333333', font: {color: '#cccccc'}, parent: 4, hidden: true },
        { id: 42, label: 'Contradição', color: '#333333', font: {color: '#cccccc'}, parent: 4, hidden: true },
        { id: 43, label: 'Contingência', color: '#333333', font: {color: '#cccccc'}, parent: 4, hidden: true },
        
        // Subtópicos: Equivalências (Iniciam Ocultos)
        { id: 51, label: 'De Morgan', color: '#333333', font: {color: '#cccccc'}, parent: 5, hidden: true },
        { id: 52, label: 'Contrapositiva', color: '#333333', font: {color: '#cccccc'}, parent: 5, hidden: true },
        { id: 53, label: 'Nega a 1ª, Mantém 2ª', color: '#333333', font: {color: '#cccccc'}, parent: 5, hidden: true },

        // Subtópicos: Formas Normais (Iniciam Ocultos)
        { id: 61, label: 'FNC (Soma de Prod)', color: '#333333', font: {color: '#cccccc'}, parent: 6, hidden: true },
        { id: 62, label: 'FND (Prod de Somas)', color: '#333333', font: {color: '#cccccc'}, parent: 6, hidden: true },

        // Subtópicos: Argumentos (Iniciam Ocultos)
        { id: 71, label: 'Modus Ponens', color: '#333333', font: {color: '#cccccc'}, parent: 7, hidden: true },
        { id: 72, label: 'Modus Tollens', color: '#333333', font: {color: '#cccccc'}, parent: 7, hidden: true },
        { id: 73, label: 'Prova por Absurdo', color: '#333333', font: {color: '#cccccc'}, parent: 7, hidden: true }
    ];

    var nodes = new vis.DataSet(nodeArray);

    // 2. Definindo as CONEXÕES
    var edges = new vis.DataSet([
        { from: 1, to: 2 }, { from: 1, to: 3 }, { from: 1, to: 4 },
        { from: 1, to: 5 }, { from: 1, to: 6 }, { from: 1, to: 7 },

        { from: 2, to: 21 }, { from: 2, to: 22 }, { from: 2, to: 23 }, { from: 2, to: 24 },
        { from: 3, to: 31 }, { from: 3, to: 32 }, { from: 3, to: 33 }, { from: 3, to: 34 }, { from: 3, to: 35 },
        { from: 4, to: 41 }, { from: 4, to: 42 }, { from: 4, to: 43 },
        { from: 5, to: 51 }, { from: 5, to: 52 }, { from: 5, to: 53 },
        { from: 6, to: 61 }, { from: 6, to: 62 },
        { from: 7, to: 71 }, { from: 7, to: 72 }, { from: 7, to: 73 }
    ]);

    // 3. Configurações
    var container = document.getElementById('mynetwork');
    var data = { nodes: nodes, edges: edges };
    var options = {
        nodes: {
            shape: 'box', 
            borderWidth: 0,
            shadow: true,
            margin: 12
        },
        edges: {
            width: 2,
            color: '#666666',
            smooth: { type: 'continuous' }
        },
        physics: {
            stabilization: false,
            barnesHut: {
                gravitationalConstant: -2000,
                springConstant: 0.04,
                springLength: 120
            }
        },
        interaction: { hover: true }
    };
    
    var network = new vis.Network(container, data, options);

    // 4. A MÁGICA: Lógica de Expandir/Recolher ao clicar no nó
    network.on("click", function(params) {
        if (params.nodes.length > 0) {
            var clickedNodeId = params.nodes[0];
            
            // Procura todas as bolhas que são filhas do nó clicado
            var childNodes = nodes.get({
                filter: function (item) {
                    return item.parent === clickedNodeId;
                }
            });

            if (childNodes.length > 0) {
                // Pega o status atual (escondido ou visível) e inverte
                var isHidden = childNodes[0].hidden;
                var updates = [];
                
                for (var i = 0; i < childNodes.length; i++) {
                    updates.push({id: childNodes[i].id, hidden: !isHidden});
                }
                
                // Atualiza o gráfico fazendo as bolhas aparecerem ou sumirem
                nodes.update(updates);
            }
        }
    });

</script>
</body>
</html>
"""

# Renderiza o gráfico
components.html(vis_js_html, height=620)