# 🍽️ Previsão de Desperdício de Alimentos

## Projeto de extensão que utiliza Python e Machine Learning para prever o desperdício de alimentos, com foco na redução de sobras e apoio à tomada de decisão.

## 📋 Índice
- [Sobre o Projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Instalação](#instalação)
- [Como Usar](#como-usar)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Dados e Modelos](#dados-e-modelos)
- [Contribuindo](#contribuindo)
- [Autores](#autores)
- [Licença](#licença)

## 🎯 Sobre o Projeto

O **Previsão de Desperdício de Alimentos** é uma solução inovadora que utiliza inteligência artificial e machine learning para prever e reduzir o desperdício de alimentos em estabelecimentos comerciais. Desenvolvido como parte de um projeto de extensão universitária, nosso objetivo é ajudar restaurantes, supermercados e outros estabelecimentos a otimizar seu gerenciamento de estoque, reduzir perdas financeiras e contribuir para a sustentabilidade ambiental.

### 🌍 Impacto Social
- **Redução de perdas**: Minimiza o desperdício de alimentos em até 30%
- **Economia financeira**: Reduz custos operacionais para estabelecimentos
- **Sustentabilidade**: Contribui para os Objetivos de Desenvolvimento Sustentável (ODS)
- **Conscientização**: Promove práticas mais sustentáveis no setor alimentício

## ✨ Funcionalidades

- 🔍 **Análise Preditiva**: Previsão de desperdício baseada em dados históricos
- 📊 **Dashboard Interativo**: Visualizações claras e intuitivas dos dados
- ⚡ **Processamento em Tempo Real**: Análises rápidas e atualizações dinâmicas
- 📱 **Interface Web Responsiva**: Acesso de qualquer dispositivo
- 📈 **Relatórios Detalhados**: Geração automática de relatórios mensais
- 🎯 **Alertas Inteligentes**: Notificações sobre risco de desperdício

## 🛠️ Tecnologias Utilizadas

### Linguagens e Frameworks
- ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) Python 3.8+
- ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white) Pandas - Manipulação de dados
- ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white) NumPy - Computação científica
- ![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white) Scikit-learn - Machine Learning

### Visualização e Interface
- ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white) Streamlit - Interface web
- ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat-square&logo=plotly&logoColor=white) Matplotlib - Visualizações
- ![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?style=flat-square&logo=seaborn&logoColor=white) Seaborn - Gráficos estatísticos

### Ferramentas de Desenvolvimento
- ![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white) Git - Controle de versão
- ![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=flat-square&logo=visual-studio-code&logoColor=white) VS Code - IDE

## 🚀 Instalação

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Git

### Passo a Passo

1. **Clone o repositório**
```bash
git clone https://github.com/seu-usuario/previsao-desperdicio-alimentos.git
cd previsao-desperdicio-alimentos
```

2. **Crie um ambiente virtual (recomendado)**
```bash
# No Windows
python -m venv venv
venv\Scripts\activate

# No Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. **Instale as dependências**
```bash
pip install -r previsao-desperdicio-alimentos/requirements.txt
```

4. **Verifique a instalação**
```bash
python --version
pip list
```

## 📖 Como Usar

### Opção 1: Interface Web (Recomendado)
```bash
# Navegue até o diretório do projeto
cd previsao-desperdicio-alimentos

# Execute a aplicação Streamlit
streamlit run src/main.py
```
Acesse: http://localhost:8501

### Opção 2: Execução Direta
```bash
# Execute o script principal
python src/main.py
```

### Opção 3: Jupyter Notebook
```bash
# Inicie o Jupyter
jupyter notebook notebooks/analise_exploratoria.ipynb
```

## 📁 Estrutura do Projeto

```
previsao-desperdicio-alimentos/
│
├── src/                          # Código fonte principal
│   ├── main.py                  # Ponto de entrada da aplicação
│   ├── analise_dados.py         # Análise exploratória de dados
│   ├── modelo_ml.py             # Modelos de machine learning
│   ├── pre_processamento.py     # Limpeza e preparação dos dados
│   └── utils/                   # Utilitários
│       ├── app_interface.py     # Interface do Streamlit
│       ├── visualizacoes.py     # Funções de visualização
│       └── helpers.py           # Funções auxiliares
│
├── data/                        # Dados do projeto
│   ├── raw/                    # Dados brutos
│   ├── processed/              # Dados processados
│   └── external/               # Fontes externas de dados
│
├── models/                      # Modelos salvos
│   ├── modelo_sobra.pkl        # Modelo principal treinado
│   ├── scaler.pkl              # Normalizador
│   └── encoder.pkl             # Codificador de features
│
├── notebooks/                   # Notebooks Jupyter
│   ├── analise_exploratoria.ipynb
│   ├── feature_engineering.ipynb
│   └── avaliacao_modelos.ipynb
│
├── imagens/                     # Recursos visuais
│   ├── logo.png
│   └── screenshots/
│
├── tests/                       # Testes automatizados
│   ├── test_modelo.py
│   └── test_interface.py
│
├── requirements.txt             # Dependências Python
├── .gitignore                  # Arquivos ignorados pelo Git
├── README.md                   # Este arquivo
└── treinamento.log            # Logs de execução
```

## 📊 Dados e Modelos

### Fonte de Dados
- Dados históricos de vendas e desperdício
- Informações de estoque e validade de produtos
- Dados climáticos (temperatura, umidade)
- Eventos especiais e sazonalidade

### Features Utilizadas
- **Temporais**: Dia da semana, mês, feriados
- **Meteorológicos**: Temperatura, precipitação
- **Comerciais**: Preço, categoria do produto, promoções
- **Históricos**: Vendas passadas, taxa de desperdício anterior

### Modelos de ML
- **Regressão Linear**: Baseline para comparação
- **Random Forest**: Modelo principal com melhor desempenho
- **XGBoost**: Modelo alternativo para ensemble
- **Redes Neurais**: Em desenvolvimento para casos complexos

### Métricas de Avaliação
- **MAE (Mean Absolute Error)**: < 5% de erro médio
- **RMSE (Root Mean Square Error)**: < 7% de erro quadrático
- **R² Score**: > 0.85 de explicação da variância

## 🤝 Contribuindo

Contribuições são sempre bem-vindas! Para contribuir:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

### Diretrizes de Contribuição
- Siga o padrão de código PEP 8
- Adicione testes para novas funcionalidades
- Atualize a documentação conforme necessário
- Use commits semânticos

## 🐛 Reportando Bugs

Encontrou um bug? Por favor, abra uma [issue](https://github.com/seu-usuario/previsao-desperdicio-alimentos/issues) com:
- Descrição detalhada do problema
- Passos para reproduzir
- Screenshots (se aplicável)
- Versão do Python e dependências

## 📞 Suporte

- 📧 Email: yansantos2410@gmail.com
- 📱 WhatsApp: (41) 99688-8764

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🙋‍♂️ Autores

- **Yan de Oliveira** - *Trabalho inicial* - [Meu Git Hub](https://github.com/yandeoliveira)

## 🎓 Agradecimentos

- Agradeço imensamente à UniOpet pelo apoio no desenvolvimento deste projeto
- Inspirado na luta global contra o desperdício de alimentos
- Dados fornecidos por estabelecimentos parceiros

---

<p align="center">
  <i>Desenvolvido com ❤️ para um futuro mais sustentável</i>
</p>

