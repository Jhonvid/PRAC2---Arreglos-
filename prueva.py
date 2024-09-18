import random
import time

# Función para generar los datos de los alumnos y materias
def generar_datos_alumnos_materias(num_alumnos, num_materias):
    return [[random.randint(0, 100) for _ in range(num_materias)] for _ in range(num_alumnos)]

# Función para generar los datos de las materias y alumnos
def generar_datos_materias_alumnos(num_materias, num_alumnos):
    return [[random.randint(0, 100) for _ in range(num_alumnos)] for _ in range(num_materias)]

# Función para buscar en la primera estructura (alumnos -> materias)
def buscar_alumno_materia(alumnos, alumno_index, materia_index):
    return alumnos[alumno_index][materia_index]

# Función para buscar en la segunda estructura (materias -> alumnos)
def buscar_materia_alumno(materias, materia_index, alumno_index):
    return materias[materia_index][alumno_index]

# Función para medir el tiempo de búsqueda en la primera estructura
def medir_tiempo_primera_estructura(num_alumnos, num_materias, alumno_index, materia_index):
    alumnos_materias = generar_datos_alumnos_materias(num_alumnos, num_materias)
    start_time = time.time()
    calificacion = buscar_alumno_materia(alumnos_materias, alumno_index, materia_index)
    end_time = time.time()
    return end_time - start_time, calificacion

# Función para medir el tiempo de búsqueda en la segunda estructura
def medir_tiempo_segunda_estructura(num_materias, num_alumnos, materia_index, alumno_index):
    materias_alumnos = generar_datos_materias_alumnos(num_materias, num_alumnos)
    start_time = time.time()
    calificacion = buscar_materia_alumno(materias_alumnos, materia_index, alumno_index)
    end_time = time.time()
    return end_time - start_time, calificacion

# Configuraciones para las pruebas con diferentes tamaños de datos
pruebas = [
    (1000, 100),
    (10000, 500),
    (100000, 10000)
]

# Índices de ejemplo para las pruebas (buscar alumno 321 y materia 5)
alumno_index = 320
materia_index = 4

# Ejecutar pruebas
resultados = []

for num_alumnos, num_materias in pruebas:
    # Medir tiempo para la primera estructura
    tiempo_primera, calificacion_primera = medir_tiempo_primera_estructura(num_alumnos, num_materias, alumno_index, materia_index)
    
    # Medir tiempo para la segunda estructura
    tiempo_segunda, calificacion_segunda = medir_tiempo_segunda_estructura(num_materias, num_alumnos, materia_index, alumno_index)
    
    resultados.append({
        'num_alumnos': num_alumnos,
        'num_materias': num_materias,
        'tiempo_primera': tiempo_primera,
        'calificacion_primera': calificacion_primera,
        'tiempo_segunda': tiempo_segunda,
        'calificacion_segunda': calificacion_segunda
    })

resultados
