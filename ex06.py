#filtrar as músicas lançadas após 1980 e mostre apenas ano e faixa(track)
import pandas as pd

df = pd.read_csv('ClassicDisco.csv')

print(df[df['Year']>1980][['Year','Track']])
#de padrão mostra as 5 ultimas e 5 primeiras,