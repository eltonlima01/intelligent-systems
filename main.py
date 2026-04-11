# ATIVIDADE 1

import pandas

dataset = pandas.read_csv("./datasets/Power Plant Data.csv")
dataset

x = dataset[["AT", "V", "AP", "RH"]]
y = dataset["PE"]

corr = x.corrwith(y)
print(corr)

print()

# ATIVIDADE 2

print(x.corr())