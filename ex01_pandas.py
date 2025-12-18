from sqlalchemy import create_engine 

import pandas as pd


#criar a conexão
host = 'localhost'
user = 'root'
password = ''
database = 'aulapandas'

engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}') #ceate engine é da biblioteca sqlalchemy, create engine é um fç (essa biblioeca permite usar sql no pthon) 

#df = pd.read_sql("select * from odontologia", con=engine) #não é  uma stringo mas um comando.....
df = pd.read_sql("select * from odontologia where UF in('SP','RJ')",con=engine) # escrita diferente....
print(df.to_string())