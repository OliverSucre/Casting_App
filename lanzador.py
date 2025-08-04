import sys
import os
import webbrowser
import tempfile
import shutil

def extraer_y_abrir_html():
    carpeta_temp = tempfile.mkdtemp()

    if hasattr(sys, "_MEIPASS"):
        ruta_base = os.path.join(sys._MEIPASS, "assets")
    else:
        ruta_base = os.path.join(os.path.dirname(__file__), "assets")

    shutil.copytree(ruta_base, os.path.join(carpeta_temp, "assets"), dirs_exist_ok=True)

    ruta_html = os.path.join(carpeta_temp, "assets", "Casting.html")

    webbrowser.open(f"file://{ruta_html}")

extraer_y_abrir_html()
