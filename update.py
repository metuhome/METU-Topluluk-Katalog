import pandas as pd 
import wget

df = pd.read_csv("Topluluk Katalog Formu (Responses) - Form Responses 1.csv")

df["Topluluk Bilgilendirme Dosyası"][0]

names = list(df["Topluluk Adı"])

with open("index.md","w") as f:
    for i in names:
        f.write(i + "  \n")

