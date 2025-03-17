import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris
from sklearn.preprocessing import LabelEncoder

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


# Cargar el conjunto de datos Iris desde seaborn
#(aquí deberá cargar su conjunto de datos)
data = sns.load_dataset('iris')

#--------------------------------
# tambien peude cargarse de otra manera, usando la libreria pandas:

# Cargar el conjunto de datos Iris
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Añadir la columna de las etiquetas (que son de tipo texto)
df['species'] = iris.target_names[iris.target]


# Verificar los datos
print(df.head())

# Convertir las etiquetas de 'species' en valores numéricos con LabelEncoder
label_encoder = LabelEncoder()
df['species'] = label_encoder.fit_transform(df['species'])

# Verificar los datos después de la conversión
print(df.head())

#--------------------------------

# Ver las primeras filas del conjunto de datos
print(data.head())
# Descripción general del conjunto de datos
print(data.describe())
# Generar boxplots para cada una de las características del conjunto de datos
plt.figure(figsize=(12, 8))

# Boxplot de todas las columnas numéricas
sns.boxplot(data=data[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']])
plt.title("Boxplot de las características del Iris")
plt.show()


# Histograma de las características numéricas
data[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].hist(bins=15, figsize=(12, 8))
plt.suptitle("Histogramas de las características del Iris")
plt.show()

# Pairplot para ver la relación entre las características numéricas
sns.pairplot(data, hue='species')
plt.suptitle("Pairplot de las características del Iris", y=1.02)
plt.show()


# Calcular la matriz de correlación
correlation_matrix =df.corr() # data.corr()

# Mostrar la matriz de correlación con un mapa de calor
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Mapa de calor de la correlación entre características")
plt.show()

# Gráfico de caja para comparar la longitud del sépalo entre las especies
plt.figure(figsize=(8, 6))
sns.boxplot(x='species', y='sepal_length', data=data)
plt.title("Comparación de la longitud del sépalo por especie")
plt.show()




# Modelo de regresión lineal
#************************************

# Seleccionamos las características (features) y la variable objetivo (target)
X = data[['sepal_length', 'sepal_width', 'petal_width']] # Variables predictoras
y = data['petal_length'] # Variable objetivo


# Dividir el conjunto de datos en entrenamiento y prueba (80% entrenamiento, 20% prueba)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Tamaño del conjunto de entrenamiento:", X_train.shape)
print("Tamaño del conjunto de prueba:", X_test.shape)

# Crear el modelo de regresión lineal
model = LinearRegression()

# Entrenar el modelo
model.fit(X_train, y_train)

 # Ver los coeficientes y la intersección (intercepto) del modelo
print(f"Coeficientes: {model.coef_}")
print(f"Intersección (intercepto): {model.intercept_}")


# Con el modelo entrenado, ahora podemos hacer predicciones sobre el conjunto de prueba (`X_test`).
y_pred = model.predict(X_test)

# Mostrar las predicciones y los valores reales
predictions_df = pd.DataFrame({'Real': y_test, 'Predicción': y_pred})
print(predictions_df.head())

#Ahora evaluamos el rendimiento del modelo utilizando métricas comunes de regresión: Error cuadrático medio (MSE) y R² (coeficiente de determinación) 
# Calcular el error cuadrático medio (MSE) y R²
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Error cuadrático medio (MSE): {mse}")
print(f"Coeficiente de determinación R²: {r2}")
# Graficar los valores reales vs. las predicciones
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, color='blue', label='Predicciones')

plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linewidth=2, label="Línea de referencia")
plt.xlabel("Valores reales")
plt.ylabel("Predicciones")
plt.title("Valores reales vs Predicciones")
plt.legend()
plt.show()


