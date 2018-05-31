
# Tarea 02 - Tomás Burotto #

Bienvenido al juego "PANDEMIC" este juego consiste en contagiar, al mundo entero a través de una enfermedad (Virus, Parásito o Bacteria). Acá se explicara el funcionamiento de la tarea.

### Modulos ###
La carpeta T02 contiene distintos modulos que realizan distintas funciones.

 - Main.py : solo importa los distintos módulos y corre el programa, al ejecutarlo, se inicia el juego.
 
 - Estructuras.py: en este módulo se definieron las distintas estructuras de datos a utilizar en el desarrollo de la tarea. Se definió las listas ligadas junto con sus métodos y los diccionarios y sus respectivos métodos.
 
 - Lectort.py: este módulo contiene la clase Lector la cual posee 5 métodos. cada uno de ellos tiene el objetivo de leer los archivos .cvs para obtener los datos del juego. Además tiene el método guardar_juego quién guarda el estado actual del juego para que sea continuado más tarde.
 
 - Cargar.py: este módulo tiene como única función de cargar un juego que haya sido guardado en un archivo .cvs. Obtiene los datos y genera un juego idéntico al guardado.
 
 - Plague.py : este es el módulo principal del juego. Dentro de él se implementaron las clases Pais, Pandemia, Cura y estadísticas. La primera tiene todos los métodos asociados al país. Así como los efectos que trae pasar un día, etc.. Luego pandemia es quien guarda los datos de cada país y el estado de la pandemia en el mundo. Por último cura implementa los métodos que permiten el descubrimiento de la infección en el mundo.  En este modulo también está implementado la clase estadística, quién se encarga de entregar las estadísticas del juego actualizadas al momento en que el jugador las requiere.
 
 - Gobierno.py : Este modulo pretende implementar las acciones de los gobiernos de los paises.
 
 - Menu.py : Este implementa el menú con el cual interactúa el usuario.
 
 ### Cambios en las formulas ###
 Para que el juego fuese más dinámico se hicieron modificaciones en las siguientes fórmulas que fueron proporcionadas por el enunciado.
 
- Formula de descubrimiento de la infección:
```sh
probabilidad = min((10**7)*(self.visibilidad * self.infectados * (self.muertos**2))/(self.populacion_total**3),1)
```
- Formula de probabilidad de infectar país vecino:
```sh
probabilidad_de_infeccion = min((7*self.infectados_totales) / ((self.vivos)*                                                                         (len(self.borders)+len(self.borders_airports))), 1)
```
- Formula para agregar nuevos infectados en el país:
```sh
nuevas_infecciones = int(int(random.randint(0, 6)*pandemia.contagiosidad)*self.infectados*0.5)
```
- Formula de probabilidad de muerte en el país:
```sh
if self.vivos < 10000000:
            probabilidad_de_muerte = min(min(0.2, (int(self.dias_infectado) ** 2)/1000000)*pandemia.mortalidad,1)
        else:
            probabilidad_de_muerte = min(min(0.2, (int(self.dias_infectado) ** 2)/1000000)*pandemia.mortalidad,1)
        if self.vivos > 0:
            muertos = int(self.infectados * probabilidad_de_muerte)
        if self.vivos - muertos < 0:
            muertos = self.vivos

        if self.vivos < 10000:
            muertos = int(self.vivos/3)
            if self.vivos < 100:
                muertos = int(self.vivos)
												               

```
En este código vemos que la probabilidad de muerte se calculo dependiendo de cuanta gente viva quedaba. Si quedan muy pocos se aceleran. (nota: hay una parte del código que es inútil lo sé) De este modo, no pasa que en el caso si quedan 4 vivos, estos jamás mueran. ya que si los vivos son menores a 100 entonces se asesinan a todos los restantes.

### Elementos Faltantes ###
Las siguientes exigencias de la tarea quedaron inconclusas:

 - Promedio de muertes en infecciones: en el momento de que el usuario exige ver las tasas de muertes e infecciones, estas no se calcularon. ( se me olvidó : / )
 - La estructura de datos "ListaLigada" definida en el módulo Estructuras.py , no tiene definido el método __iter__(). No sabía si era necesario hacerlo ya que definiendo el método __getitem()__ ya es posible iterar sobre los elementos de la lista. 

### Otros detalles ###
El juego no es my dinámico. Sucede que con las probabilidades dadas el juego no es muy dinámico. Puede ser que los paises cierren sus fronteras muy rápidamente dejando la enfermedad encerrada en un solo país, sin que esta pueda ser propagada.

Gran parte de lo implementado como ListaLigada fue basado en lo hecho en ayudantía, debido a esto es posible que el código presente similitudes.
