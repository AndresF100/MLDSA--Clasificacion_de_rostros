# Despliegue de modelos

## Infraestructura

- **Nombre del modelo:** Reconocimiento de personas basado en imágenes previas
- **Plataforma de despliegue:** Gradio
- **Requisitos técnicos:** 
    * python==3.10
    * tensorflow
    * gradio
    * gdown
    * keras
    * cv2
    * pandas
    * numpy

- **Requisitos de seguridad:** Despliegue local

## Código de despliegue

- **Archivo principal:** scripts\deployment\Despliegue.ipynb

## Documentación del despliegue

- **Instrucciones de instalación:** Instalar los requimientos
- **Instrucciones de configuración:** ejecutar código de despliegue y acceder al local host dado por gradio
- **Instrucciones de uso:** Cargue una imagen (sugerido de scripts\data_acquisition\test) o una jpg (para imágenes de mayor dimensión a 250x250 se hace un recorte automático desde centro)