import pandas as pd

df = pd.read_csv('ClassicDisco.csv')

filtroArtista = df['Artist']
filtroTrilha = df['Track']
filtroAno = df['Year']
filtroAlbum = df['Album']
#Track(faixa), Year, Album

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


'''print(filtro.to_string())
print(filtro1.to_string())
print(filtro2.to_string())
print(filtro.to_string())'''

#print(filtro) - mostra as 5 primeiras e 5 ultimas linhas

