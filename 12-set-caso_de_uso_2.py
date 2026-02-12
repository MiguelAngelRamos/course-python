## Fuente de datos de servidores
import json # Importar para dar un formato legible a la salida

servidores = [
    {"id": "SRV-01", "modelo": "NVIDIA DGX", "vram": 80, "estado": "activo"},
    {"id": "SRV-02", "modelo": "ASUS TUF", "vram": 8, "estado": "mantenimiento"},
    {"id": "SRV-03", "modelo": "NVIDIA DGX", "vram": 80, "estado": "activo"},
]

def filtrar_servidores_activos(lista_servidores:list[dict]) -> list[dict]:
    return [servidor for servidor in lista_servidores if servidor["estado"] == "activo"]

def calcular_vram_total(lista_servidores:list[dict]) -> int:
    total = 0
    for servidor in lista_servidores:
        total = total + servidor["vram"] # total += servidor["vram"]
    return total
    # return sum(servidor["vram"] for servidor in lista_servidores)

def mostrar_reporte(titulo:str, datos:list[dict], total_vram:int):
    print(f"\n === {titulo.upper()} ===")
    print(json.dumps(datos, indent=4)) # Imprime los datos en formato JSON con indentación
    print(f"VRAM Total Disponible: {total_vram} GB")
"""
lista_filtrada = []
    for servidor in lista_servidores:
        if servidor["estado"] == "activo":
            lista_filtrada.append(servidor)
    return lista_filtrada
"""
if __name__ == "__main__":
    servidores_activos = filtrar_servidores_activos(servidores)
    vram_disponible = calcular_vram_total(servidores_activos)
    mostrar_reporte("Reporte de Servidores Activos", servidores_activos, vram_disponible)