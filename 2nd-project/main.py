# ATIVIDADE 1

from ucimlrepo import fetch_ucirepo 
   
heart_disease = fetch_ucirepo(id=45) 
   
X = heart_disease.data.features 
y = heart_disease.data.targets 
  
print(heart_disease.variables)

print(X.isnull().sum())

X['ca'] = X['ca'].fillna(X['ca'].median())
X['thal'] = X['thal'].fillna(X['thal'].median())

print(X.isnull().sum())

print(y.columns)

y = (y['num'] > 0).astype(int)

print(y.value_counts())

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    stratify=y,
    random_state=42
)

print(f"Treino:\n{y_train.value_counts()}")
print(f"\nTeste:\n{y_test.value_counts()}")

from sklearn.preprocessing import StandardScaler

cols = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']

scaler = StandardScaler()

X_train[cols] = scaler.fit_transform(X_train[cols])
X_test[cols]  = scaler.transform(X_test[cols])

print(X_train[cols].mean())
print(X_train[cols].std())

# ATIVIDADE 2

from sklearn.linear_model import LogisticRegression

modelo = LogisticRegression(
    solver='liblinear', 
    random_state=42, 
    max_iter=1000
)

modelo.fit(X_train, y_train)

iteracoes = modelo.n_iter_[0]
print(f"Iterações necessárias para a convergência: {iteracoes}")

# ATIVIDADE 3

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_curve, auc
import matplotlib.pyplot as plt

y_pred = modelo.predict(X_test)
y_prob = modelo.predict_proba(X_test)[:, 1]

acuracia = accuracy_score(y_test, y_pred)

precisao = precision_score(y_test, y_pred)

recall = recall_score(y_test, y_pred)

f1 = f1_score(y_test, y_pred)

print("--- MÉTRICAS DE AVALIAÇÃO ---")
print(f"Acurácia: {acuracia:.4f}")
print(f"Precisão: {precisao:.4f}")
print(f"Recall:   {recall:.4f}")
print(f"F1-score: {f1:.4f}\n")

fpr, tpr, thresholds = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)

print(f"Valor da AUC (Área sob a curva ROC): {roc_auc:.4f}\n")

plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'Curva ROC (AUC = {roc_auc:.4f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--', label='Modelo Aleatório (AUC = 0.5000)')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('Taxa de Falsos Positivos (1 - Especificidade)')
plt.ylabel('Taxa de Verdadeiros Positivos (Sensibilidade/Recall)')
plt.title('Curva ROC - Previsão de Doenças Cardiovasculares')
plt.legend(loc="lower right")
plt.grid(alpha=0.3)
plt.show()