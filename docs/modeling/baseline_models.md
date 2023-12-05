# Reporte del Modelo Baseline

Este documento contiene los resultados del modelo baseline.

## Descripción del modelo

El modelo baseline es el primer modelo construido y se utiliza para establecer una línea base para el rendimiento de los modelos posteriores.

## Variables de entrada

Lotes de imágenes con su etiqueta correspondiente.

## Variable objetivo

Etiqueta númerica.

## Evaluación del modelo

### Métricas de evaluación

Accuracy: Toma el accuracy_score de sklearn, basado en las etiquetas reales contra las predicciones, para mayor facilidad se convierte el vector de ceros y uno, al índice correspondiente.


### Resultados de evaluación

Tabla que muestra los resultados de evaluación del modelo baseline, incluyendo las métricas de evaluación.

![resultados ml flow](image.png)

## Análisis de los resultados

Descripción de los resultados del modelo baseline, incluyendo fortalezas y debilidades del modelo.

modelos:

modelo base: ResNet50 de keras.

* epochs_10: Modelo base con capas congeladas durante 10 épocas, por ende se usa su capacidad actual para estas imágenes.
* epochs_70: Modelo epochs_10 con aumento a 70 épocas.
* epochs_10_warm_70_train: Modelo base, con calentamiento durante 10 épocas y reentrenamiento (liberando capas finales) durante 70 épocas.





## Conclusiones

Conclusiones generales sobre el rendimiento del modelo baseline y posibles áreas de mejora.

Los modelos base, requieren ser tunneados para que se ajusten al problema particular, un gran tiempo de entrenamiento provee mejores resultados siempre y cuando se liberen las capas para reentrenar los pesos.


