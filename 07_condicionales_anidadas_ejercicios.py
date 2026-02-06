"""
Imagina que tienes una lista de programadores y solo quieres filtrar a aquellos que cumplen con requisitos específicos de lenguaje, años de experiencia y expectativa salarial.
"""
# Criterios definidos en un diccionario
requisitos = {
    "lenguaje": "Python",
    "min_experiencia": 3,
    "max_presupuesto": 5000
}
# Lista de candidatos (nuestra fuente de datos)
candidatos = [
    {"nombre": "Ana", "lenguaje": "Python", "exp": 5, "pretension": 4500},
    {"nombre": "Luis", "lenguaje": "Java", "exp": 4, "pretension": 4000},
    {"nombre": "Marta", "lenguaje": "Python", "exp": 2, "pretension": 3000},
    {"nombre": "Pedro", "lenguaje": "Python", "exp": 6, "pretension": 6000},
]

def filtrar_candidatos_aptos(lista_postulantes, criterios):
    postulantes_aptos = []
    for postulante in lista_postulantes:
        # inicio de validaciones anidadas
        if postulante["lenguaje"] == criterios["lenguaje"]:
            if postulante["exp"] >= criterios["min_experiencia"]:
                if postulante["pretension"] <= criterios["max_presupuesto"]:
                    postulantes_aptos.append(postulante)
    return postulantes_aptos

# Ejecutamos la función para filtrar candidatos
seleccionados = filtrar_candidatos_aptos(candidatos, requisitos)
print(f"Candidatos que pasan al foro técnico: {seleccionados}")