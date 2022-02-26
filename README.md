# TFG
Repositorio para ir subiendo todos los avances respecto a mi Tfg que vaya realizando

# Bitácora

* 13/11/21  
    - He montado la Raspberry
    - He comprobado que funcionen los pines creando un circuito simple de led encendida/apagado.  

* 16/11/21  
    - He instalado miniconda  

* 27/11/21  

    - Sensor LDR:  
	      (- si conectamos GND al pin de resistencia de valor fijo y 3.3V al pin de fotoresistencia, el voltaje aumentara al aumentar la intensidad de luz.  
	      - si conectamos 3.3V al pin de resistencia de valor fijo y GND al pin de la fotoresistencia, el voltaje aumentara en ausencia de luz. )  
	      
        Como lo he hecho yo es cuando hay luz salida a 0, cuando hay oscuridad salida a 1  
	
  - Sensor Humedad:
	      Si está a 1 es seco, si está a 0 húmedo
	
* 5/12/21  

  - Thermistor (NTC Thermistor: 3950 100K ):  
	    The resistance of NTC will decrease as the temperature increases.  
      
      Más adelante descubrí que para que funcione correctamente el thermistor y pueda cambiar de estado, es necesario aplicarle una gran fuente de calor.  


* 21/12/21  
	El entorno que he creado de momento se llama first.  
	
	    source activate first
	    source deactivate  
	
	- Instalado:  
		- numpy  
		- scipy  
		- pandas  
		- matplotlibscikit-learn
		- altair (con conda install -c conda-forge altair)
		
* 28/1/22  
	- Instalación de Ubuntu en la Raspberry.  
  
  - Ha sido necesario debido a que con el sistema operativo anterior (RaspbianOS) no se podía conseguir una versión de Python superior a la 3.6, esto era consecuencia de que la arquitectura utilizada por el antiguo SO era de 32-bit mientras que para poder instalar Python 3.8 o 3.9 era necesario tener una de 64-bit.

* 31/1/22  

    - Instalación miniconda con versión de python 3.9.  
	
		No se ha podido instalar miniconda, sino que ha sido necesario utilizar [miniforge](https://github.com/conda-forge/miniforge) (a través de este [enlace](https://forums.raspberrypi.com/viewtopic.php?t=316338) lo instalé). Con miniconda seguía teniendo el problema de que al instalarlo decía que mi sistema no era de 64 bit(a pesar de tener Ubuntu 21.10) y no me dejaba instalarlo. Sin embargo por medio de miniforge esta instalada la versión 4.11. Una vez instalado he conseguido finalmente crear un entorno llamado myenv con Python 3.9.  
    
   Por la documentacion que he encontrado se debe a que el procesador de la raspberry es de tipo ARM.
	 While the Raspberry Pi includes a 64 bit processor, the RaspbianOS is built on a 32 bit kernel and is not a supported configuration for these installers. We recommend using 64 bit linux distribution such as Ubuntu for Raspberry PI.  
	
	    cd miniforge3/bin/
	    source activate myenv
	    source deactivate  
	 
    O  
	
	    conda activate myenv
	    conda deactivate  
	 
	
	- Instalado:  
		- numpy (dio error al principio y tuve que ejecutar: sudo dpkg --configure -a)
			conda install numpy
		- scipy (conda install scipy)
		- pandas (conda install pandas)
		- matplotlib (conda install matplotlib)
		- altair (conda install altair)
		- scikit-learn (conda install scikit-learn)

* 1/2/22  
	- Dado que la Raspberry se me quedaba pillada simplemente al intentar abrir o cerrar una aplicación y tenía que estar apagandola y encenciendola a lo "bruto" encontré una posible solución que es sustituir en el fichero **/boot/firmware/config.txt** la línea **dtoverlay=vc4-kms-v3d** por **dtoverlay=vc4-fkms-v3d** ([enlace](https://bugs.launchpad.net/ubuntu/+source/linux-raspi/+bug/1946368))  
	- ~~sudo apt install python3-rpi.gpio  (para que no de error hay que ejecutarlo con sudo).~~

* 2/2/22  
	* Sigo sin ser capaz de ejecutar un fichero que tenga import RPi.GPIO, probando:  
	* ~~pip install [lgpio](https://ubuntu.com/tutorials/gpio-on-raspberry-pi#1-overview)~~, error: AttributeError: module 'lgpio' has no attribute 'gpiochip_open'

* 3/2/22
	* He vuelto a intentar instalar con **pip3 install lgpio**  
  	  Ya que por la documentacion del enlace creo que RPi.GPIO no puedo instalarmelo. El problema (por lo que he entendido) es que para poder acceder a los pines (ejecutar gpiochip_open(0)) es necesario ser root, sin embargo al instalarlo (como he dicho antes) y ejecutar **sudo python LDR_data_lgpio.py**, sudo no es "consciente" de que tiene instalado lgpio por lo tanto da error de que no existe ningún módulo lgpio.  
	  Al fichero que intento ejecutar (LDR_data_lgpio.py) le he cambiado de propietario a root:  
	  
	  ```
	     sudo chown root:root LDR_data_lgpio.py
	     sudo chmod u+s LDR_data_lgpio.py
	     sudo chmod g+s LDR_data_lgpio.py
	  ```
	 Y le he puesto un setuid de forma que al ejecutar, ejecute con los permisos del propietario del fichero que es root.  
	 Pero sigo igual, con el mismo error.  
	 
* 4/2/22
	* He estado probando a ejecutar los ficheros haciendo que sean sudo pero que mantenga las variables (el entorno) de myenv, pero no he conseguido nada.
	  He instalado y desinstalado varias veces lgpio de diferentes formas.  
	 
* 5/2/22  
	* He intentado instalar lgpio de otra forma siguiendo este [enlace](http://abyz.me.uk/lg/download.html).  
	  He ejecutado: 
	  
	  ```
	     conda install swig
	     wget http://abyz.me.uk/lg/lg.zip
	     unzip lg.zip
	     cd lg
	     conda install make
	     conda install gcc
	     make
	  ```
	  
	 Con make me saltan muchos errores el último es make: *** [<builtin>: lgGpio.o] Error 1.  
	 He hecho uninstall de todos de estos conda install.

* 6/2/22
	
	* Posible solución a la instalación de Lgpio, pasos que he seguido:  
	
		1.Instalación lgpio: ```sudo apt-get install python3-lgpio```  
		2.Mover ficheros:  
	  
	| File | FROM | TO |
	|------|------|----|
	|lgpio-0.1.0.1.egg-info| /usr/lib/python3/dist-packages/lgpio-0.1.0.1.egg-info | /home/nuria/miniforge3/env/myenv/lib/python3.9/site-packages/lgpio-0.1.0.1.egg-info |  
	| lgpio.py | /usr/lib/python3/dist-packages/lgpio.py | /home/nuria/miniforge3/env/myenv/lib/python3.9/site-packages/lgpio.py |
	| _lgpio.cpython-39-aarch64-linux-gnu.so | /usr/lib/python3/dist-packages/_lgpio.cpython-39-aarch64-linux-gnu.so | /home/nuria/miniforge3/env/myenv/lib/python3.9/site-packages/_lgpio.cpython-39-aarch64-linux-gnu.so |
	| lgpio.cpython-39.pyc | /usr/lib/python3/dist-packages/__pycache__/lgpio.cpython-39.pyc | /home/nuria/miniforge3/env/myenv/lib/python3.9/site-packages/__pycache__/lgpio.cpython-39.pyc |
	| liblgpio1 | /usr/share/doc/liblgpio1 | /home/nuria/miniforge3/env/myenv/share/doc/liblgpio1 |
	| python3-lgpio | /usr/share/doc/python3-lgpio | /home/nuria/miniforge3/env/myenv/share/doc/python3-lgpio |

	Los últimos dos "movimientos" creo que no son necesarios.  

	Ahora, para poder ejecutar el fichero que quiera utilizar lgpio hay que ejecutar:  
		```
		sudo env "PATH=$PATH" python file.py
		```

	3.Una vez copiados todos los ficheros necesarios desinstalo python3-lgpio: ```sudo apt remove python3-lgpio```  
	
	* He creado un primer programa (commit: first csv generator) que lee los datos proporcionados por el LDR y cuando tenga 100 muestras genera un csv con ellas.  

* 9/2/22
	* He probado (por si acaso) a instalar lgpio con pip3 install lgpio y luego ejecutar el .py con el comando de antes (sudo env ....) pero no va dice que lgpio has no attribute 'gpiochip_open'  
	* He añadido al Latex el paquete comment, \usepackage{comment}. He comentado unas figuras en la seccion de arquitectura general.
* 11/2/22
	* Reunión con tutores.
	* Crear un nuevo entorno virtual llamado **occupancy** con Python 3.9.
	* ``` 
		conda install scikit-learn  
		conda install pandas  
		conda install matplotlib    
	* Tengo que crear tres modelos:
		- Regresión Logistica.
		- Máquinas de soporte vectorial.
		- Gradient tree boosting.
	* **Primer modelo de regresion logística, tiene un porcentaje de Accuracy: más del 98%, Precision: 95-96%, Recall: 99%, en unos 4-5 segundos.**

* 12/2/22
	* Accuracy= (True positive + True Negative)/(True positive+ True Negative + False Positive + False Negative), porcentaje de aciertos.  
	* Precision= (True positive)/(True positive + False positive), los verdaderos positivos entre todos los positivos que ha asignado, cuanto más alto el porcentaje mejor porque significa que False positive es practicamente 0.  
	* Recall= (True positives)/(True positive + False negative) los verdaderos positivos entre los positivos que ha asignado más los que son positivos y ha pusto como negativos.
	
	* **Primer modelo de máquina de soporte vectorial, con un porcentaje de Accuracy (en los datos de test): más del 97%, Precision: 95-96%, Recall: 99%, en unos 5 segundos.**  
		Con el counter que aparece en este código se puede comprobar que el stratify lo esté haciendo bien (el numero de cada elemento sea el correcto por  ejemplo se de 1 hay 100 ejemplos y queremos que el 70% de los datos totales sean de entrenamiento, el stratify debería de hacer que hubiese (100*70%)/100% (regla de tres).  
		El random_state sirve para que siempre salgan en el mismo orden los valores (se mezclan pero siempre en el mismo orden).  
		
		He comprobado que al hacerlo sin el stratify tambien consigue porcentajes muy buenos (del estílo anterior) ya que consigue (más o menos) la misma proporcion de 0 y 1 que usando el stratify. Los 0 rondan los 11000 y los 1 los 3300 (en cantidad, es decir hay 3300 unos y 11000 ceros).  
	
	* Gradient tree boosting ~= Árboles de decisión  
	
	* **Primer modelo con Gradient tree boosting, con Accuracy: más del 98%, Precision: 96%, Recall: 99% en unos 7 (casi ocho) segundos.**
		
	* Nuevo entorno virtual **jupiter**  
		```
		conda install ipython  
		conda install jupyter  
		conda install jupyterlab
		conda install numpy  
		conda install scipy  
		conda install matplotlib  
		conda install pandas  
		conda install scikit-learn  
		```  
	
	Ctr+Enter para hacer run de todas las cells.  
	Insertar una nueva celda debajo Esc+b.  
	
	* Ejecutando el código de regresión logística en Jupyter Notebook el tiempo total es de 1.38s y mismos porcentajes.  
	* Ejecutando el código de máquinas de soporte vectorial en Jupyter Notebook el tiempo total es de 2s y mismos porcentajes.  
	* Ejecutando el código de Gradient tree boosting en Jupyter Notebook el tiempo total es de casi 4s y mismos porcentajes. 
	* ¿He hecho algo mal? Haciendo que el test size sea muy grande y quitando el stratify, sigue dando valores de accuracy muy altos (por encima del 98%). Haciendo también el cross validation da accuracy muy altos.
	
* 13/2/22  
	* Si stratify está a None (no se asigna nada) utiliza stratify fashion que entiendo que es un stratified k-fold, porque en la [documentación](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html) te lleva a [esa página](https://scikit-learn.org/stable/modules/cross_validation.html#stratification). Por eso siempre salen más o menos los mismos porcentajes porque stratified k-fold hace que aproximadamente se mantengan en proporcion los mismos porcentajes de ejemplos de cada clase.  
	* En regresión logistica aún con un train size muy pequeño (0.001 que son 20 ejemplos) la accuracy sigue siendo del 90%.Y con 0.0005, que son 10 ejemplos la accuracy baja a más o menos el 85% (aun que todavía hay veces que está por encima del 90%).  
	* He hecho cross validation y sigue teniendo porcentajes altos de accuracy (superiores al 90%)
	
* 22/2/22
	* He cambiado la validación cruzada de StratifiedKFold a KFold directamente. Obteniendo igualmente muy buenos resultados Regresión tarda unos 1 segundo (wall time, si miramos CPU son unos 4 segundos), SVM 6-7 segundos y gradient tree boosting 16 segundos.  
	* El tiempo en Jupyter notebook que interesa es el Wall time que muestra el verdadero tiempo que ha pasado para ejecutar esa cell.  
	* En el enviroment **jupiter** he instalado stressberry:  
		```
		sudo apt install stress  
		pip3 install stressberry --user  
		sudo apt update  
		sudo apt upgrade  
		sudo usermod -aG video <username>  
		Hacer logout  
		```
	[Ejecutar](https://peakd.com/hive-163521/@themarkymark/how-to-stress-test-your-raspberry-pi) con: /home/nuria/.local/bin/stressberry-run -d {tiempo en segundos estresada} -i {segundos idle} -c {numero de cpus a estresar} name.out  
	La Raspberry tiene 4 Cpus. ¿Hacer tres niveles comenzando estresando una (nivel bajo), medio (estresando 2) y alto estresando las 4?  
	En **mi portátil blanco** descomento en .bashrc desde  
		__conda_setup="$('/home/nuriadj/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"  
	hasta  
		unset __conda_setup  
	
	Crear un nuevo enviroment llamado tfg
		```
		conda create --name tfg python=3.9
		```
	Instalo:  
	```
		conda install ipython  
		conda install jupyter  
		conda install jupyterlab
		conda install numpy  
		conda install scipy  
		conda install matplotlib  
		conda install pandas  
		conda install scikit-learn  
	```  
		
	* Stressberry 1 cpu:  
		- regression (stress= 300, idling= 150) cross: 22 segundos  
		- SVM (stress= 300, idling= 150) cross: 6 segundos  
		- gradient tree boosting (stress= 300, idling= 150) cross: 16 segundos  
	
	* Stressberry 2 cpu:  
		- regression (stress= 300, idling= 150) cross: 20 segundos  
		- SVM (stress= 300, idling= 150) cross: 6 segundos  
		- gradient tree boosting (stress= 300, idling= 150) cross: 15 segundos  
	
	* Stressberry 4 cpu:  
		- regression (stress= 300, idling= 150) cross: 15 segundos.
		- SVM (stress= 300, idling= 150) cross: 6 segundos  
		- gradient tree boosting (stress= 300, idling= 150) cross: 16 segundos  
* 23/2/22
	
	* Pruebas bajo condiciones normales en mi portátil:  
		- Regression tarda 711 milisegundos - 1 segundo (mismos valores de Accuracy, Precision, Recall más o menos) Wall time unos 200 ms.  
		- SVM tarda 1.7 segundos (mismos valores) Wall time= 1.6 seg.  
		- Gradient tree boosting unos 5 segundos, Wall time unos 5 segundos.  
	* He vuelto a hacer pruebas con stressberry, esta vez para stress=120 e idling= 60. En el caso de regression he obtenido resultados muy similares.  
	Para SVM igual, en todos los casos el tiempo que atarda es casi siempre 6 segundos.  
	Para Gradient tree boosting (para una, dos y cuatro cpu se queda todo el rato en 15 segundos mas o menos).
	
* 24/2/22
	* Instalado git en la Raspberry con ```sudo apt install git```  
	
	* He estado probando tambien con stress= 900 e idle= 150
	
	En Raspberry (total CPU time) con Jupyter-notebook:
	
	| Modelo | Idle | Bajo | Medio | Alto |
	|--------|------|------|-------|------|
	|Regresión logística| 5 seg | 22 seg | 20 seg | 15 seg|
	|SVM | 5 seg | 6 seg | 6 seg | 6 seg|
	|Gradient tree boosting | 16 seg | 16 seg | 15 seg | 16 seg|  
	
	* Wall time is the actual amount of time taken to perform a job  
	
	En Raspberry (Wall time):  
	
	| Modelo | Idle | Bajo | Medio | Alto |
	|--------|------|------|-------|------|
	|Regresión logística| 1 seg | 8 seg | 10 seg | 7 seg|
	|SVM | 6 seg | 6 seg | 6 seg | 6 seg|
	|Gradient tree boosting | 16 seg | 16 seg | 15 seg | 16 seg| 
	
	* Wall time Regresion, idle = 1 seg, 1 cpu= 8 seg, 2 cpu= 10 seg, 4 cpu= 7 seg.  
	  Wall time SVM, idle= 6 seg, 1 cpu= 6 seg, 2 cpu= 6 seg, 4 cpu= 6 seg.  
	  Wall time Gradient tree, idle= 16 seg, 1 cpu= 16 seg , 2 cpu= 16 seg , 4 cpu= 15 seg.
	
* 25/2/22
	
	* Pruebas stressberry sin usar Jupyter-notebook (desde el entorno ocuppancy) stress 300 idle 150:
		- 1 CPU  
			Regresión real 13 seg, user 30 seg  
			SVM real 10 seg, user 9 seg  
			Gradient tree real 19 seg, user 18 seg  
		
		- 2 CPU  
			Regresión real 14 seg, user 25 seg  
			SVM real 10 seg, user 9 seg  
			Gradient tree real 19 seg, user 18 seg  
		
		- 4 CPU  
	
	Desordenando las ejecuciones (punto 1 reunión 23/2/22)  
	
	CROSS VALIDATION **Raspberry**:  
	
	**CPU time**:  
	
	| Modelo | Idle | Bajo | Medio | Alto |
	|--------|------|------|-------|------|
	|Regresión logística| 5 seg | 22 seg | 20 seg | 12 seg|
	|SVM | 5 seg | 6 seg | 6 seg | 6 seg|
	|Gradient tree boosting | 16 seg | 15 seg | 15 seg | 15.5 seg|  
	
	**Wall time**  
	
	| Modelo | Idle | Bajo | Medio | Alto |
	|--------|------|------|-------|------|
	|Regresión logística| 1 seg | 8 seg | 10 seg | 7 seg|
	|SVM | 6 seg | 6 seg | 6 seg | 6 seg|
	|Gradient tree boosting | 16 seg | 16 seg | 15 seg | 16 seg|  
	
	**Instalo en mi portátil stress**
		```
		sudo apt install stress  
		```  
	
	CROSS VALIDATION **Portátil**:  
	
	**CPU time**  
	
	| Modelo | Idle | Bajo | Medio | Alto |
	|--------|------|------|-------|------|
	|Regresión logística| 700 ms | 700 ms | 900 ms | 1 seg|
	|SVM | 1.5 seg | 1.6 seg | 1.8 seg | 3-5 seg|
	|Gradient tree boosting | 5 seg | 5 seg | 6 seg | 10 seg|
	
	**Wall time**  
	
	| Modelo | Idle | Bajo | Medio | Alto |
	|--------|------|------|-------|------|
	|Regresión logística| 180 ms | 180 ms | 200 ms | 320 ms|
	|SVM | 1.5 seg | 1.6 seg | 1.8 seg | 3-5 seg|
	|Gradient tree boosting | 5 seg | 5 seg | 6 seg | 10 seg|
	
	
	Wall time:
		Regresión idle 180 ms, 1 cpu 180 ms, 2 cpu 200 ms, 4 cpu 320 ms
		SVM idle 1.5 seg, 1 cpu 1.6 seg, 2 cpu 1.8 seg, 4 cpu 3-5 seg
		Gradient tree idle 5 seg, 1 cpu 5 seg, 2 cpu 5 seg, 4 cpu 10 seg
		Random forest idle 750 ms, 1 cpu 800 ms, 2 cpu 1 seg, 4 cpu 1.9 seg
	
	* He generado el modelo de Random forest directamente sin validación cruzada.
	
* 26/2/22  
	
	SIN CROSS VALIDATION **Raspberry**:  
	
	**CPU time**  
	
	| Modelo | Idle | Bajo | Medio | Alto |
	|--------|------|------|-------|------|
	|Regresión logística|  1 seg | 4 seg | 4 seg | 3 seg |
	|SVM | 1.9 seg | 2 seg | 2 seg | 2 seg |
	|Gradient tree boosting | 4 seg | 4 seg | 4 seg | 4 seg |
	|Random forest | 3 seg | 3 seg | 3 seg | 3 seg|  
	
	**Wall time**  
	
	| Modelo | Idle | Bajo | Medio | Alto |
	|--------|------|------|-------|------|
	|Regresión logística| 300 ms  | 2 seg | 2 seg | 1.6 seg |
	|SVM | 1.9 seg | 2 seg | 2 seg | 2 seg |
	|Gradient tree boosting | 4 seg | 4 seg | 4 seg | 4 seg |
	|Random forest | 3 seg | 3 seg | 3 seg | 3 seg |  
	
	Regresion 1 cpu= 4 seg (cpu) 2 seg (wall time)  
	
	SIN CROSS VALIDATION **Portátil**:  
	
	**CPU time**  
	
	| Modelo | Idle | Bajo | Medio | Alto |
	|--------|------|------|-------|------|
	|Regresión logística| 130 ms | 160 ms | 180 ms | 280 ms |
	|SVM | 570 ms | 600 ms | 830 ms  | 1.6 seg |
	|Gradient tree boosting | 1.2 seg | 1.3 seg | 1.8 seg | 3 seg |
	|Random forest | 750 ms | 800 ms | 1 seg | 1.9 seg|  
	
	**Wall time**  
	
	| Modelo | Idle | Bajo | Medio | Alto |
	|--------|------|------|-------|------|
	|Regresión logística| 30 ms | 50 ms | 55 ms | 80 ms |
	|SVM | 570 ms | 600 ms | 830 ms | 1.6 seg |
	|Gradient tree boosting | 1.2 seg | 1.3 seg | 1.8 seg | 3 seg |
	| Random forest | 750 ms | 800 ms | 1 seg | 1.9 seg |  
	
	**Logistic regresion** (Cpu time//Wall time), en principio no tiene efecto segun la pregunta de [stack overflow](https://stackoverflow.com/questions/51318367/scikit-learn-multithreading) pero he querido comprobarlo, y parece que algo de efecto si que tiene.
	
	| N_JOBS | Idle | Bajo | Medio | Alto |
	|--------|------|------|-------|------|
	| 1 | 1 seg // 350 ms | 4 seg // 2 seg | 3.7 seg // 2 seg | 3.5 seg // 1.5 seg |
	| 2 | 70 ms // 250 ms | 50 ms // 250 ms | 35 ms // 350 ms | 50 ms // 500 ms |
	| 3 | 50 ms // 260 ms | 60 ms // 270 ms |  50 ms // 300 ms | 40 ms // 300 ms |
	| 4 | 50 ms // 250 ms | 50 ms // 200 ms | 50 ms // 300 ms |  40 ms // 300 ms |
	
	1 cpu, 2 cpu muy variables (en general todos) (n_jpb= 4)
	
	**Random forest** (Cpu time // **Wall time**)  
	
	| N_JOBS | Idle | Bajo | Medio | Alto |
	|--------|------|------|-------|------|
	| 1 | 3 seg // **3 seg** | 3 seg // **3 seg** | 3 seg // **3 seg** | 3 seg // **3 seg** |
	| 2 | 3.5 seg // **2 seg** | 3.5 seg // **2 seg** | 3.4 seg // **2.4 seg** | 3.3 seg // **2.6 seg** |
	| 3 | 4 seg // **1.6 seg** | 4 seg // **2 seg** | 3.3 seg // **2 seg** | 3.5 seg // **3 seg** |
	| 4 | 4.3 seg // **1.5 seg** | 4 seg // **2 seg** | 3.4 seg // **2 seg** | 3.4 seg // **3 seg** |  
	
# **TO DO Memoria:**  
	
**Para guardar la memoria en git:**  
- Guardo el zip  
- Descomprimo zip  
- Descargo el pdf y lo guardo dentro de la carpeta generada por el zip  

Repasar estado del arte: Miniconda poner algo sobre que ofrece un mayor control sobre el entorno en el que se desarrolla el programa, respecto a los paquetes que se instalan. Además permite "compartir" el entorno de forma que se puede replicar ese enotorno virtual en otra máquina.  
~~Cambiar Miniconda!!! es **Miniforge3** !!~~  
~~¿Por qué lgpio?~~  
Pasar el desarrollo de los problemas de de instalación (miniconda, RPi.GPIO...) Al Anexo.  
Estado del arte meter las librerías de scikit-learn, pandas, jupyter-notebook?  
Comentar en la memoria que dado que es un gran número de ejemplos no es necesario utilizar stratified a pesar de que haya menor número de muestras en una clase que en otra. Mirar otra vez como he explicado lo de validación cruzada.
	
(Sobre la estratificación: Un aspecto importante a destacar de este set de datos es que hay una mayor cantidad de ejemplos de habitación no ocupada que de ocupada. En otros sets de datos esto podría representar un problema ya que puede dar lugar a que al realizar esta división de forma aleatoria, el conjunto de datos de entrenamiento apenas tenga ejemplos de una de las clases. Sin embargo al tener una gran cantidad de ejemplos en el que ambas clases tienen una gran cantidad de muestras, como es este caso, una división aleatoria no representa ningún inconveniente dado que el set de entrenamiento siempre tendrá la cantidad de muestras necesarias de ambas clases para entrenar correctamente. )
