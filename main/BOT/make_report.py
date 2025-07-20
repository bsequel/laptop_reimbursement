import os
import pandas as pd

from config import *
import config

outputFolder = config.outputFolder

outputFilePath = os.path.join(outputFolder, 'output.xlsx')

table_name = config.table_name

sql_qery = f''' select * from {table_name} '''
df = pd.read_sql_query(sql_qery, con=con)
df.to_excel(outputFilePath, index=False)


