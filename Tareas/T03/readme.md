# Tarea 03 - Tomás Burotto #

Bienvenido a "RQL" esta aplicación está diseñada para emplear métodos estadísticos en conjuntos de datos y variables.

### Modulos ###
La carpeta T03 contiene tres modulos que realizan distintas funciones dentro del programa

 - Main.py : en este modulo se encuentran implementadas como se relaciona Varios.py con la interfaz grafica. En el método "process consult", se ejecuta la función leer_consulta de Varios para leer el array que se entrega desde la interfaz. Se devuelve como un texto el cual se devuelve a la interfaz. Además se añadio el atributo "i" a la clase T03window, este permite añadir el numero de consulta que se realiza el cual aumenta en 1 cuando se realiza una consulta.
 
 - Varios.py: en este modulo existen tres funciones. La primera es leer_consulta. Esta función recibe una lista de consultas y devuelve un string de las respuestas. Principalmente sirve para entregar los resultados de las consultas en una forma legible para el usuario. Usa la función lector del modulo ConsultasBasicas. La segunda función definida es contador quien es un generador de numeros sucesivos, cada vez que se llama a "next(contador)". Finalmente esta la función generar_archivo que se encarga de generar el .txt saliente. Funciona de la misma forma que leer_consulta, solo que este guarda los resultados en un .txt
 
 - ConsultasBasicas.py: este modulo es el principal de la aplicación. En este se definen las distintas funciones para realizar las consultas (promedio, desviación, evaluar, graficar, etc...). Además se realizaron decoradores para las funciones de modo que se pueda implementar la asignación de str a variables o conjuntos. Para esto se usa una lista global en el cual se guardan las variables. Por último esta el decorador de anidación quién se encarga de verificar para las funciones si existe una anidación de consultas ejemplo:
 
 ```sh
consulta = ["asignar","x",["evaluar",["crear_funcion","normal",0,1]]
```

- Funciones.py : En este modulo se definieron las funciones de probabilidad que se requerían para la tareas. Estas son función normal, gamma, exponencial. Son utilizadas por la función crear_funcion de ConsultasBasicas. También se creó dentro de este modulo la función decimal_range que se utiliza para la función evaluar, donde se pide que el step puede ser decimal. De modo que decimal_range es un generador de valores entre un inicio y fin con un step que puede ser decimal. Otra función que se implemento es factorial, quien calcula de manera funcional el factorial de un numero entero. Finalmente también se encuentra como intruso abrir_archivo. Esta función permite leer un archivo .csv , es utilizado por extraer_columna, para extraer datos desde un archivo. 

### Elementos Faltantes y posibles errores ###
En esta tarea el principal ausente es el testing. Este no fue desarrollado en la tarea. Sin embargo pueden existir errores en el manejo de exceptions. Se intentó manejar los errores de una manera eficiente para que el nombre del error se identificara correctamente. Sin embargo, no se logró aquello por lo que para manejar los posibles errores simplemente se utilizó "Exception". 

### Otros detalles ###
Un detalle de la tarea es el momento de generar el archivo de salida. Para esto se ocupó el siguiente código:
 ```sh
j = contador()
    lista = [ConsultasBasicas.lector(x) for x in array]
    texto = [("----- Consulta {} -----\n".format(next(j))) +
             str(x) + "\n" for x in lista]
    texto = "".join(texto)
    archivo = open("resultados.txt", "w")
    archivo.write(texto)
    archivo.close()
```
Si bien se genera un archivo de salida este genera el mismo output que se genera en la consola del usuario al correr todas las consultas disponibles. Es por esto que quizás no es lo pedido ya que también genera el gráfico nuevamente. Es decir se abre una pestaña con el gráfico, lo cuál no es correcto. 

Otro detalle es que es necesario dar cuenta de que las funciones de factorial y contador fueron creadas con la ayuda de StackOverflow quién resolvio dudas sobre como crearlas.

Espero que este archivo haya clarificado las posibles dudas que surjan al corregir la tarea :)
