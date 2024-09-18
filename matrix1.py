import random #para no estar metiendo los datos xd
import time #ver cuanto tiempo tarda

# Crear la matriz 
alumnos_materias = [[random.randint(0, 100) for _ in range(6)] for _ in range(500)]

# Función para buscar la calificación del alumno 321 en la materia 5
def buscar_alumno_materia(alumnos, alumno_index, materia_index):
    return alumnos[alumno_index][materia_index]

# Medir el tiempo de ejecución para la búsqueda
start_time = time.time()

# Buscar al alumno 321 y la materia 5 (índices en 0, por lo que alumno 321 es índice 320 y materia 5 es índice 4)
calificacion = buscar_alumno_materia(alumnos_materias, 320, 4)

end_time = time.time()
execution_time = end_time - start_time

print(f"La calificación del alumno 321 en la materia 5 es: {calificacion}")
print(f"Tiempo de ejecución (Primero alumnos, luego materias): {execution_time:.8f} segundos")

