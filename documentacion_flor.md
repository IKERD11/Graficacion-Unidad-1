# Documentación de Generador de Figura "Flor" en Blender

Este documento detalla el funcionamiento del script de Python para Blender (`flor.py`). Este programa utiliza un bucle condicional (`while`) y cálculos trigonométricos (coordenadas polares) para generar y distribuir círculos primitivos alrededor de un centro, produciendo una estructura visual similar a una "flor" bidimensional.

## 1. Introducción
El script hace uso de la automatización en Blender (`bpy`) acoplado con el módulo matemático estándar (`math`). En lugar de dibujar formas completas desde cero con vértices individuales (como vimos con la malla del polígono), este enfoque agrupa formas preexistentes: instancia un "Círculo Primitivo" central y luego itera rotando alrededor de éste, "sellando" círculos adicionales como si fueran pétalos.

## 2. Código Fuente

```python
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
```

## 3. Análisis del Código Paso a Paso

### 3.1. Limpieza de Entorno
```python
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()
```
Como paso estándar de automatización en Blender, seleccionamos todos los polígonos, luces y cámaras que existan en el lienzo actual y los borramos. Esto asegura un espacio vacío para que, al probar el script una y otra vez, las flores no se traslapen entre ejecuciones.

### 3.2. Definición de Variables y Estado
```python
radio = 3
angulo_actual = 0
paso_angular = 60 
```
Aquí se configura la lógica de distribución geométrica:
- `radio`: Establece tanto el tamaño (radio) inicial de cada círculo, como la **distancia** a la que estarán empujados los círculos periféricos desde el centro absoluto (origen). Elegir el mismo número implica que los círculos "pétalo" tocarán exactamente el centro geométrico del primer círculo, generando una geometría intersectada perfecta.
- `angulo_actual`: Funciona como nuestro acumulador, rastreando en qué ángulo de la rotación total vamos operando. Arranca en `0` (apuntando hacia la derecha en la gráfica matemática, eje X positivo).
- `paso_angular`: Dicta cuánto rotaremos en cada repetición. Al establecerse en `60`, sabiendo que un círculo tiene 360 grados, este script fabricará lógicamente `360 / 60 = 6` círculos periféricos conformando los pétalos.

### 3.3. Colocación de la Raíz Central
```python
bpy.ops.mesh.primitive_circle_add(radius=radio, location=(0, 0, 0), vertices=64)
```
Invoca al operador nativo de Blender para inyectar una "primitiva" (figuras preprogramadas). En este caso, añade al origen `(0,0,0)` el círculo con el radio de `3`. Se le da el argumento explícito de `vertices=64` porque, por defecto, Blender crea los círculos geométricos con solo 32 aristas unidas, lo que se ve puntiagudo o como un polígono plano. Elevar este número a 64 le da mayor definición o "curvatura limpia" al render final.

### 3.4. Bucle e Instanciación Procedural `while`
```python
while angulo_actual < 360:
    # Coordenadas polares a cartesianas con conversión a radianes
    x = radio * math.cos(math.radians(angulo_actual))
    y = radio * math.sin(math.radians(angulo_actual))
    
    # Primitiva periférica "Pétalo"
    bpy.ops.mesh.primitive_circle_add(radius=radio, location=(x, y, 0), vertices=64)
    
    # Avance del bucle
    angulo_actual += paso_angular
```
A diferencia del bucle `for` convencional, se usa aquí un `while` que corre mientras nuestro marcador no exceda ni complete la vuelta máxima `(< 360)`.
- La principal variante visual aquí es que **`math.cos/sin` exigen valores en _Radianes_**, en contraste con las variables de nuestro script (`360`, `60`), que están expresadas en grados _Sexagesimales_. Para solucionar esta incompatibilidad, se utiliza `math.radians()`, logrando un puente que evita engorrosas divisiones flotantes manuales.
- Se posicionan las primitivas de acuerdo a `x` e `y`.
- Es **CRUCIAL** la línea final del bucle: `angulo_actual += paso_angular`. Si se omite, `angulo_actual` viviría atrapado en `0` permanentemente con respecto a `< 360`, ocasionando un desastroso _bucle infinito_ que terminaría colapsando el software Blender.

---

## 4. Variaciones Prácticas y Mejoras en el Código

Agregando alteraciones senciilas, esta pequeña pieza de automatización es capaz de generar patrones radicalmente distintos.

### Rosa Densa Compleja (Iteración por Bucle `for`)
Reescribiendo la parte del ciclo puede formarse una rosa superpuesta y no depender de prevenir un bucle infinito manualmente con el `while`:

```python
# Aumentamos pétalos mediante bucle For en rango numérico
import bpy, math
# Limpieza...
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

radio = 4 # Más amplio
numero_petalos = 16 # Ajustable al instante, sin fracciones sexagesimales 

bpy.ops.mesh.primitive_circle_add(radius=radio, location=(0,0,0), vertices=64)

for i in range(numero_petalos):
    # Uso puro de Radianes desde el ciclo For (2*pi equivalente a círculo entero)
    angulo = i * (2 * math.pi / numero_petalos)
    x = radio * math.cos(angulo)
    y = radio * math.sin(angulo)
    
    bpy.ops.mesh.primitive_circle_add(radius=radio, location=(x, y, 0), vertices=64)
```

```

---

## 5. Vistas del Proyecto

A continuación, se presentan las capturas de pantalla de los resultados logrados con el código dentro del entorno de Blender:

### Script en el Editor de Texto
En esta imagen visualizamos cómo luce el script organizado dentro del área de `Scripting` en Blender, con la configuración del bucle `while` encargado de la distribución matemática.

![Código de la Flor](codigo_flor.png)

### Resultado Geométrico (Patrón Floral)
Al ejecutar el script, nos movemos a la vista `Layout` y notamos el patrón dibujado por el alambre de las primitivas de círculo. Los aros anaranjados y oscuros confluyen perfectamente creando la apariencia de flor simétrica en el centro de los ejes.

![Vista de la Flor](vista_flor.png)

---

## 6. Instrucciones de Ejecución
1. Abre un nuevo proyecto en **Blender**.
2. Dirígete a la interfaz o pestaña de **Scripting** en la banda superior de diseño.
3. Haz clic en el botón de archivo **+ New** para crear una hoja de Python.
4. Pega meticulosamente el Código Fuente superior (Fijándote que se respeten los sangrados lógicos u _indentations_ en el espacio debajo del `while`).
5. Pulsa el botón superior **▶ Play (Run Script)**.
6. Regresa al área **Layout**: Un arreglo floral matemático conformado por un denso cúmulo de arcos de alambre surgirá en tu malla y origen céntrico `(0,0,0)`.
