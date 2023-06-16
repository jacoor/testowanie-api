import os
import pandas as pd



print(os.getcwd())
df = pd.read_json("data.json", encoding="utf-8")
print(df)
