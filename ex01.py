import pandas as pd

dados = {
    'cargos':["assistente","analista","gerente","diretor"], #campo/chave e atributos daquela chave
    'salarios':[1000,2000,3000,4000]
}
dados_bi = pd.DataFrame(dados)
print(dados_bi)