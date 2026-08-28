import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, f1_score

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

# 1. Carregar os dados (Arquivo local)
# Certifique-se de ter feito o upload do arquivo 'dados_predicao_modelos.csv'
df_p1 = pd.read_csv('dados_predicao_modelos.csv')

# 2 e 3. Selecionar colunas de interesse e apagar nulos
features_p1 = ['Idade', 'Renda_Anual_K', 'Score_Credito', 'Pontuacao_Engajamento']
target_p1 = 'Compro_Produto'
df_p1 = df_p1[features_p1 + [target_p1]].dropna()

# 4. Features e variável alvo
X = df_p1[features_p1]
y = df_p1[target_p1]

# 5. Divisão treino/teste com estratificação
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

# 6. Padronizar (necessário para SVM e KNN)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 7. Modelos de classificação
modelos = {
    'Logistic Regression': LogisticRegression(max_iter=1000),
    'Decision Tree': DecisionTreeClassifier(random_state=42),
    'Random Forest': RandomForestClassifier(random_state=42),
    'KNN': KNeighborsClassifier(),
    'Naive Bayes': GaussianNB(),
    'SVM': SVC(random_state=42),
    'Gradient Boosting': GradientBoostingClassifier(random_state=42)
}

# 8. Avaliar cada modelo
resultados_p1 = []
print("--- Avaliação dos Modelos: Problema 1 (Marketing) ---\n")

for nome, modelo in modelos.items():
    modelo.fit(X_train, y_train)
    y_pred = modelo.predict(X_test)
    
    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average='macro', zero_division=0)
    resultados_p1.append((nome, acc, f1))

    print(f"Modelo: {nome}")
    print(f"Acurácia: {acc:.4f} | F1-Score (Macro): {f1:.4f}")
    print("Matriz de Confusão:")
    print(confusion_matrix(y_test, y_pred))
    print("-" * 50)

# 9. Mostrar ranking final
resultados_p1.sort(key=lambda x: x[2], reverse=True)
print("\nRanking Final (Problema 1):")
for nome, acc, f1 in resultados_p1:
    print(f"{nome:<25} Acc: {acc:<8.4f} F1: {f1:<8.4f}")
