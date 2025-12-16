import pandas as pd
cargos = []
salarios = []

qtde = int(input("Quer cadastrar quantas informações?"))
           
for i in range(qtde):
    print(f"cadastro nº{i+1}")
    cargo = input("Cargo: ")
    salario = float(input("Salário: "))
    cargos.append(cargo)
    salarios.append(salario)
dados = {
    'cargos':cargos, 
    'salarios':salarios      #estava "salario" deu erro, no final todos os salários ficavam com o valor do último.....
}
dados_bi = pd.DataFrame(dados)
print(dados_bi)


