# Guía de Instalación y Visualización

## Descripción
Eversión analítica de una esfera utilizando superficies regladas
[https://arxiv.org/abs/1711.10466](https://arxiv.org/abs/1711.10466)


## Requisitos Previos
- Python 3.x instalado en tu sistema.

## Pasos de Instalación

1. **Crear un Entorno Virtual:**
  ```
  python -m venv Eversion
  ```


2. **Activar el Entorno Virtual:**
- En Windows:
  ```
  Eversion\Scripts\activate
  ```
- En sistemas Unix/MacOS:
  ```
  source Eversion/bin/activate
  ```

3. **Actualizar pip (administrador de paquetes de Python):**
  ```
  python -m pip install --upgrade pip
  ```

4. **Instalar Dependencias:**
  ```
  python -m pip install -r requirements.txt
  ```

## Ejecución de la Aplicación

1. **Crear visualización eversión de cilindro:**

  ```
  manim -pql eversions/cylinder.py CylinderEversion
  ```


