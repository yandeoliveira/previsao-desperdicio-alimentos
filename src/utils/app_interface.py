import streamlit as st
import pandas as pd
import joblib
import os
import io

# Configuração da página do Streamlit
st.set_page_config(
    page_title="Previsão de Desperdício de Alimentos",
    layout="wide",
    page_icon="🍎"
)
# Estilo customizado para modernizar a interface
st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(120deg, #f8fafc 0%, #e0e7ef 100%);
    }
    .stButton>button {
        background-color: #4F8EF7;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.5em 2em;
        margin-top: 1em;
        transition: 0.2s;
    }
    .stButton>button:hover {
        background-color: #2563eb;
        color: #fff;
    }
    .stNumberInput>div>input {
        border-radius: 6px;
        border: 1px solid #4F8EF7;
    }
    .stSelectbox>div>div {
        border-radius: 6px;
        border: 1px solid #4F8EF7;
    }
    .st-cb {
        font-size: 1.1em;
    }
    .stMetric {
        background: #f1f5f9;
        border-radius: 8px;
        padding: 1em;
        margin-bottom: 1em;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título e descrição da aplicação
st.title("🍎 Previsão de Desperdício de Alimentos")
st.markdown(
    """
    <span style='font-size:1.2em;'>Preencha os dados abaixo para prever a sobra de alimentos e tomar decisões mais inteligentes para o seu negócio.</span>
    """,
    unsafe_allow_html=True
)

# Carregar o modelo treinado salvo pelo main.py
try:
    modelo = joblib.load('modelo_sobra.pkl')
except FileNotFoundError:
    st.error("Modelo não encontrado. Treine o modelo primeiro executando o main.py.")
    st.stop()

# Caminho absoluto para a pasta de imagens
IMAGENS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../imagens'))

# Caminho para o arquivo de histórico
HISTORICO_CSV = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../historico_previsoes.csv'))

# Função para carregar histórico do CSV
@st.cache_data(show_spinner=False)
def carregar_historico():
    if os.path.exists(HISTORICO_CSV):
        try:
            return pd.read_csv(HISTORICO_CSV).to_dict('records')
        except Exception:
            return []
    return []

# Função para salvar histórico no CSV
def salvar_historico(lista):
    df = pd.DataFrame(lista)
    df.to_csv(HISTORICO_CSV, index=False)

# Inicializa histórico de previsões
if 'historico_previsoes' not in st.session_state:
    st.session_state['historico_previsoes'] = carregar_historico()

# Layout responsivo com três colunas
col1, col2, col3 = st.columns([1, 1, 1], gap="large")

categorias = [
    "Fruta",
    "Legume",
    "Verdura",
    "Carne",
    "Bebida",
    "Laticínio",
    "Pão",
    "Doce",
    "Grão",
    "Outro"
]

# Imagens correspondentes a cada categoria (ajuste os nomes conforme os arquivos reais)
categoria_imagens = {
    "Fruta": os.path.join(IMAGENS_DIR, "frutas.jpg"),
    "Legume": os.path.join(IMAGENS_DIR, "legumes.jpg"),
    "Verdura": os.path.join(IMAGENS_DIR, "verdura.jpg"),
    "Carne": os.path.join(IMAGENS_DIR, "carne.jpg"),
    "Bebida": os.path.join(IMAGENS_DIR, "bebida.jpg"),
    "Laticínio": os.path.join(IMAGENS_DIR, "Laticínio.jpg"),
    "Pão": os.path.join(IMAGENS_DIR, "pao.jpg"),
    "Doce": os.path.join(IMAGENS_DIR, "doce.jpg"),
    "Grão": os.path.join(IMAGENS_DIR, "grao.jpg"),
    "Outro": os.path.join(IMAGENS_DIR, "outros.jpg")
}

# Função para limpar campos
if 'reset' not in st.session_state:
    st.session_state['reset'] = False

def limpar_campos():
    st.session_state['reset'] = True
    st.session_state['entrada'] = 0
    st.session_state['saida'] = 0
    st.session_state['validade_dias'] = 0
    st.session_state['preco_unitario'] = 0.0
    st.session_state['temperatura_media'] = 0.0
    st.session_state['categoria'] = categorias[0]
    st.session_state['dia_semana'] = 0
    st.session_state['fornecedor'] = "Ceasa Minas"
    st.session_state['promocao'] = "Não"
    st.session_state['feriado'] = "Não"

with col1:
    entrada = st.number_input("Quantidade de entrada", min_value=0, step=1, help="Quantidade total recebida do produto.", key='entrada')
    validade_dias = st.number_input("Dias até a validade", min_value=0, step=1, help="Dias restantes até o vencimento.", key='validade_dias')
    categoria = st.selectbox("Categoria", categorias, help="Tipo do produto.", key='categoria')
    preco_unitario = st.number_input("Preço unitário (R$)", min_value=0.0, format="%.2f", help="Preço de cada unidade. Não pode ser negativo.", key='preco_unitario')
    temperatura_media = st.number_input("Temperatura média (°C)", min_value=-30.0, max_value=60.0, format="%.1f", help="Temperatura média do ambiente. Valores típicos: -10 a 40°C.", key='temperatura_media')

with col2:
    saida = st.number_input("Quantidade de saída", min_value=0, step=1, help="Quantidade vendida ou utilizada. Não pode ser maior que a entrada.", key='saida')
    dia_semana = st.selectbox(
        "Dia da semana",
        list(range(7)),
        format_func=lambda x: ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"][x],
        help="Dia da semana referente ao registro.", key='dia_semana')
    fornecedor = st.selectbox(
        "Fornecedor",
        [
            "Ceasa Minas",
            "Frutaria São Jorge",
            "Hortifruti Oba",
            "Swift",
            "Ambev",
            "Makro",
            "Carrefour",
            "Atacadão",
            "Supermercados BH",
            "VerdeMais",
            "Sacolão ABC",
            "Distribuidora Santa Luzia",
            "Mart Minas",
            "Assaí Atacadista",
            "Outro"
        ],
        help="Fornecedor do produto.", key='fornecedor')
    promocao = st.selectbox("Promoção?", ["Não", "Sim"], help="O produto está em promoção?", key='promocao')
    feriado = st.selectbox("É feriado?", ["Não", "Sim"], help="O registro refere-se a um feriado?", key='feriado')

# Validação de entradas
erro = None
if saida > entrada:
    erro = "A quantidade de saída não pode ser maior que a de entrada."
elif preco_unitario < 0:
    erro = "O preço unitário não pode ser negativo."
elif temperatura_media < -30 or temperatura_media > 60:
    erro = "Temperatura média fora do intervalo permitido (-30°C a 60°C)."

if erro:
    st.error(erro)

# Botão Limpar campos
st.button("Limpar campos", on_click=limpar_campos)

# Botão para limpar histórico de previsões (CSV e session_state)
if st.button('Limpar histórico de previsões', type='primary'):
    st.session_state['historico_previsoes'] = []
    salvar_historico([])
    st.success('Histórico de previsões limpo com sucesso!')

# Exibe imagem com descrição alternativa
with col3:
    img_path = categoria_imagens.get(categoria, categoria_imagens["Outro"])
    alt_text = f"Imagem ilustrativa da categoria {categoria}"
    if os.path.exists(img_path):
        st.image(img_path, use_container_width=True, caption="Exemplo da comida selecionada", output_format="JPEG")
    else:
        st.warning(f"Imagem não encontrada para a categoria selecionada: {img_path}")
    st.info("Dica: Ajuste os parâmetros para simular diferentes cenários e tomar melhores decisões.")

# Adiciona um separador visual
st.markdown("<hr style='border:1px solid #4F8EF7; margin:1.5em 0;'>", unsafe_allow_html=True)

# Botão de previsão com feedback visual e loading (compacto)
if not erro and st.button("🔮 Prever sobra", use_container_width=True):
    # Monta novamente o DataFrame com os dados inseridos pelo usuário
    dados = {
        'entrada': [entrada],
        'saida': [saida],
        'validade_dias': [validade_dias],
        'dia_semana': [dia_semana],
        'categoria': [categoria],
        'fornecedor': [fornecedor],
        'preco_unitario': [preco_unitario],
        'promocao': [1 if promocao == "Sim" else 0],
        'feriado': [1 if feriado == "Sim" else 0],
        'temperatura_media': [temperatura_media]
    }
    df = pd.DataFrame(dados)
    df = pd.get_dummies(df)
    for col in modelo.feature_names_in_:
        if col not in df.columns:
            df[col] = 0
    df = df[modelo.feature_names_in_]
    with st.spinner("Calculando previsão..."):
        pred = modelo.predict(df)[0]
    # Bloco Resumo da obra atualizado com os valores informados
    st.markdown(f"""
    <div style='background:#23272f;padding:1.5em 2em;border-radius:12px;color:#fff;margin:1em 0;'>
        <h4 style='color:#4F8EF7;'>Resumo da obra</h4>
        <b>Entrada:</b> {entrada} &nbsp; | &nbsp; <b>Saída:</b> {saida} &nbsp; | &nbsp; <b>Categoria:</b> {categoria} &nbsp; | &nbsp; <b>Fornecedor:</b> {fornecedor}<br>
        <b>Preço unitário:</b> R$ {preco_unitario:,.2f} &nbsp; | &nbsp; <b>Temperatura média:</b> {temperatura_media:,.1f}°C<br>
        <b>Promoção:</b> {'Sim' if promocao == 'Sim' else 'Não'} &nbsp; | &nbsp; <b>Feriado:</b> {'Sim' if feriado == 'Sim' else 'Não'}<br>
        <b>Dias até a validade:</b> {validade_dias} &nbsp;
    </div>
    """, unsafe_allow_html=True)
    # Bloco de previsão destacado e com número centralizado
    st.markdown(f"""
        <div style='display:flex;justify-content:center;align-items:center;margin:2em 0;'>
            <div style='background:#23272f;padding:2.5em 4em;border-radius:24px;color:#fff;box-shadow:0 2px 12px #0003;text-align:center;'>
                <span style='font-size:2.2em;font-weight:600;letter-spacing:1px;display:block;'>Previsão de sobra (unidades)</span>
                <span style='font-size:4.5em;font-weight:bold;color:#4F8EF7;line-height:1.1;display:block;margin-top:0.3em;text-align:center'>{str(pred).replace('.', ',')}</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    # Mensagem sobre o nível de desperdício
    if pred > entrada * 0.5:
        st.warning("Atenção: previsão de alto desperdício! Considere ajustar o pedido ou promoção.", icon="⚠️")
    elif pred < entrada * 0.1:
        st.success("Ótimo! Baixo desperdício previsto.", icon="✅")
    else:
        st.info("Desperdício dentro do esperado.", icon="ℹ️")
    # Histórico de previsões
    st.session_state['historico_previsoes'].append({
        'entrada': entrada,
        'saida': saida,
        'validade_dias': validade_dias,
        'dia_semana': dia_semana,
        'categoria': categoria,
        'fornecedor': fornecedor,
        'preco_unitario': preco_unitario,
        'promocao': promocao,
        'feriado': feriado,
        'temperatura_media': temperatura_media,
        'previsao': pred
    })
    salvar_historico(st.session_state['historico_previsoes'])
    # Alerta visual para sobra negativa
    if pred < 0:
        st.error("Atenção: o modelo previu sobra negativa. Verifique os dados informados ou reavalie o modelo.")

# Exibe histórico de previsões
if st.session_state['historico_previsoes']:
    st.markdown("<h4 style='color:#4F8EF7;'>Histórico de Previsões</h4>", unsafe_allow_html=True)
    st.dataframe(pd.DataFrame(st.session_state['historico_previsoes']))

# Botão para exportar histórico em Excel
if st.session_state['historico_previsoes']:
    df_historico = pd.DataFrame(st.session_state['historico_previsoes'])
    excel_bytes = b''
    if not df_historico.empty:
        buffer = io.BytesIO()
        df_historico.to_excel(buffer, index=False, engine='openpyxl')
        buffer.seek(0)
        excel_bytes = buffer.read()
    st.download_button(
        label='Exportar histórico em Excel',
        data=excel_bytes,
        file_name='historico_previsoes.xlsx',
        mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        disabled=df_historico.empty
    )

# Rodapé moderno e acessível
st.markdown("---")
st.caption(
    "<span style='color:#4F8EF7;'>Desenvolvido para facilitar a gestão de estoques e reduzir desperdícios.</span>", unsafe_allow_html=True
)
