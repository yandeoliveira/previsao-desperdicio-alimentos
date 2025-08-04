def load_data(file_path):
    import pandas as pd
    data = pd.read_csv(file_path)
    return data

def preprocess_data(data):
    # Implementar limpeza e transformação dos dados
    return data

def save_data(data, file_path):
    data.to_csv(file_path, index=False)