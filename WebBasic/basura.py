import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def procesar():
    # Cargar el conjunto de datos Iris desde seaborn
    # #(aquí deberá cargar su conjunto de datos)
    data = sns.load_dataset('iris')
    # Ver las primeras filas del conjunto de datos
    print(data.head())
