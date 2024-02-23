import pandas as pd

def remove_null(df,coluna,logs=False):
    # Removendo linhas com valores Nulos
    shape_antigo = df[df[coluna].isnull()].shape
    
    df.dropna(subset=[coluna],inplace=True)
    
    if logs:
        print(f'Foram removidas {shape_antigo[0]-df[df[coluna].isnull()].shape[0]} da coluna {coluna}')

    return df