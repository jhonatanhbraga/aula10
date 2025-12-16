import pandas as pd

df = pd.read_csv('ClassicDisco.csv')

filtroArtista = df['Artist']
filtroTrilha = df['Track']
filtroAno = df['Year']
filtroAlbum = df['Album']
#Track(faixa), Year, Album

'''
r = input("oque deseja analisar? a - artista. b- trilha. c- ano. d- album")
match r:
    case "a":
        print(filtroArtista.to_string())
    case "b":
        print(filtroTrilha.to_string())
    case "c":
        print(filtroAno.to_string())
    case "d":
        print(filtroAlbum.to_string())
'''

#print(filtro) - mostra as 5 primeiras e 5 ultimas linhas


#print(df.head)
#print(df.head(10))
#print(df.tail(10))

#filtro = df[df['Artist'] == "Aretha Franklin"]

#filtro = df[df['Year']>=1980]

#print(filtro)


filtro1 = df.head(30)
#filtro2 = filtro1.sort_values('Artist', ascending==false) #poe em ordem decrescente
filtro2 = filtro1.sort_values('Artist')
print(filtro2.to_string)
#isso é bem interessante