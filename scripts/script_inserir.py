import pandas as pd
from sqlalchemy import create_engine
from tqdm import tqdm

tables = ['previsao_estados', 'previsao_lojas', 'previsao_produtos', 'previsao_valor']

for i in tqdm(tables, desc="Processando tabelas"):
    df = pd.read_csv(f'preds/{i}.csv')
    engine = create_engine("sqlite:///data/predictions.db")
    df.to_sql(f'{i}', con=engine, if_exists='replace', index=False)
