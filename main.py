# ATIVIDADE 1

import pandas

dataset = pandas.read_csv("./dataset/Power Plant Data.csv")
dataset

x = dataset[["AT, V, AP, R"]]
y = dataset[["PE"]]

corr = x.corrwith(y)
corr