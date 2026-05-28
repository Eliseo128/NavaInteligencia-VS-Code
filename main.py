# ==========================================
# SUCESIÓN DE FIBONACCI INTERACTIVA
# CBTIS 128
# Carrera: Inteligencia Artificial
# Materia: Elabora Proyectos de Programación Lógica
# Alumno: Nahum Flores
# NL = 21
# ==========================================

print("===================================")
print("   SUCESIÓN DE FIBONACCI EN PYTHON")
print("===================================")

# Solicitar cantidad de términos
n = int(input("¿Cuántos términos deseas mostrar?: "))

# Variables iniciales
a = 0
b = 1
contador = 0

print("\nSerie de Fibonacci:")

# Ciclo while
while contador < n:

    print(a)

    # Proceso Fibonacci
    siguiente = a + b
    a = b
    b = siguiente

    contador = contador + 1

print("\nPrograma finalizado")
print("Creado por Nahum Flores NL = 21")