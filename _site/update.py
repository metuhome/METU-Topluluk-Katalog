import pandas as pd 

def sort_mds(filepath="index.md"):
    with open(filepath,"r") as f:
        lines = f.readlines()
    lines.sort()
    with open(filepath,"w") as f:
        f.writelines(lines)



df = pd.read_csv("Topluluk Katalog Formu (Responses) - Form Responses 1.csv")

names = list(df["Topluluk Adı"])

with open("index.md","w") as f:
    for i in names:
        f.write(i + "  \n")

