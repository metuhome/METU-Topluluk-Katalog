import pandas as pd 

df = pd.read_csv("Topluluk Katalog Formu (Responses) - Form Responses 1.csv")

names = list(df["Topluluk Adı"])

with open("index.md","w") as f:
    for i in names:
        f.write(i + "  \n")

