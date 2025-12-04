#Funciones

"""
Archivo: funciones.py
Contiene las funciones de búsqueda en Shodan, Google y Whois.
-t o --target: hace referencia al termino de búsqueda que el usuario requiera. 
Este debe ser genérico para cualquiera de las opciones disponibles y, por lo tanto, de carácter obligatorio.
 -s o –shodan: debe tomar el valor de target y realizar la búsqueda en Shodan. 
 -g o –google: debe tomar el valor de target y realizar la búsqueda en Google. 
 -w o –whois: debe tomar el valor de target y realizar la búsqueda en Whois. 
"""

import shodan
from googlesearch import search
import whois

# --- Shodan ---
def buscar_shodan(target: str) -> str:
    """
    Realiza una búsqueda en Shodan usando la API.
    """
    try:
        api = shodan.Shodan("Api_key")  # Reemplazar con tu API Key
        resultado = api.host(target)
        return f"[Shodan] Información de {target}: {resultado}"
    except Exception as e:
        return f"Error en búsqueda Shodan: {e}"

# --- Google ---
def buscar_google(target: str) -> str:
    """
    Realiza una búsqueda en Google usando googlesearch-python.
    """
    try:
        resultados = list(search(target, num_results=5))
        return "[Google] Resultados:\n" + "\n".join(resultados)
    except Exception as e:
        return f"Error en búsqueda Google: {e}"

# --- Whois ---
def buscar_whois(target: str) -> str:
    """
    Realiza una consulta Whois sobre un dominio.
    """
    try:
        informacion  = whois.whois(target)
        return f"[Whois] Información de {target}:\n{informacion}"
    except Exception as e:
        return f"Error en búsqueda Whois: {e}"
