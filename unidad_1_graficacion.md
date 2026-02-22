# Unidad I. Introducción a la Graficación por Computadora

Esta unidad proporciona los fundamentos necesarios para diseñar modelos gráficos que permitan el trazado y manipulación de objetos geométricos. A través de bases matemáticas y la automatización mediante scripting, se asientan las competencias para construir simulaciones y entornos digitales.

---

## 1.1 Historia y evolución de la graficación por computadora
La graficación ha evolucionado radicalmente desde sistemas primitivos de líneas en osciloscopios hasta los entornos fotorrealistas de realidad virtual actuales:

- **Años 50:** Surgimiento de las primeras pantallas vectoriales creadas primordialmente para usos militares y radares (Proyecto _Whirlwind_).
- **Años 60:** El hito de Ivan Sutherland al desarrollar "Sketchpad" en 1963. Este programa sentó las bases eternas de la interfaz gráfica de usuario (GUI) y el diseño asistido por computadora (CAD) moderno.
- **Años 70-80:** Época dorada de la investigación en iluminación y texturizado. Aparecen los primeros y más importantes algoritmos de sombreado, como el de _Gouraud_ y _Phong_. De manera paralela, nace la animación por computadora para la industria cinematográfica y publicitaria.
- **Actualidad:** Existe un predominio y masificación de interfaces vistosas tridimensionales en sistemas web (WebGL), plataformas móviles y aplicaciones _stand-alone_ gracias al aceleramiento por hardware de las GPUs.

## 1.2 Áreas de aplicación
Debido a la naturaleza de visualización de información, la graficación es una ciencia transversal fundamental en diversas áreas:

- **Simulación y Capacitación:** Creación de entornos virtuales de cero riesgo para entrenamiento de vuelo en aviación, cirugía médica simulada o tácticas militares.
- **Arte y Entretenimiento:** El núcleo visual de los videojuegos (motores como Unreal o Unity), películas de animación 3D de grandes estudios y efectos visuales (VFX) integrados en cine de acción real.
- **Diseño e Ingeniería:** Modelado 3D interactivo de piezas mecánicas, motores, y arquitectura civil (BIM/CAD).
- **Medicina y Noticias:** Reconstrucción tridimensional a partir de tomografías (visualización de anatomía local) y gráficos dinámicos o infografías para digestión de datos complejos en periodismo de datos.

## 1.3 Aspectos matemáticos de la graficación
Cualquier píxel dibujado en pantalla requiere operaciones numéricas por debajo. El diseño de modelos gráficos exige el uso intensivo de herramientas matemáticas robustas para solucionar problemas de trazo, posición, deformación y física:

- **Álgebra Lineal:** El uso de matrices y vectores es indispensable para representar coordenadas de puntos y ejecutar transformaciones afines fundamentales en el espacio 2D y 3D (Traslación, Rotación, Escalamiento).
- **Geometría Analítica:** Permite delimitar espacios utilizando ecuaciones de la recta para el _clipping_ (recortes de visión) y la definición de las fronteras de polígonos irregulares y regulares (Círculos, Hexágonos, etc).
- **Cálculo:** Vital para los gráficos vectoriales complejos, utilizando curvas paramétricas de Bezier, B-Splines o NURBS que garantizan superficies suaves (útil al modelar capós de autos o rostros).

## 1.4 Modelos del color: RGB, CMY, HSV y HSL
Para digitalizar el aspecto de un material, las propiedades lumínicas se representan de forma numérica dependiendo de la naturaleza del dispositivo de visualización.

- **RGB (Red, Green, Blue):** Modelo **Aditivo** (la suma de rojo, verde y azul da el blanco). Es el estándar universal para dispositivos emisores de luz como monitores, pantallas de teléfonos y televisores.
- **CMY(K) (Cyan, Magenta, Yellow, Key/Black):** Modelo **Sustractivo** (la suma de pigmentos quita la luz, por lo que su combinación da negro o tintes oscuros). Es usado con rigurosidad matemática para el proceso de impresión física en papel o superficies tangibles.
- **HSV / HSL (Hue, Saturation, Value/Lightness):** Modelos circulares basados en la **percepción humana**. El _Tono_ decide el color en el círculo cromático, la _Saturación_ cuánta vivacidad tiene o si tiende a gris, y la _Luminosidad/Valor_ qué tan brillante u oscuro se muestra el matiz.

### Tutorial Práctico: Iluminación Emanante de un Cubo en Blender
La graficación estudia cómo interactúa la luz, en Blender esta simulación puede ser activada fácilmente:
1. **Selección:** Haz clic derecho sobre el cubo principal en la escena de default.
2. **Modo de Edición:** Presiona la tecla `Tab` para entrar al Edit Mode y selecciona la cara específica que deseas que funja como un faro, seleccionando previamente el modo de 'caras' con la tecla `3`.
3. **Material:** Dirígete al panel lateral de la derecha, ingresa a la pestaña _Material Properties_ (el círculo cuadriculado rojizo) y crea un nuevo slot para el material seleccionando `+ New`.
4. **Emisión:** En el apartado _Surface_, cambia el tipo de BSDF Principal a `"Emission"`. Escoge la potencia de encandilamiento (`Strength`) y asinga un color como azul eléctrico.
5. **Renderizado:** Asegúrate de estar en el motor `Eevee` con la casilla de _Bloom_ (Resplandor) activa. Presiona `F12` para computar y ver el efecto final de la energía lumínica emanando matemáticamente de la capa del cubo hacia el entorno.

## 1.5 Representación y trazo de líneas y polígonos
Nos referimos a la algoritmia base de computador. Son los métodos que determinan el orden lógico en que ciertos píxeles deben encenderse y con qué proporción cromática para trazar ilusiones de figuras geométricas en una retícula formada por pixeles diminutos, superando en ocasiones el fenómeno informático de _Aliasing_ (bordes dentados).

### 1.5.1 Formatos de imagen
Dichas representaciones pueden grabarse para postestad de diferentes maneras:
- **Mapas de bits (Raster / Rastreo):** Son imágenes almacenadas por coordenadas como un gran arreglo de matrices de color por cada bloque o pixel; ej. PNG, JPG o BMP. Al buscar ver un detalle, muestran cuadrados pixelados perdiendo la definición original.
- **Vectoriales:** Formatos como el famosísimo SVG. No guardan posiciones, guardan comandos y fórmulas matemáticas puras de nodos e intersecciones escalables; puedes imprimirlo del tamaño de un estadio sin pérdida mínima de calidad y contornos perfectos.

### Ejercicios Prácticos de Dibujo de Polígonos y Curvas (con API Python de Blender)

A continuación, mostramos la teoría convertida en automatización.

#### Práctica 1: Dibujo de un Polígono y Álgebra Polar
Se usa la trigonometría (Seno y Coseno) en la programación para trazar las aristas de un polígono perfecto en Blender (ej. hexágono).

```python
import bpy, math

# Paso 1: Limpieza
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Paso 2 y 3: Configuración de Geometría
lados = 6  # Hexágono de 6 caras
radio = 5
vertices = []
aristas = []

# Trigonometría de Ángulos Espaciales 
for i in range(lados):
    angulo = 2 * math.pi * i / lados # Conversión de fracciones del círculo completo 
    x = radio * math.cos(angulo)     # Coordenada en X
    y = radio * math.sin(angulo)     # Coordenada en Y
    vertices.append((x, y, 0))

# Cerrar el contorno
for i in range(lados):
    aristas.append((i, (i + 1) % lados))

# Paso 4: Inyección a la malla en Escena
malla = bpy.data.meshes.new("Poligono2D")
objeto = bpy.data.objects.new("Poligono2D", malla)
bpy.context.collection.objects.link(objeto)

malla.from_pydata(vertices, aristas, [])
malla.update()
```

#### Práctica 2: La Flor de la Vida 
Esta composición geométrica demuestra cómo aplicar conceptos de **Traslación** y **Rotación**, utilizando círculos superpuestos controlados por un bucle lógico de acumulación de grados polares:

```python
import bpy, math

# Limpiar Escena predefinida de Blender
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Variables y Condiciones Limites
radio = 3
angulo_actual = 0
paso_angular = 60 # Cada iteración avanzará una fracción sexagesimal para orbitar

# 1er Elemento: Círculo Primitivo Central (Origen)
bpy.ops.mesh.primitive_circle_add(radius=radio, location=(0, 0, 0), vertices=64)

# Rotación Procedural vía Bucle de Ciclo "Mientras"
while angulo_actual < 360:
    # Conversión Polar a Cartesiano
    x = radio * math.cos(math.radians(angulo_actual))
    y = radio * math.sin(math.radians(angulo_actual))
    
    # 2do Elemento: Lluvia de Círculos "Pétalo" en los vértices del radio del primero
    bpy.ops.mesh.primitive_circle_add(radius=radio, location=(x, y, 0), vertices=64)
    
    # Fundamental: Acumulador (Impedir Bucle Infinito del "While")
    angulo_actual += paso_angular
```

## 1.6 Procesamiento de mapas de bits (Post-procesamiento)
Más allá del modelo original de las figuras 3D como en las prácticas anteriores, el procesamiento de mapas de bits se encarga de alterar la imagen bidimensional de salida una vez el motor ha "renderizado" (tomado la foto de nuestra escena).

Consiste en programar kernels matriciales, funciones de transferencia de píxel, e interpolaciones espaciales para la **manipulación directa de la matriz central de píxeles**. Así se logran aplicar:
- **Filtros Convulsivos**  (Ej. _Blur_, detección capciosa de bordes o contornos realzados).
- Cambios de espectro cromático, variaciones de brillo, niveles gama, de matiz  o contraste dinámico.
- Transformaciones espaciales en la cámara en sí o ruido algorítmico, por citar la composición nodal (_Compositor_) que proporciona Blender.

---

## Bibliografía y Referencias
*   Blender Foundation. (2026). _Blender 4.x Manual: Lighting and Materials._ Recuperado de https://docs.blender.org/manual/en/latest/render/shader_nodes/shader/emission.html
*   Hearn, D., & Baker, M. P. (2004). _Computer Graphics with OpenGL_ (3rd ed.). Pearson Education.
*   Hughes, J. F., Van Dam, A., McGuire, M., Sklar, D. F., Foley, J. D., Feiner, S. K., & Akeley, K. (2014). _Computer Graphics: Principles and Practice_ (3rd ed.). Addison-Wesley Professional.
*   Tecnológico Nacional de México. (2010). _Caracterización de la asignatura: Graficación (SCC-1010)_. Secretaría de Educación Pública.
*   Tecnológico Nacional de México. (2010). _Temario oficial: Ingeniería en Sistemas Computacionales_. Dirección de Docencia e Innovación Educativa.
