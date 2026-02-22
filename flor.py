import bpy
import math

# Paso 1: Limpiar la escena [cite: 18, 27, 28]
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Paso 2: Definición de variables [cite: 19, 31, 32, 33]
radio = 3
angulo_actual = 0
paso_angular = 60 

# Paso 3: Círculo Central [cite: 20, 35, 36]
bpy.ops.mesh.primitive_circle_add(radius=radio, location=(0, 0, 0), vertices=64)

# Paso 4: Ciclo WHILE para completar la figura [cite: 93, 94, 95]
while angulo_actual < 360:
    # Calcular nueva posición usando coordenadas polares [cite: 4, 5, 7, 96]
    x = radio * math.cos(math.radians(angulo_actual))
    y = radio * math.sin(math.radians(angulo_actual))
    
    # Crear el círculo periférico [cite: 97]
    bpy.ops.mesh.primitive_circle_add(radius=radio, location=(x, y, 0), vertices=64)
    
    # Actualización de estado para evitar bucle infinito [cite: 99, 100]
    angulo_actual += paso_angular
