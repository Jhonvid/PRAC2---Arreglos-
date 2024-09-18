import random #para no estar metiendo los datos xd
import time

# Crear la matriz 
materias_alumnos = [[random.randint(0, 100) for _ in range(500)] for _ in range(6)]

# Función para buscar la calificación 
def buscar_materia_alumno(materias, materia_index, alumno_index):
    return materias[materia_index][alumno_index]

# Medir el tiempo de ejecución 
start_time = time.time()

# Buscar la materia 5 y el alumno 321 (índices en 0, por lo que materia 5 es índice 4 y alumno 321 es índice 320)
calificacion = buscar_materia_alumno(materias_alumnos, 4, 320)

end_time = time.time()
execution_time = end_time - start_time

print(f"La calificación del alumno 321 en la materia 5 es: {calificacion}")
print(f"Tiempo de ejecución (Primero materias, luego alumnos): {execution_time:.8f} segundos")
