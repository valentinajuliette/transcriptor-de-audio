import os
import textwrap
from faster_whisper import WhisperModel

def formatear_tiempo(segundos):
    horas = int(segundos // 3600)
    minutos = int((segundos % 3600) // 60)
    segundos_restantes = int(segundos % 60)
    return f"{horas:02d}:{minutos:02d}:{segundos_restantes:02d}"

# Personalizar entre las comillas con la ruta de tu archivo de audio
audio_path = r"C:\transcriptor\Entrevista1.m4a"

nombre_base = os.path.splitext(audio_path)[0]
archivo_salida = f"{nombre_base}_transcripcion.txt"

# Personalizar amaño de cada bloque de tiempo
# Ejemplo: 5 minutos = 300 segundos
max_duracion_bloque = 300

# Ancho máximo de cada línea en el archivo de texto (detalle visual)
# Sugiero no modificar a partir de aquí para evitar problemas de formato
ancho_linea = 100

model = WhisperModel("base", device="cpu", compute_type="int8")
segments, info = model.transcribe(audio_path, language="es")

segmentos_lista = list(segments)
bloques = []

if segmentos_lista:
    inicio_bloque = segmentos_lista[0].start
    texto_bloque = segmentos_lista[0].text.strip()

    for seg in segmentos_lista[1:]:
        duracion_potencial = seg.end - inicio_bloque

        if duracion_potencial <= max_duracion_bloque:
            texto_bloque += " " + seg.text.strip()
        else:
            bloques.append((inicio_bloque, texto_bloque))
            inicio_bloque = seg.start
            texto_bloque = seg.text.strip()

    bloques.append((inicio_bloque, texto_bloque))

with open(archivo_salida, "w", encoding="utf-8") as f:
    for inicio, texto in bloques:
        texto_limpio = " ".join(texto.split())
        texto_formateado = textwrap.fill(
            texto_limpio,
            width=ancho_linea,
            break_long_words=False,
            break_on_hyphens=False
        )

        f.write(f"[{formatear_tiempo(inicio)}]\n")
        f.write(texto_formateado)
        f.write("\n\n")

print(f"Archivo guardado como: {archivo_salida}")