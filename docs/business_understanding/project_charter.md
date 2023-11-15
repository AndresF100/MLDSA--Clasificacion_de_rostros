# Project Charter - Entendimiento del Negocio

## Nombre del Proyecto

Clasificación de rostros

## Objetivo del Proyecto

El presente proyecto no tiene un campo de aplicación específico, sin embargo puede tomarse como verificador de identidad de una persona basada en una o más imágenes previas cargadas en un sistema, de esta manera el sistema permitiría distinguir personas de una base potencial.

De igual manera será un ajuste al proyecto del módulo anterior con el fin de estructurar el proyecto de acuerdo a las buenas prácticas y herramientas del módulo, y guardar registro de los experimentos y resultados a las redes neuronales entrenadas.

Para ello el principal problema de este verificador de identidad es ¿cómo reconocer a una persona? y posteriormente ¿cómo diferenciarla del resto?. 

## Alcance del Proyecto

### Incluye:

- Datos provenientes de Kaggle en específico del [Face Recognition Dataset](https://www.kaggle.com/datasets/stoicstatic/face-recognition-dataset/), los cuales vienen en un archivo comprimido, una vez abierto este archivo se encuentran imágenes centradas en una sola cara con los canales RGB, con dimensiones de 250x250, en total se tienen 1680 carpetas dentro de cada una se tienen imágenes de la persona (de 2 a 50), estas carpetas tienen como nombre id del 0 a 1679.

- Modelo clasificador de nuevos rostros

- Modelo funcional y desplegado

### Excluye:

- Carga directa de los datos

## Metodología

1. Recopilación de imágenes
2. Definición del modelo y registro en mlflow
3. Entrenamiento
4. Contraste contra modelos de reconocimiento facial preentrenados
5. Elección de mejor modelo
6. Despliegue

## Cronograma


| Etapa | Duración Estimada | Fechas |
|------|---------|-------|
|Recopilación de imágenes|1 semana| 2023-11-12 al 2023-11-18| 
|Definición del modelo y registro en mlflow|1 semana|2023-11-19 al 2023-11-25|
|Entrenamiento|1 semana|2023-11-26 al 2023-12-02|
|Contraste contra modelos de reconocimiento facial preentrenados|1 semana|2023-11-26 al 2023-12-02|
|Elección de mejor modelo|1 semana|2023-12-03 al 2023-12-09|
|Despliegue|1 semana|2023-12-03 al 2023-12-09|



Hay que tener en cuenta que estas fechas son de ejemplo, estas deben ajustarse de acuerdo al proyecto.

## Equipo del Proyecto

- Andrés Forero

## Presupuesto

Sin presupuesto asignado.

