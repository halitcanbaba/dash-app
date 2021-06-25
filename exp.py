import mysql.connector
import pandas as pd 
my_conn = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="Bjk1903",
      database="mt4"
    )
####### end of connection ####
my_data = pd.read_sql("SELECT * FROM mt4_users WHERE LOGIN='83601'",my_conn)
print(my_data[['NAME','GROUP']])