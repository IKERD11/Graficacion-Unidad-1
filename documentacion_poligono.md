# Documentación del Proyecto: Generación de Polígono 2D en Blender

Este documento explica en detalle el funcionamiento del script de Python para Blender (`poligono2d.py`), el cual genera de forma procedural un polígono regular bidimensional utilizando matemáticas puras (coordenadas polares) y la API de mallas de Blender.

## 1. Introducción
A diferencia de crear objetos primitivos predefinidos (como cubos o esferas), este script construye un objeto 3D desde cero definiendo matemáticamente la ubicación exacta de cada uno de sus vértices en el espacio y cómo estos se conectan mediante aristas (líneas) para formar una figura cerrada plana, en este caso, en el plano XY (2D).

## 2. Código Fuente

```python
import bpy
import math

def crear_poligono_2d(nombre, lados, radio):
    # Crear una nueva malla y un nuevo objeto
    malla = bpy.data.meshes.new(nombre)
    objeto = bpy.data.objects.new(nombre, malla)

    # Vincular el objeto a la escena actual
    bpy.context.collection.objects.link(objeto)

    vertices = []
    aristas = []

    # Cálculo de vértices usando coordenadas polares a cartesianas
    for i in range(lados):
        angulo = 2 * math.pi * i / lados
        x = radio * math.cos(angulo)
        y = radio * math.sin(angulo)
        vertices.append((x, y, 0))  # Z = 0 para mantenerlo en 2D

    # Definir las conexiones (aristas) entre los vértices
    for i in range(lados):
        aristas.append((i, (i + 1) % lados))

    # Cargar los datos en la malla
    malla.from_pydata(vertices, aristas, [])
    malla.update()

# Limpiar la escena antes de empezar
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Llamada a la función: Un hexágono de radio 5
crear_poligono_2d("Poligono2D", lados=6, radio=5)
```

## 3. Análisis del Código Paso a Paso

### 3.1. Importación de Librerías
```python
import bpy
import math
```
- `bpy`: Es la librería principal de la API de Python para interactuar con Blender, manipular la escena, objetos, mallas, etc.
- `math`: Proporciona funciones matemáticas estándar, esenciales aquí para usar `math.pi` (el valor de π), `math.cos()` y `math.sin()` para la trigonometría.

### 3.2. Creación e Inicialización del Objeto
```python
def crear_poligono_2d(nombre, lados, radio):
    malla = bpy.data.meshes.new(nombre)
    objeto = bpy.data.objects.new(nombre, malla)
    bpy.context.collection.objects.link(objeto)
```
1.  **`bpy.data.meshes.new(nombre)`**: Crea un bloque de datos vacío en la memoria de Blender destinado a almacenar información de geometría (vértices, bordes, caras).
2.  **`bpy.data.objects.new(nombre, malla)`**: Crea el contenedor (el "Objeto" que ves en la interfaz de Blender) y le asigna la malla recién creada. Un objeto requiere una malla para tener forma física.
3.  **`bpy.context.collection.objects.link(objeto)`**: Inserta físicamente el objeto en la escena (específicamente en la colección activa) para que sea visible y renderizable.

### 3.3. Cálculo Geométrico (Vértices)
```python
    vertices = []
    aristas = []

    for i in range(lados):
        angulo = 2 * math.pi * i / lados
        x = radio * math.cos(angulo)
        y = radio * math.sin(angulo)
        vertices.append((x, y, 0))
```
Este es el corazón matemático del script. Para dibujar un polígono regular (donde todos los lados y ángulos son iguales), imaginamos un círculo perfecto y colocamos puntos a distancias equivalentes a lo largo de su borde.
- `2 * math.pi` representa los 360 grados de un círculo completo expresados en radianes.
- Al dividir este valor entre la cantidad de `lados`, obtenemos la "porción" de ángulo (el incremento) entre un vértice y el siguiente.
- Al multiplicar por la iteración `i`, calculamos el ángulo absoluto actual.
- **Trigonometría**: Empleamos conversión de coordenadas polares (radio y ángulo) a cartesianas (x, y). 
  - `x = radio * coseno(ángulo)`
  - `y = radio * seno(ángulo)`
- El valor Z se empuja forzosamente a `0`, lo que garantiza que todos los puntos existan únicamente en el "suelo", haciendo la figura estrictamente bidimensional. La tupla `(x, y, 0)` se agrega a la lista `vertices`.

### 3.4. Conexión de Vértices (Aristas)
```python
    for i in range(lados):
        aristas.append((i, (i + 1) % lados))
```
Tener puntos en el espacio no forma un objeto sólido o dibujable; necesitan estar unidos. 
El ciclo crea líneas ("aristas" o _edges_) nombrando el índice de inicio y el índice de finalización (conectando el vértice 0 con el 1, el 1 con el 2, etc.).
- La operación `(i + 1) % lados` (módulo) es el truco clave aquí. Asegura de que cuando se alcanza el último vértice, este conecte de vuelta con el primer vértice (el 0), cerrando así perfectamente el bucle del polígono. Por ejemplo, en un hexágono (6 lados), el último vértice es el 5. `(5 + 1) % 6` es `0`. Así que conecta el 5 con el 0.

### 3.5. Construcción de la Malla
```python
    malla.from_pydata(vertices, aristas, [])
    malla.update()
```
- `from_pydata()` es una función que acepta tres listas: vértices, aristas y caras. Toma los datos matemáticos calculados e inyecta la geometría real en la malla vacía. (El tercer argumento es una lista vacía `[]` porque solo estamos creando el contorno 2D de alambres/líneas, sin rellenarlo con una cara plana "sólida").
- `malla.update()` fuerza a Blender a recalcular las estructuras internas para que los cambios se reflejen de inmediato en el espacio de trabajo.

### 3.6. Ejecución y Limpieza
```python
# Limpiar la escena antes de empezar
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Llamada a la función: Un hexágono de radio 5
crear_poligono_2d("Poligono2D", lados=6, radio=5)
```
- Las primeras dos líneas borran todo el escenario para evitar encimar objetos cada vez que se ejecute el script repetidamente.
- Finalmente, se invoca la función pidiendo una figura de 6 lados (Hexágono) con un tamaño de 5 unidades desde el centro hacia los vértices.

### 3.7. Variaciones de Código (Opcional)
Si deseas experimentar con otras formas geométricas, simplemente altera los parámetros de la función en la última línea:

```python
# Crear un Triángulo
crear_poligono_2d("Triangulo", lados=3, radio=3)

# Crear un Octágono similar a un letrero de 'ALTO'
crear_poligono_2d("Octagono", lados=8, radio=4)

# Crear un círculo aproximado (múltiples lados pequeños)
crear_poligono_2d("Circulo", lados=64, radio=5)
```

---

## 4. Vistas del Proyecto

A continuación, se presentan las capturas de pantalla de los resultados logrados con el código dentro del entorno de Blender:

### Script en el Editor de Texto
Esta imagen muestra el entorno de `Scripting` en Blender, con el archivo de código Python redactado que permite crear la geometría bidimensional del polígono procedimentalmente.

![Código en Editor](codigo_poligono.png)

### Resultado Geométrico (Hexágono 2D)
Esta vista dentro del `Layout` de Blender ilustra la representación visual del objeto que se ha inyectado con los arreglos matemáticos. En ella se aprecia el objeto plano formado por sus vértices y las aristas cerrando el hexágono.

![Vista de Polígono 2D](vista_poligono.png)

---

## 5. Instrucciones de Ejecución
1. Abre un nuevo proyecto en **Blender**.
2. Dirígete al espacio de trabajo de **Scripting** en las pestañas superiores.
3. Haz clic en **+ New** para crear un archivo de texto en blanco.
4. Copia el código fuente completo proporcionado.
5. Presiona el botón de **▶ Play (Run Script)**.
6. En la ventana **Layout (3D Viewport)** podrás observar el contorno perfecto del hexágono dibujado mediante sus uniones en el espacio XYZ.
