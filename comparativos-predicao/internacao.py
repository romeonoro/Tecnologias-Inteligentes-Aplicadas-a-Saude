# 1. Carregar os dados (Arquivo local)
# Certifique-se de ter feito o upload do arquivo 'dados_saude_predicao.csv'
df_p2 = pd.read_csv('dados_saude_predicao.csv')

# 2 e 3. Selecionar colunas de interesse e apagar nulos
features_p2 = ['Idade', 'Pressao_Arterial', 'Colesterol_Total', 'Frequencia_Cardiaca_Max']
target_p2 = 'Risco_Internacao'
df_p2 = df_p2[features_p2 + [target_p2]].dropna()

# 4. Features e variável alvo
X = df_p2[features_p2]
y = df_p2[target_p2]

# 5. Divisão treino/teste com estratificação
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

# 6. Padronizar
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 7 e 8. Treinar e Avaliar
resultados_p2 = []
print("--- Avaliação dos Modelos: Problema 2 (Saúde) ---\n")

for nome, modelo in modelos.items():
    modelo.fit(X_train, y_train)
    y_pred = modelo.predict(X_test)
    
    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average='macro', zero_division=0)
    resultados_p2.append((nome, acc, f1))
    
    print(f"Modelo: {nome}")
    print(f"Acurácia: {acc:.4f} | F1-Score (Macro): {f1:.4f}")
    print("Matriz de Confusão:")
    print(confusion_matrix(y_test, y_pred))
    print("-" * 50)

# 9. Mostrar ranking final
resultados_p2.sort(key=lambda x: x[2], reverse=True)
print("\nRanking Final (Problema 2):")
for nome, acc, f1 in resultados_p2:
    print(f"{nome:<25} Acc: {acc:<8.4f} F1: {f1:<8.4f}")
