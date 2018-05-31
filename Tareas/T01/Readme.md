**Tarea 01 - Tomás Burotto Clément**

En primer lugar es necesario clarificar que la tarea no está completa. Es más le falta bastante, lamento los inconvenientes 
 :( . Las siguientes funciones no se encuentran implementadas correctamente:

 - Estrategias de extinción
 - Posición y estado de los recursos
 - Barra de estado
 
A continuación explicaré las siguientes clases que se encuentran implementadas dentro de la tarea.

- Menu:
Esta clase pretende imprimir el menu con el que el usuario interactúa. Para esto pide información como usuario y clave. Utiliza la clase usuario,  para verificar su existencia. Luego estan las clases Menu_Anaf y Menu_Jefes_Pilotos quienes heredan de Menu. Imprimien la información necesaria para el usuario y el respectivo menú.

- Usuario:
Esta clase es la encargada de dar los atributos del usuario. Se encarga de leer los archivos y cargar sus datos utilizando el modulo lector.py. De esta clase heredan Usuario_Anaf y Usuario_Jefes_Pilotos quienes se instancean dependiendo de la identidad recogida a partir del nombre de usuario y la clave ingresada.

- Hora_fecha:
Esta clase se encarga de generar una hora y fecha según lo que se ingrese. Permite calcular las horas que existen entre dos horas distintas. Además de permitir la comparación entre dos fechas para saber cual se encuentra más o menos avanzada.

- Incendio:
Esta clase permite instancear un incendio a partir de un id ingresado. Recopila las distintas informaciones del incendio y los guarda como atributos.

-  Inicializar_Clima:
Esta clase permite ver como se afectan los incendios según e clima presente. Para esto calcula las longitudes y latitudes maximas y mínimas de un clima y ve si estas se solapan con la longitudes y latitudes máximas y mínimas de un incedio. Según esto y la hora de inicio de un incendio y la hora actual, permite afectar al incendio dependiendo del tipo de clima. Este puede aumentar o dismunuir los puntos de poder de un incendio.
 
Todos estas clases se relacionan como se muestra en el diagrama de clases. Finalmente quería lamentar lo incompleto de la tarea, espero que la próxima este más completa.
