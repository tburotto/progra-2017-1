# Tarea 04 - Tomás Burotto Clément

Bienvenido a "LEAGUE OF PROGRA" (cualquier parecido a league of legends es mera coincidencia). 

### Introducción 
En primer lugar es necesario pedir disculpas por el desorden en la tarea, ojalá que en este readme encuentres todo lo necesario para entender lo que se hizo.
Además de esto también por lo poco desarrollado de la tarea.
### Alcance
Los siguientes items no fueron desarrollados en la tarea:
- Guardar estado de juego.
- Cargar partidas y estadisticas
- Disitintos niveles de dificultad, la computadora solo juega en modo "noob"
- Hay problemas con el "lag", creo que se debe especialmente por el uso de QThreads y no QTimers
- No se implementó el archivo con constantes del juego. No pueden ser modificadas.
### Modulos

- Inicio.py: Este modulo tiene la misión de generar todos los elementos presentes en la ventana pricipal.
- Elementos.py: Este modulo crea todos las "unidades" y edificios. Cada uno de los elementos presentes es un Thread que se vera en la pantalla (Chmpions, minions, etc..)
- TPersonasienda.py: Contine los elementos para hacer funcionar la tienda del juego.
- Juego.py: Posee la clase Game que se encarga de cambiar los atributos de los elementos del juego.
- Funciones.py: En este modulo se definieron funciones de apoyo para la simulación.


