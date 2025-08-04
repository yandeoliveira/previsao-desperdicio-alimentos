import joblib
import os
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(), logging.FileHandler('treinamento.log', encoding='utf-8')]
)

# Função para carregar os dados principais do projeto
def carregar_dados():
    logging.info("Carregando dados principais...")
    try:
        # Caminho absoluto baseado na localização do script
        caminho_dados = os.path.join(os.path.dirname(__file__), 'dados.csv')
        df = pd.read_csv(caminho_dados)
        logging.info("Arquivo 'dados.csv' carregado com sucesso.")
    except FileNotFoundError:
        logging.error("Arquivo 'dados.csv' não encontrado. Por favor, adicione o arquivo na pasta do projeto.")
        raise Exception(
            "Arquivo 'dados.csv' não encontrado. Por favor, adicione o arquivo na pasta do projeto.")
    # Enriquecimento opcional dos dados com informações adicionais dos produtos
    try:
        caminho_info = os.path.join(os.path.dirname(__file__), 'info_produtos.csv')
        info_produtos = pd.read_csv(caminho_info)
        # Mescla as informações adicionais ao dataframe principal
        df = pd.merge(df, info_produtos, on='produto_id', how='left')
        logging.info("Arquivo 'info_produtos.csv' encontrado e mesclado aos dados.")
    except FileNotFoundError:
        logging.warning("Arquivo 'info_produtos.csv' não encontrado. Seguindo sem enriquecimento.")
    return df

def preparar_pipeline(df):
    logging.info("Preparando pipeline de pré-processamento e modelo...")
    # Colunas
    numeric_features = ['entrada', 'saida', 'validade_dias', 'preco_unitario', 'temperatura_media']
    categorical_features = ['dia_semana', 'categoria', 'fornecedor', 'promocao', 'feriado']
    # Preenche valores ausentes
    df = df.fillna({'categoria': 'Desconhecido', 'fornecedor': 'Desconhecido'})
    # Variável alvo
    y = df['sobrou']
    # Pipeline numérico
    numeric_transformer = Pipeline([
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler())
    ])
    # Pipeline categórico
    categorical_transformer = Pipeline([
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])
    # Pré-processador
    preprocessor = ColumnTransformer([
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])
    # Pipeline completo
    pipeline = Pipeline([
        ('preprocessor', preprocessor),
        ('regressor', RandomForestRegressor(random_state=42))
    ])
    X = df[numeric_features + categorical_features]
    logging.info("Pipeline preparado.")
    return pipeline, X, y

def treinar_e_avaliar(pipeline, X, y):
    logging.info("Treinando e avaliando modelo com validação cruzada...")
    # Validação cruzada
    scores = cross_val_score(pipeline, X, y, cv=5, scoring='r2')
    logging.info(f"Acurácia média (R²) na validação cruzada: {scores.mean():.2f} ± {scores.std():.2f}")
    # Treina no conjunto completo
    pipeline.fit(X, y)
    joblib.dump(pipeline, 'modelo_sobra.pkl')
    logging.info("Pipeline completo salvo como 'modelo_sobra.pkl'.")
    return pipeline

# Bloco principal do script
if __name__ == "__main__":
    try:
        # Carrega os dados
        df = carregar_dados()
        pipeline, X, y = preparar_pipeline(df)
        pipeline = treinar_e_avaliar(pipeline, X, y)
        # Exemplo de previsão
        logging.info("Exemplo de previsões de sobra:")
        previsoes = pipeline.predict(X[:10])
        for i, prev in enumerate(previsoes):
            produto_id = df.iloc[i]['produto_id'] if 'produto_id' in df.columns else '-'
            nome_produto = df.iloc[i]['nome_produto'] if 'nome_produto' in df.columns else '-'
            logging.info(f"  Amostra {i+1}: Produto {produto_id} ({nome_produto}) - {prev:.2f} unidades")
        logging.info("Processo finalizado com sucesso!")
    except Exception as e:
        logging.error(f"Erro: {e}")

try:
    import pandas as pd
except ImportError:
    import pip
    pip.main(['install', 'pandas'])



