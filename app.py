
import streamlit as st
import pandas as pd

# Estilo do app
st.set_page_config(page_title="🎤 Consulta de Músicas", layout="centered")

# CSS personalizado para visual karaokê
st.markdown("""
    <style>
    .title {
        text-align: center;
        font-size: 50px;
        color: #f72585;
        font-weight: bold;
        margin-bottom: 20px;
        text-shadow: 2px 2px #560bad;
    }
    .song-card {
        background-color: #3a0ca3;
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 10px;
        color: white;
        font-size: 20px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🎶 Busca de Músicas Karaokê 🎶</div>', unsafe_allow_html=True)

# Carregar os dados da planilha
@st.cache_data
def carregar_dados():
    return pd.read_excel("musicas.xlsx")

# Carrega a planilha
try:
    df = carregar_dados()
except Exception as e:
    st.error(f"Erro ao carregar a planilha: {e}")
    st.stop()

# Entradas de busca
col1, col2 = st.columns(2)
with col1:
    cantor_input = st.text_input("Buscar por Cantor")
with col2:
    musica_input = st.text_input("Buscar por Nome da Música")


# Filtragem
filtro = df
if cantor_input:
    filtro = filtro[filtro["cantos"].str.contains(cantor_input, case=False, na=False)]
if musica_input:
    filtro = filtro[filtro["nome da musica"].str.contains(musica_input, case=False, na=False)]

# Exibir resultados
if not filtro.empty:
    for _, row in filtro.iterrows():
        st.markdown(f"""
            <div class=\"song-card\">
                <strong>🎤 Cantor:</strong> {row['cantos']}<br>
                <strong>🎵 Música:</strong> {row['nome da musica']}<br>
                <strong>🔢 Código:</strong> {row['codigo_musica']}
            </div>
        """, unsafe_allow_html=True)
else:
    st.warning("Nenhum resultado encontrado. Tente outro nome ou cantor.")
