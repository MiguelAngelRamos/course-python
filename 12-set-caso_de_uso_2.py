## Fuente de datos de servidores
import json # Importar para dar un formato legible a la salida

servidores = [
    {"id": "SRV-01", "modelo": "NVIDIA DGX", "vram": 80, "estado": "activo"},
    {"id": "SRV-02", "modelo": "ASUS TUF", "vram": 8, "estado": "mantenimiento"},
    {"id": "SRV-03", "modelo": "NVIDIA DGX", "vram": 80, "estado": "activo"},
]

def filtrar_servidores_activos(lista_servidores:list[dict]) -> list[dict]:
    return [servidor for servidor in lista_servidores if servidor["estado"] == "activo"]
"""
lista_filtrada = []
    for servidor in lista_servidores:
        if servidor["estado"] == "activo":
            lista_filtrada.append(servidor)
    return lista_filtrada
"""
if __name__ == "__main__":
    servidores_operativos = filtrar_servidores_activos(servidores)
    print("Servidores activos:", servidores_operativos)