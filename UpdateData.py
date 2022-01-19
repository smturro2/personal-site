import numpy as np
import pandas_gbq as pd_gbq
import pandas as pd
import requests
import bs4
r = requests.get('https://pypistats.org/api/packages/quantum-tomography/overall')
data = r.json()


df_total.to_csv("df_total.csv", index=False)
df_year.to_csv("df_year.csv",index=False)
df_total2 = pd.read_csv("df_total.csv",index=False)
df_year2 = pd.read_csv("df_year.csv",index=False)

print(0)