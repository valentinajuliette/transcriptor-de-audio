# Transcriptor de Audio con Whisper (CPU)

Este proyecto permite transcribir archivos de audio (`.m4a`, `.mp3`, etc.) a texto utilizando `faster-whisper`, optimizado para CPU.

Es un proyecto exprés que desarrollé para no tener que pagar por aplicaciones externas que transcriban el audio de las múltiples entrevistas que tendré que llevar a cabo durante mi tesis.

Es una versión beta y con muuuucha oportunidad de mejora, empezando porque algunas palabras no las transcribe correctamente y no logra diferenciar entre locutores. Estaré trabajando en eso cuando pueda y subiré avances ;)

## Requisitos

* Python 3.9 o superior
* Windows
* FFmpeg instalado y agregado al PATH

## Instalación paso a paso

### 1. Crear carpeta del proyecto

Abrir CMD o PowerShell y ejecutar:

```bash
mkdir C:\transcriptor
cd C:\transcriptor
```

### 2. Crear entorno virtual

```bash
python -m venv venv
```

### 3. Activar entorno virtual

En CMD:

```bash
venv\Scripts\activate
```

### 4. Actualizar pip (recomendado)

```bash
python -m pip install --upgrade pip setuptools wheel
```

### 5. Instalar dependencias

```bash
python -m pip install faster-whisper
```

## Instrucciones de uso

1. Copiar el archivo de audio dentro de la carpeta del proyecto:

```text
C:\transcriptor\
│
├── venv\
├── transcriptor.py
├── audio.m4a
```

2. Ejecutar el script:

```bash
python transcriptor.py
```

## Salida

Se generará automáticamente un archivo `.txt` con:

* Transcripción completa.
* Timestamps cada 5 minutos (personalizable).
* Texto formateado en bloques legibles.

Ejemplo:

```text
[00:00:00]
Hola, muchas gracias por acompañarnos...

[00:05:02]
Bueno, en ese contexto también es importante...
```

## Notas importantes

* El archivo de audio debe estar en la misma carpeta que el script o indicar la ruta completa.
* El tiempo de procesamiento depende de:
  * duración del audio
  * potencia del CPU
* No se requiere GPU.