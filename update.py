import pandas as pd 

with open("index.md","r") as f:
    lines = f.readlines()


names = list(df["Topluluk Adı"])

with open("index.md","w") as f:
    for i in names:
        f.write(i + "  \n")

