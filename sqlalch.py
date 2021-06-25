import pandas as pd
import sqlalchemy
#pip install PyMySQL

engine = sqlalchemy.create_engine('mysql+pymysql://root:Bjk1903@localhost/mt4')
df = pd.read_sql_table('mt4_users', engine)
type(df)