"""
Script de análise exploratória e atualização de dados/modelo

- Gera gráficos e estatísticas descritivas dos dados.
- Salva relatório em HTML.
- Permite atualizar os dados e re-treinar o modelo automaticamente.
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from main import carregar_dados, preparar_pipeline, treinar_e_avaliar

# 1. Carregar dados
df = carregar_dados()

# 2. Estatísticas descritivas e tipos
desc = df.describe(include='all')
print('Resumo estatístico:\n', desc)
print('\nTipos de dados:\n', df.dtypes)

# 3. Valores ausentes
missing = df.isnull().sum()
print('\nValores ausentes por coluna:\n', missing)

# 4. Gráficos exploratórios
os.makedirs('relatorio', exist_ok=True)
plt.figure(figsize=(10, 6))
sns.histplot(df['sobrou'], kde=True)
plt.title('Distribuição da variável alvo (sobrou)')
plt.savefig('relatorio/sobrou_hist.png')
plt.close()

for col in ['entrada', 'saida', 'validade_dias', 'preco_unitario', 'temperatura_media']:
    plt.figure(figsize=(8, 5))
    sns.boxplot(x=df[col])
    plt.title(f'Boxplot de {col}')
    plt.savefig(f'relatorio/box_{col}.png')
    plt.close()

# 5. Correlação
corr = df.corr(numeric_only=True)
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='Blues')
plt.title('Matriz de Correlação')
plt.savefig('relatorio/correlacao.png')
plt.close()

# 6. Salvar relatório simples em HTML
with open('relatorio/relatorio_dados.html', 'w', encoding='utf-8') as f:
    f.write('<h2>Relatório Exploratória dos Dados</h2>')
    f.write('<h3>Resumo estatístico</h3>')
    f.write(desc.to_html())
    f.write('<h3>Valores ausentes</h3>')
    f.write(missing.to_frame('Ausentes').to_html())
    f.write('<h3>Gráficos</h3>')
    f.write('<img src="sobrou_hist.png"><br>')
    for col in ['entrada', 'saida', 'validade_dias', 'preco_unitario', 'temperatura_media']:
        f.write(f'<img src="box_{col}.png"><br>')
    f.write('<img src="correlacao.png"><br>')

print('Relatório salvo em relatorio/relatorio_dados.html')

# 7. Atualizar dados e re-treinar modelo (opcional)
retrain = input('Deseja re-treinar o modelo com os dados atuais? (s/n): ').strip().lower()
if retrain == 's':
    pipeline, X, y = preparar_pipeline(df)
    pipeline = treinar_e_avaliar(pipeline, X, y)
    print('Modelo re-treinado e salvo como modelo_sobra.pkl')
else:
    print('Modelo não foi re-treinado.')

# 8. Dicionário de dados (documentação)
colunas = {
    'entrada': 'Quantidade total recebida do produto',
    'saida': 'Quantidade vendida ou utilizada',
    'validade_dias': 'Dias restantes até o vencimento',
    'dia_semana': 'Dia da semana (0=Domingo, 6=Sábado)',
    'categoria': 'Tipo do produto',
    'fornecedor': 'Fornecedor do produto',
    'preco_unitario': 'Preço de cada unidade',
    'promocao': 'Se o produto está em promoção (0=Não, 1=Sim)',
    'feriado': 'Se o registro refere-se a um feriado (0=Não, 1=Sim)',
    'temperatura_media': 'Temperatura média do ambiente',
    'sobrou': 'Quantidade de sobra (variável alvo)',
    'produto_id': 'Identificador único do produto',
    'nome_produto': 'Nome do produto (se disponível)'
}
with open('relatorio/dicionario_colunas.txt', 'w', encoding='utf-8') as f:
    for k, v in colunas.items():
        f.write(f'{k}: {v}\n')
print('Dicionário de colunas salvo em relatorio/dicionario_colunas.txt')
