import pandas as pd

df = pd.read_excel("People.xlsx")

print(df["Age"].sum())