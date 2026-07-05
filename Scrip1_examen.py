titulo = "Evaluacion N°1 Programacion y Redes Virtualizadas"
integrantes = [
    {"rol": "Integrante 1", "nombre": "Claudio Torres"},
    {"rol": "Integrante 2", "nombre": "Benjamin Marchant"},
    {"rol": "Integrante 3", "nombre": "Benjamin Ortiz"},
    {"rol": "Integrante 4", "nombre": "Bastian Alvarez"}
]

print("-" * 50)
print(titulo)
print("-" * 50)
for integrante in integrantes:
    print(f"{integrante['rol']} : {integrante['nombre']}")
print("-" * 50)
