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
print()

# ATIVIDADE 3

import pandas as pd

df = pd.read_csv("datasets/Power Plant Data.csv")

print(df.head())

X = df.drop(columns=["PE"])
y = df["PE"]

from sklearn.preprocessing import MinMaxScaler

scaler  = MinMaxScaler(feature_range=(0, 1))
scaled  = scaler.fit_transform(X)
df_scaled = pd.DataFrame(scaled, columns=X.columns)
df_scaled

from sklearn.model_selection import train_test_split

X = df_scaled
X_train, X_test, y_train, y_test = train_test_split(
  X, y, test_size=0.2, random_state=42
)

print(f"Tamanho do dataset = {X.shape[0]} amostras")
print(f"Quantidade de amostras de treinamento = {X_train.shape[0]} amostras")
print(f"Quantidade de amostras de teste = {X_test.shape[0]} amostras")

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)

theta = model.coef_
print(theta)

theta_0 = model.intercept_
print(theta_0)
print()

# ATIVIDADE 4

from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import numpy as np

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)


print(f"Erro quadrático médio (MSE): {mse:.2f}")
print(f"Coeficiente de determinação (R²): {r2:.2f}")
print(f"Raiz do Erro quadrático médio (RMSE): {rmse:.2f}")
print(f"Erro absoluto médio (MAE): {mae:.2f}")