import pandas as pd
connector = 'mysql+mysqlconnector://root:insofe@172.17.0.2:3306/cust_db'
bank = pd.read_sql("select * from bank", con=connector)
bank.head(6)
print(bank.head(6))