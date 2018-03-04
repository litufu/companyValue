# _author : litufu
# date : 2018/3/4

import pandas as pd


# file = r'H:\project\companyvalue\new_data_base_table.xlsx'
# df = pd.read_excel(file,sheetname='Balance_sheet_field')
# print(df[:10])


import tushare as ts
df = ts.get_stock_basics()
print(df[:10])