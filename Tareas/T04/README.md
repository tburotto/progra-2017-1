# Tarea 04 - Tomás Burotto Clément

Bienvenido al simulador de programación avanzada. Esta tarea consiste en un simulador virtual de un semestre de progrmación avanzada.
En este readme encontrarás todo lo que se relaciona con las funciones implementadas,
los modulos y fórmulas utilizadas para llevar a cabo la simulación.

### Introducción 
En primer lugar es necesario pedir disculpas por el desorden en la tarea, ojalá que en este readme encuentres todo lo necesario para entender lo que se hizo.

### Alcance
Por temas de tiempo hubieron problemas para implementar todo lo requerido en el enunciado. Los siguientes requerimientos no fueron implementados:
- Eventos no programados: en esta tarea quedó como gran ausente los eventos no programados, es decir que el nivel de programación no cambia si hubo o no una fiesta, el futbol no influye y los cortes de agua tampoco.
- Atraso de notas: tuve problemas para lograr que el coordinador atrasase las notas por lo que esto no funciona correctamente.
- Analisis de resultados : El problema que tuve fue al correr los distintos escenarios en conjunto de modo a poder compararlos, logree leer el archivo escenarios.csv sin embargo no implementé que se ejecutaran todos los escenarios.(no lo logré :( )
### Cambios con respecto al enunciado
Para lograr una simulación más dinámica y coherente cambie algunos parámetros que venían dados por el enunciado.
- Valor de "s" en bota de ramos: Me encontré con el problema de que una gran cantidad de alumnos botaban el curso tras la actividad 4, por lo que para evitar esto cambie el S a 3.

### Modulos

- Main.py: Este modulo solo corre la simulación con los parámetros por defecto. Traté de implementar aquí que se corrieran los otros escenarios para obtener una comparación pero no se logró.

- Simulacion.py: En este modulo encontraras la clase simulacion quien se encarga de simular los distintos eventos necesarios para crear la simulación. Se detallará mas adelante

- Personas.py: Aqui se encuentran las clases Alumno, Ayudante, Profesor, Coordinador. Son los objetos principales quienes pueblan la simulación.

- Funciones.py: En este modulo se definieron funciones de apoyo para la simulación.
-  Estadisticas.py : este modulo se encarga de generar el grafico final asi como todas las estadisticas relacionadas a la simulacion

### Explicacion de Simulacion
Existen distintos métodos implementados en la clase simulacion que son necesarios para dar vida a los distintos eventos. Explicaré algunos de los métodos para facilitar la comprensión. 

#### Run()
Este método permite el inicio de la simulacion, se conforma de tres partes. Uno es la población de la simulación cargando integrates.csv luego se inicia el while que define la simulacion donde se ejecutan los eventos necesarias. Finalmente se usa el modulo estadisticas para retornar las estadisticas relacionadas con la simulación 

#### Comienzo_semana()

Este modulo se ejecuta una vez que pasaron todos los eventos de la semana, y cargar cual sera la materia de la semana y calcula las horas que dedica un alumno al curso.

#### Publicacion_notas()
Tuve problemas implementando que las notas se subieran cada 2 semanas, por lo que las notas de las evaluaciones realizadas durante la semana se entregan al final de esta misma.

### Reunion_ayudantes()
Solo para la actividad y la tarea cree un método para realizar la reunión de los ayudantes para definir el nivel de exigencia. En los controles y el examen, este proceso se realiza en el mismo método que en el método de la realización de la evaluación.

### Conclusión 
Espero que este readme haya explicado alguna de las dudas que pudiesen surgir. El resto de los metodos en simulacion tienen nombres que deducen su funcionamiento. Cualquier duda porfavor no dudes en contactarme en tfburotto@uc.cl .
