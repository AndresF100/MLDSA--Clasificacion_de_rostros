# Reporte de Datos

Este documento contiene los resultados del análisis exploratorio de datos.

## Resumen general de los datos

Se cuenta con 8204 imágenes a color de dimensiones 250 x 250 en formato jpg, pertenecientes a 1680 clases, cada clase siendo una persona diferente identificada con un índice de 0 a 1679.

## Resumen de calidad de los datos

Los datos ya vienen preprocesados dejando dimensiones de 250 x 250 en las que se tiene como centro de la imagen el rostro de la persona, sin embargo se analizó la distribución de cantidad de imágenes por clase teniendo en su mayoría clases con menos de 5 imágenes por clase.

## Datos a usar

Los datos se separaron en carpetas train y test, trantando de mantener un split ratio de 80%, para el cargue de estas imágenes se usa un generador de datos de keras, se aconseja para el entranamiento usar aumento de datos o descartar las clases que tienen pocas imágenes.

