# Tarea Dev Junior - Ruuf

## 🎯 Objetivo

El objetivo de este ejercicio es poder entender tus habilidades como programador/a, la forma en que planteas un problema, cómo los resuelves y finalmente cómo comunicas tu forma de razonar y resultados.

## 🛠️ Problema

El problema a resolver consiste en encontrar la máxima cantidad de rectángulos de dimensiones "a" y "b" (paneles solares) que caben dentro de un rectángulo de dimensiones "x" e "y" (techo).

## 🚀 Cómo Empezar

### Opción 1: Solución en TypeScript
```bash
cd typescript
npm install
npm start
```

### Opción 2: Solución en Python
```bash
cd python
python3 main.py
```

## ✅ Casos de Prueba

Tu solución debe pasar los siguientes casos de prueba:
- Paneles 1x2 y techo 2x4 ⇒ Caben 4
- Paneles 1x2 y techo 3x5 ⇒ Caben 7
- Paneles 2x2 y techo 1x10 ⇒ Caben 0

---

## 📝 Tu Solución

Deja acá el link a tu video explicando tu solución con tus palabras_
https://drive.google.com/file/d/1oHh18fvT8A3gzaqzsSK9m2R62UlfQov2/view?usp=sharing


Se implementa un algoritmo que calcula el número de paneles al obtener una solución del escenario.

Las posiciones en el techo se representan de la siguiente manera:
```
# representar las posiciones en el roof
# ejemplo "roofW": 2, "roofH": 4
# =>
# [ 
# [0, 0],
# [0, 0],
# [0, 0],
# [0, 0]
# ]
#
# 

# "roofW": 3, "roofH": 5
# =>
#[
#[0, 0, 0]
#[0, 0, 0],
#[0, 0, 0],
#[0, 0, 0],
#[0, 0, 0],
#]
```

Antes de continuar se calcula el máximo de paneles posibles según el área disponible para reducir el espacio de búsqueda.

```
# por ejemplo: 
# 
#  "panelW": 1, "panelH": 2, "roofW": 2, "roofH": 4,
# => (2*4) // (1*2) = 8//2 = 4 paneles como maximo
#
#  "panelW": 1, "panelH": 2, "roofW": 3, "roofH": 5,
# => (5*3) // (1*2) = 15//2 = 7 paneles como maximo 
```

Luego se determinan las posibles soluciones considerando las posibles orientaciones de los paneles.
Por ejemplo para 2 paneles con dos combinaciones: 
```
# [horizontal, horizontal]
# [horizontal, vertical]
# [vertical, horizontal]
# [vertical, vertical]

# => son 2**2 = 4 combinaciones
```    
Se representa horizontal con False y vertical con True.

Finalmente por cada permutación se busca una solución válida utilizando como función de costo el espacio disponible en el  techo, es decir, se minimiza el espacio disponible.  

Notar que por la simetría del techo y paneles, basta con revisar solo la mitad de permutaciones. 

Se retorna el número de paneles de la mejor solución.  


---

## 💰 Bonus (Opcional)

Si completaste alguno de los ejercicios bonus, explica tu solución aquí:

### Bonus Implementado
Opción 2 (rectángulos superpuestos)



### Explicación del Bonus
Ya que el algoritmo implementado es genérico en la búsqueda de soluciones. Basta con adaptar las posiciones y valores de iteración.

Se asume 4 nuevos parámetros correspondientes a el ancho y alto de un segundo techo y el ancho y alto
de un "gap" correspondiente a la superposiciones de ambos  rectangulos. 

Por ejemplo, considerando el siguiente caso (rectangulo A de 4x4, rectangulo B de 4x4 y superposición de 2x2).

      "panelW": 1,
      "panelH": 2,
      "roofWA": 4,
      "roofHA": 4,
      "roofWB": 4,
      "roofHB": 4,
      "gapW": 2,
      "gapH": 2,
      "expected": 14

El techo vacio en su totalidad es representado de la siguiente forma, donde -1 son espacios no permitidos. 

```
[-1, -1, 0, 0,  0,  0]
[-1, -1, 0, 0,  0,  0]
[ 0,  0, 0, 0,  0,  0]
[ 0,  0, 0, 0,  0,  0]
[ 0,  0, 0, 0, -1, -1]
[ 0,  0, 0, 0, -1, -1]
```

Luego el problema es análogo al original considerando un solo rectangulo resultante de la superposición. 

Las nuevas iteraciones para generar dicho rectangulo se modifican de la siguiente forma:

```
# problema original
for y in range(roof_height): 
    for x in range(roof_width):
        # do something 

# problema bonus
for y in range(roof_height_B + roof_height_A - gap_height): 
    for x in range(roof_width_A + roof_width_B - gap_width ):
        # do something
```

Para la inserción de paneles la iteración es la misma. 

---

## 🤔 Supuestos y Decisiones

- Espacio discreto.
- Orientaciones posibles de paneles: horizontal y vertical.
