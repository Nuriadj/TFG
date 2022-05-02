# TFG
Repositorio para ir subiendo todos los avances respecto a mi Tfg que vaya realizando  

[DataSets de clasificación](https://epistasislab.github.io/pmlb/), seleccionar task con clasificacion. Pinchar 2 veces en las flechitas junto al título de la columna n_observations salen lo más grandes ordenados de mayor a menor.

# Bitácora  

## Noviembre

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
	      
## Diciembre	      
	
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


## Enero
		
* 28/1/22  
	- [Instalación de Ubuntu en la Raspberry](https://ubuntu.com/tutorials/how-to-install-ubuntu-desktop-on-raspberry-pi-4). Pasos del 1 al 3.  
  
  	 Ha sido necesario debido a que con el sistema operativo anterior (RaspbianOS) no se podía conseguir una versión de Python superior a la 3.6, esto era consecuencia de que la arquitectura utilizada por el antiguo SO era de 32-bit mientras que para poder instalar Python 3.8 o 3.9 era necesario tener una de 64-bit.  
	 
	 - El otro problema que tuve es que no sé por qué razón el teclado no me dejaba escribir en el terminal ni en ninguna otra aplicación, solo me dejaba escribir para hacer log in. Por medio de una pregunta en el foro de Raspberry pude solucionarlo, os adjunto el enlace a la página con la solución https://forums.raspberrypi.com/viewtopic.php?t=310293 (el penúltimo post es el que seguí).
 

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


## Febrero

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
	|SVM | 6 seg | 6 seg | 6 seg | 6 seg|
	|Gradient tree boosting | 16 seg | 15 seg | 15 seg | 15.5 seg|
	|Random forest | 12 seg | 12.3 seg | 12 seg | 12 seg |
	
	**Wall time**  
	
	| Modelo | Idle | Bajo | Medio | Alto |
	|--------|------|------|-------|------|
	|Regresión logística| 1 seg | 8 seg | 10 seg | 7 seg|
	|SVM | 6 seg | 6 seg | 6 seg | 6 seg|
	|Gradient tree boosting | 16 seg | 16 seg | 15 seg | 16 seg|
	|Random forest | 12 seg | 12.3 seg | 12 seg | 12 seg |
	
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
	|Random forest | 3.4 seg | 3.3 seg | 5 seg | 8 seg |
	
	**Wall time**  
	
	| Modelo | Idle | Bajo | Medio | Alto |
	|--------|------|------|-------|------|
	|Regresión logística| 180 ms | 180 ms | 200 ms | 320 ms|
	|SVM | 1.5 seg | 1.6 seg | 1.8 seg | 3-5 seg|
	|Gradient tree boosting | 5 seg | 5 seg | 6 seg | 10 seg|
	|Random forest| 3.4 seg | 3.3 seg | 5 seg | 8 seg |
	
	
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
	
	1 cpu, 2 cpu muy variables (en general todos) (n_job= 4)
	
	[n_jobs](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html), el número de trabajos que se ejecutan en paralelo. Con n_jobs= 1 solo dejamos a una cpu trabajar, con n_jobs= 4 se utilizan 4 cpus. 
	
	**Random forest** Raspberry (Cpu time // **Wall time**)  
	
	| N_JOBS | Idle | Bajo | Medio | Alto |
	|--------|------|------|-------|------|
	| 1 | 3 seg // **3 seg** | 3 seg // **3 seg** | 3 seg // **3 seg** | 3 seg // **3 seg** |
	| 2 | 3.5 seg // **2 seg** | 3.5 seg // **2 seg** | 3.4 seg // **2.4 seg** | 3.3 seg // **2.6 seg** |
	| 3 | 4 seg // **1.6 seg** | 4 seg // **2 seg** | 3.3 seg // **2 seg** | 3.5 seg // **3 seg** |
	| 4 | 4.3 seg // **1.5 seg** | 4 seg // **2 seg** | 3.4 seg // **2 seg** | 3.4 seg // **3 seg** |  
	
	**Random forest** Portátil (Cpu time // **Wall time**) 
	| N_JOBS | Idle | Bajo | Medio | Alto |
	|--------|------|------|-------|------|
	| 1 | 750 ms // **750 ms** | 770 ms // **770 ms** | 800 ms // **800 ms** | 1.2 seg // **1.2 seg** |
	| 2 | 850 ms // **450 ms** | 850 ms // **460 ms** | 900 ms // **550 ms**  | 2 seg // **1 seg** |
	| 3 | 950 ms // **350 ms** | 1 seg // **350 ms** | 1.4 seg // **540 ms** | 2 seg // **800 ms** |
	| 4 |  1 seg // **310 ms** | 1 seg // **330 ms** | 1.5 seg // **515 ms** | 2 seg // **650 ms** |  
	
	- Con mayor número de n_jobs wall time disminuye mientras que el de cpu aumenta.
	
	* En la Raspberry he probado a utilizar en vez de stressberry usar stress pero por lo menos para regresión logística pasa lo mismo.  

## Marzo	
	
* 1/3/22  
	
	* Pruebo a instalar stress-ng:  
		```
		sudo snap install stress-ng  
		```
	Consigo los mismos resultados, lo borro:  
		```
		sudo snap remove stress-ng  
		```
	
	* Hoy la Raspberry esta mucho más lenta, por ejemplo ejecutar cross validation sin estresar ninguna cpu de gradient tree le ha costado 32 segundos, regresión lineal 8 seg. Apagandola y encendiendola parece que ha vuelto a la normalidad.  
	
	* Probar a instalar s-tui  
		```
		sudo apt install s-tui  
		```
	Obtengo los mismos resultados  
		```
		sudo apt remove s-tui  
		```  
* 3/3/22  
	He vuelto a instalar stress-ng de otra forma  
	```
	sudo apt install stress-ng  
	```  
	Ejecutando:  
	```
	stress-ng --cpu 4 --cpu-method fft --timeout 60s 
	```  
	Con esto el gradient tree con 4 cpus incrementa un poco el tiempo a 18 seg. Sin embargo para el resto como regresión lineal no consigue ningún cambio.  
	- [x] (Hecho) ~~(Tengo que desinstalar stress-ng, ya que no ha servido para no tenerlo instalado inecesariamente).~~  
	
* 4/3/22  
	Como ejecutaba antes stressberry:  
		```
		/home/nuria/.local/bin/stressberry-run -n "My Test" -d 1800 -i 300 -c 4 mytest.out
		```  
	Ahora lo estoy ejecutando desde dentro del entorno virtual jupiter con:  
		```
		stressberry-run -d 60 -i 30 -c 4 mytest.out
		```  
	Pero sigo obteniendo los mismos resultados.  
	
* 8/3/22  
	He probado ha abrir en firefox varias pestañas (6 en total) que estén reproduciendo vídeos (de música todos ellos). Con todos los vídeos en play el tiempo de ejecución para gradient tree boosting con cross validation es de 21 seg, (con 8 pestañas es de 22 seg). Con 8 pestañas de vídeos abiertas regresión logistica con validación cruzada tarda 9 segundos. Random forest con cross validation tarda 17 seg.  
	Esta es la única forma (de momento) que en la Raspberry haya conseguido aumentar el tiempo de ejecución.  
	
* 9/3/22  
	- Instalo htop utilizando ```sudo apt install htop```
	- He tenido que hacer ```sudo apt install firefox``` ya que la otra que tenia de antes no habia forma de que fuese. Para ejecutar ahora firefox pongo en el terminal ```firefox```    
	- Ejecuto ```stress -c 4 --timeout 60s``` mismos resultados cuando en htop se puede ver claramente que las cpus están al 100%  
	
* 10/3/22  
	- Me he fijado que al ejecutar stress en la Raspberry observando los datos que aporta htop, si nos fijamos en la columna de cpu (no las barritas horizontales), se puede ver que al ejecutar stress los procesos de stress se encuentran con cpu prácticamente al 100% peor cuando ejecuto uno de los modelos, los porcentajes de stress en la columna de cpu decrecen, siendo el proceso que ejecuta el modelo el que se encuentra al 100%.
	Esto en el portátil no pasa cuando se estresan los porcesos de stress se mantienen al 100% independientemente de que se ejecute un modelo de aprendizaje o no. Esto estresando 4 cpus en Raspberry y portatil.  
	
	Si solo estreso dos cpus tanto los stress como el algorito se mantienen al 100% en la columna de cpu.  
	
* 12/2/22  
	
	- Volviendo a hacer pruebas:  
	
	CROSS VALIDATION **Portátil**:  
	
	**CPU time**  
	
	| Modelo | Idle | 1 cpu | 2 cpu | 4 cpu | 6 cpus | 8 cpus |
	|--------|------|------|-------|------|--------|--------|
	|Regresión logística| 550 ms | 800 ms | 1 seg | 1.5 seg| 2-2.5 seg| 3.5 seg |
	|SVM | 1.5 seg | 1.7 seg | 2.6 seg | 5 seg| 5 seg | 5 seg |
	|Gradient tree boosting | 5 seg | 5 seg | 7.6 seg | 12 seg| 12.5 seg | 12.5 seg |
	|Random forest | 3 seg | 4 seg | 5 seg | 8 seg | 8.3 seg | 8.4 seg |
	
	Con esto lo único que saco es que tiene un comportamiento parecido a la Raspberry, lo único que como tiene 8 cpus se nota menos. Al principio la subida de tiempos es notable pero a partir de 4 cpus estresadas se estancan bastante los tiempos.
	
* 19/3/22
	
	- Nuevo [dataSet](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_kddcup99.html#sklearn.datasets.fetch_kddcup99). La Raspberry está teniendo problemas para descargarselo, se ha quedado pillada. Voy a probar primero con el 10% y una vez que sepa descargarlo, leerlo y tratarlo pruebo con el total.  
	No estoy siendo capaz de descargar el dataset, no se descargan csv se descargan ficheros binarios. Como no soy capaz de descargarla usando scikitlearn la voy a coger de [aqui](http://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html), una vez descargado el archivo hay que descomprimirlo (gzip -d file).  
	Con el 10% todo bien, he podido convertirlo en binario (código de [Download_dataSet](https://github.com/Nuriadj/TFG/blob/main/kdd_cup99/Download_dataSet.ipynb)). Para convertirlo en binario mire [aquí](https://github.com/uptodiff/kdd-cup-99-Analysis-machine-learning-python/blob/master/kdd_binary_classification_naive_bayes.py)   
	Con el 100% no he podido pasarlo a clasificación binaria, la propia Raspberry se queda un rato pillada y luego ella sola lo mata. He probado a ejecutarlo en el teminal (porque con notebook después de un rato pillada perdia la conexión con el kernel) pero después de estar pillada un rato aparece un mensaje de Killed y temina la ejecución. De momento haré las pruebas solo con el 10%.  
	
	- De ese 10% voy a utilizar el 70% para entrenar y 30% para validar. En la primera fila hay columnas que tienen valores extraños como 0.00.1 por lo que para quitarlo elimino la primera fila. Y quitar la primera columna que es el índice. He hecho que el csv que se guarda no contenga ni la cabecera ni el indice (primera fila y primera columna) ya está preparado para directamente utilizarlo. Esto se hace también en [Download_dataSet](https://github.com/Nuriadj/TFG/blob/main/kdd_cup99/Download_dataSet.ipynb)  
 
	- Quito la columna 19 y 20 porque contienen todo el rato el mismo valor (en ambos casos el cero). Se pone axis= 1 para indicar que se quiere eliminar la columna 19 (no la fila) e inplace se pone a true para que la variable dataset sea "actualizada". Transformo los datos categoricos (strings a otro valor, o eso he entendido) y se quitan las filas que se repiten.   
	
	- Para hacer todo el tratamiento del dataSet he utilizado de referencia el siguiente [enlace](https://github.com/timeamagyar/kdd-cup-99-python/blob/master/kdd%20preprocessing.ipynb).  
	
	- A la hora de entrenar el modelo da error, no converge las iteraciones llegan al máximo. He intentado [escalar los datos de entrenamiento](https://scikit-learn.org/stable/modules/preprocessing.html), pero con el ejemplo que ponen no es suficiente. Luego a parte de scalarlo aumento el máximo número de iteraciones a 400 (por defecto el máximo número de iteraciones es 100), he elegido ese número porque es el valor más bajo para el que he conseguido que converja el modelo en una solución **siempre**.  
	
	- Ahora ya no solo tengo que mirar el tiempo que tarda el entrenamiento, ya que hay otras celdas que tambíen tardan varios segundos.  
	
	- Recall y precision lo calculo repecto a la salida: normal.  
	
* 20/3/22  
	
	- Voy a utilizar el time de linux para ver los tiempos (en vez de jupyter-notebook) porque ya son varias celdas en las que hay que mirar el tiempo y es más cómodo así. [Real= wall time, user= cpu times user, sys= cpu times sys](https://blog.gceasy.io/2016/04/06/gc-logging-user-sys-real-which-time-to-use/). El tiempo total de cpu es la suma de user y sys.  
	
	- Máquinas de soporte vectorial por defecto tiene un max limit -1, es decir no tiene limite.  
	
	DataSet: **10% Kdd_cup99** Dispositivo: **Raspberry** **SIN CROSS VAL** **(CPU)**  
	
	| Modelo | Idle | 1 cpu | 2 cpu | 4 cpu |
	|--------|------|------|-------|------|
	|Regresión logística| 64 seg | 74 seg | 70 seg | 64 seg |
	|SVM | 77 seg | 76 seg | 76 seg | 77 seg | 
	|Gradient tree boosting | 116 seg | 115 seg | 115 seg | 115 seg | 
	|Random forest | 61 seg | 60 seg | 60 seg | 60 seg |  
	
	DataSet: **10% Kdd_cup99** Dispositivo: **Raspberry** **SIN CROSS VAL** **(WALL TIME)**
	
	| Modelo | Idle | 1 cpu | 2 cpu | 4 cpu |
	|--------|------|------|-------|------|
	|Regresión logística| 31 seg | 39 seg | 44 seg | 43 seg |
	|SVM | 78 seg | 76 seg | 76 seg | 77 seg | 
	|Gradient tree boosting | 116 seg | 115 seg | 115 seg | 115 seg | 
	|Random forest | 61 seg | 60 seg | 60 seg | 60 seg |  
	
* 22/3/22  
	
	DataSet: **10% Kdd_cup99** Dispositivo: **Portátil** **SIN CROSS VAL** **(CPU)**  
	
	| Modelo | Idle | 1 cpu | 2 cpu | 4 cpu |
	|--------|------|------|-------|------|
	|Regresión logística| 11 seg | 13 seg | 16 seg | 23 seg |
	|SVM | 15 seg | 19 seg | 24 seg | 45 seg | 
	|Gradient tree boosting | 22 seg | 26 seg | 39 seg | 53 seg | 
	|Random forest | 9 seg | 11 seg | 13 seg | 24 seg |  
	
	DataSet: **10% Kdd_cup99** Dispositivo: **Portátil** **SIN CROSS VAL** **(WALL TIME)**
	
	| Modelo | Idle | 1 cpu | 2 cpu | 4 cpu |
	|--------|------|------|-------|------|
	|Regresión logística| 5 seg | 6 seg | 8 seg | 13 seg |
	|SVM | 15 seg | 19 seg | 24 seg | 46 seg | 
	|Gradient tree boosting | 22 seg | 26 seg | 39 seg | 53 seg | 
	|Random forest | 9 seg | 11 seg | 13 seg | 24 seg |  
	
* 23/3/22
	
	- Observar valor de la RAM para los diferentes modelos en diferentes niveles de estrés. Con el **10%** de datos de kdd y entrenando con el 70% de los mismos:  
	
	DataSet: **10% Kdd_cup99** Dispositivo: **Raspberry** **SIN CROSS VAL** **(Max RAM)**  
	
	| Modelo | Idle | 1 cpu | 2 cpu | 4 cpu |
	|--------|------|------|-------|------|
	|Regresión logística| 1.37G | 1.38G | 1.46G | 1.50G |
	|SVM | 1.42G | 1.42G | 1.42G | 1.42G | 
	|Gradient tree boosting | 1.24G | 1.37G | 1.42G | 1.51G | 
	|Random forest | 1.34G | 1.37G | 1.38G | 1.38G |   
	
	- En regresión logística es verdad que con 4 cpus he llegado a ver ese valor, pero tras hacer varias ejecuciones lo normal es que no pase de los 1.37G más o menos. Con dos cpus igual, he visto ese valor pero tras varias ejecuciones no da valores tan altos (depende hay veces que se queda sobre los 1.3G y otras veces que aumenta incluso más que ese valor.
	Eso si, cuando están todas las cpus al 100% (lo que comento en el siguiente punto (*)) la Mem se queda en 1.25G practicamente siempre (independientemente del número de cpus estresadas).
	
	- Una cosa que estoy viendo es que en regresión logśitica en idle al principio solo una cpu se pone al 100%, pero pasado unos intantes (y habiendo bajado un poco el valor de Mem) (*)las cuatro cpus se ponen al 100%. Estresando solo una, dos  cpu pasa igual, al principio solo están dos al 100% y pasado un rato se ponen todas al 100% hasta que finaliza la ejecución.
	Con SVM NO pasa.
	
	- Otra cosa que creo que antes no pasaba es que hay veces que el valor del porcentaje de las cpu se ponen algunos en color rojo uando llegan a valores más grandes (mas del 90%).  
	
	- Gradient tree boosting se mantiene practicamente todo el rato en 1.24G, es verdad que momentaneamente hay más RAM ocupada (las que se ven en la tabla), pero prácticamente todo el rato se queda en 1.24G.  
	Lo mismo pasa con random forest, llega a alcanzar valores más altos pero se mantiene todo el rato prácticamente en 1.22G. Se pone a 1.25G cuando hay 1, 2 o 4 cpus estresadas.  
	
* 24/3/22  
	
	El fichero kdd_cup_10_perBinary.csv contiene un total de **494020** líneas.  
	
	| Modelo | Idle | 1 cpu | 2 cpu | 4 cpu |
	|--------|------|------|-------|------|
	|Regresión logística| | | | |
	|SVM | | | | | 
	|Gradient tree boosting | | | | | 
	|Random forest | | | | |  
	
	
	DataSet: El 10% de **10% Kdd_cup99** 
	Dispositivo: **Raspberry** **SIN CROSS VAL** **(CPU // WALL TIME)**  
	
	| Modelo | Idle | 1 cpu | 2 cpu | 4 cpu |
	|--------|------|------|-------|------|
	|Regresión logística| 15 seg // **12 seg** | 26 seg // **16 seg** | 25 seg // **18 seg** | 22 seg // **17 seg** |
	|SVM | 13 seg // **13 seg** | 13 seg // **13 seg** | 13 seg // **13 seg** | 13 seg // **13 seg** | 
	|Gradient tree boosting | 20 seg // **20 seg**| 21 seg // **21 seg** | 20 seg // **20 seg** | 20 seg // **21 seg** | 
	|Random forest | 14 seg // **14 seg**| 14 seg // **14 seg** | 14 seg // **14 seg** | 14 seg // **14 seg** |  
	
	- Como no veo cambios voy a seguir bajando, ahora solo voy a leer un 5% del csv.  
	
	DataSet: El 5% de **10% Kdd_cup99** 
	Dispositivo: **Raspberry** **SIN CROSS VAL** **(CPU // WALL TIME)**  
	
	| Modelo | Idle | 1 cpu | 2 cpu | 4 cpu |
	|--------|------|------|-------|------|
	|Regresión logística| 13 seg // **11 seg** | 24 seg // **15 seg** | 22 seg // **16 seg**| 18 seg // **15 seg** |
	|SVM | 11 seg // **11 seg** | 11 seg // **11 seg** | 11 seg // **11 seg** | 11 seg // **11 seg** | 
	|Gradient tree boosting | 15 seg // **15 seg**| 15 seg // **15 seg** | 15 seg // **15 seg** | 15 seg // **15 seg** | 
	|Random forest | 13 seg // **12 seg** | 12 seg // **12 seg** | 12 seg // **12 seg** | 12 seg // **12 seg** |  
	
	- Sin cambios voy a probar con el 1% de los datos.  
	
	DataSet: El 1% de **10% Kdd_cup99** 
	Dispositivo: **Raspberry** **SIN CROSS VAL** **(CPU // WALL TIME)**  
	
	| Modelo | Idle | 1 cpu | 2 cpu | 4 cpu |
	|--------|------|------|-------|------|
	|Regresión logística| 11 seg // **11 seg** | 17 seg // **12 seg** | 16 seg // **13 seg** | 13 seg // **12 seg** |
	|SVM | 11 seg // **10 seg** | 11 seg // **10 seg** | 10 seg // **10 seg** | 11 seg // **11 seg** | 
	|Gradient tree boosting | 12 seg // **11 seg** | 11 seg // **11 seg** | 11 seg // **11 seg** | 11 seg // **11 seg** | 
	|Random forest | 11 seg // **11 seg** | 11 seg // **11 seg** | 11 seg // **11 seg** | 11 seg // **11 seg** |  
	
* 25/3/22  
	
	- Voy a probar leyendo únicamente 50 líneas del csv.  
	
	DataSet: 50 líneas de **10% Kdd_cup99** 
	Dispositivo: **Raspberry** **SIN CROSS VAL** **(CPU // WALL TIME)**  
	
	| Modelo | Idle | 1 cpu | 2 cpu | 4 cpu |
	|--------|------|------|-------|------|
	|Regresión logística| 11 seg // **11 seg** | 11 seg // **10 seg** | 11 seg // **10 seg** | 11 seg // **11 seg** |
	|SVM | 11 seg // **10 seg** | 11 seg // **10 seg** | 11 seg // **10 seg** | 10seg // **10 seg** | 
	|Gradient tree boosting | 11 seg // **11 seg** | 11 seg // **11 seg** | 11 seg // **11 seg** | 11 sef // **11 seg** | 
	|Random forest | 11 seg // **11 seg** | 11 seg // **11 seg** | 11 seg // **11 seg** | 11 seg // **11 seg** |   
	
	- Como me han sugerido los tutores voy a probar lo contrario, voy a aumentar el porcentaje.
	Voy a empezar con el 15% dell csv.  
	
	DataSet: El 15% de **10% Kdd_cup99** 
	Dispositivo: **Raspberry** **SIN CROSS VAL** **(CPU // WALL TIME)**  
	
	| Modelo | Idle | 1 cpu | 2 cpu | 4 cpu |
	|--------|------|------|-------|------|
	|Regresión logística| 19 seg // **13 seg** | 32 seg // **19 seg** | 30 seg // **21 seg** | 24 seg // **18 seg** |
	|SVM | 15 seg // **15 seg** | 15 seg // **15 seg** | 15 seg // **15 seg** | 14 seg // **15 seg** | 
	|Gradient tree boosting | 27 seg // **27 seg** | 26 seg // **27 seg** | 26 seg // **26 seg** | 26 seg // **27 seg** | 
	|Random forest | 16 seg // **16 seg** | 16 seg // **16 seg** | 16 seg // **16 seg** | 16 seg // **16 seg** |  
	
	
	DataSet: El 35% de **10% Kdd_cup99** 
	Dispositivo: **Raspberry** **SIN CROSS VAL** **(CPU // WALL TIME)**  	
	
	| Modelo | Idle | 1 cpu | 2 cpu | 4 cpu |
	|--------|------|------|-------|------|
	|Regresión logística| 28 seg // **17 seg** | 36 seg // **22 seg** | 36 seg // **25 seg** | 30 seg // **22 seg** |
	|SVM | 25 seg // **24 seg** | 24 seg // **24 seg** | 24 seg // **24 seg** | 24 seg // **24 seg** | 
	|Gradient tree boosting | 49 seg // **49 seg** | 49 seg // **49 seg** | 48 seg // **48 seg** | 48 seg // **49 seg** | 
	|Random forest | 26 seg // **26 seg** | 26 seg // **26 seg** | 26 seg // **26 seg** | 26 seg // **26 seg** |     
	
	
* 27/3/22  
	
	- He vuelto a probar stress-ng para 50 datos. He instalado stress-ng dentro del entorno de jupiter: ```sudo apt install stress-ng```. Parece que sigue saliendo lo mismo.    
	
	- He encontrado [este](https://github.com/GaetanoCarlucci/CPULoadGenerator/tree/Python3/) repo para estresar la cpu, encontre este repo opr medio de [esta](https://stackoverflow.com/questions/35312756/how-can-i-simulate-cpu-and-memory-stress-in-python) pregunta. De este repo solo quiero clonarme la rama de python 3 ```git clone --branch Python3 https://github.com/GaetanoCarlucci/CPULoadGenerator.git```. Lo voy a probar también por si veo alguna diferencia. Voy a crearme un nuevo enviroment llamado stress_test, he instalado:  
		- sudo apt install python3-matplotlib
		- sudo apt install python3 pstuil (ya estaba instalado)
		- sudo apt intall python3-click  (ya estaba instalado)
	
	Lo voy a eliminar para empezar desde 0 después de comer (volver a crear el enviroment...).  
	
	Vuelvo a crearme un entorno con ```conda create --prefix ./stress_test python=3.6```  
	```conda activate /home/nuria/Documents/CPULoadGenerator/stress_test```
	
	He instalado en este entorno:
		- conda install matplotlib
		- conda install sutils
		- conda install click
	
	(Instalé algo más al intentar intalar matplotlib con pip, algo como pip intall --upgrade setools pero como no he guardado el comitt que lo tenia no se exactamente.)
	
	Ejecutando ./CPULoadGenerator.py -l 1 -d 10 -c 0 parece que va. Pruebo a mirar los tiempos con los modelos.
	Ahora no me acuerdo exactamente (volver a mirar mañana) pero al estresar 4 cpus con 5o lineas de csv los tiempos de cpu se quedaban igual pero los de wall time si crecian algo.
	
	Más o menos creo que esto era todo lo que tenía apuntado antes de apagar el ordenador sin hacer el commit.  
	
* 28/3/22  
	
	Para activar el entorno stress_test: ```coda activate /home/nuria/Documents/CPULoadGenerator/stress_test```
	
	DataSet: 50 líneas de **10% Kdd_cup99** 
	Dispositivo: **Raspberry** **SIN CROSS VAL** **(CPU // WALL TIME)**  
	
	| Modelo | Idle | 1 cpu | 2 cpu | 4 cpu |
	|--------|------|------|-------|------|
	|Regresión logística| 11 seg // **11 seg** | 11 seg // **11 seg** | 11 seg // **11 seg** | 11 seg // **13 seg** |
	|SVM | 11 seg // **10 seg** | 11 seg // **10 seg** | 11 seg // **11 seg** | 11 seg // **14 seg** | 
	|Gradient tree boosting | 11 seg // **11 seg** | 11 seg // **11 seg** | 11 seg // **11 seg** | 11 seg // **14 seg** | 
	|Random forest | 11 seg // **11 seg** | 11 seg // **11 seg** | 11 seg // **11 seg** | 11 seg // **14 seg** |  
	
	
	DataSet: El 35% de **10% Kdd_cup99** 
	Dispositivo: **Raspberry** **SIN CROSS VAL** **(CPU // WALL TIME)**  	
	
	| Modelo | Idle | 1 cpu | 2 cpu | 4 cpu |
	|--------|------|------|-------|------|
	|Regresión logística| 28 seg // **17 seg** | 41 seg // **23 seg**| 35 seg // **24 seg**| 30 seg // **27 seg**|
	|SVM | 25 seg // **24 seg** | 26 seg // **24 seg** | 24 seg // **25 seg**| 25 seg // **32 seg** | 
	|Gradient tree boosting | 49 seg // **49 seg** | 49 seg // **49 seg** | 49 seg // **49 seg** | 49 seg // **63 seg** | 
	|Random forest | 26 seg // **26 seg** | 26 seg // **26 seg** | 26 seg // **26 seg** | 26 seg // **34 seg** |  
	
* 29/3/22  
	
	- Voy a volver a hacer pruebas pero esta vez ejecutando el stress en el mismo terminal que ejecuto python (por probar), para ello:  
		```cd Documents/TFG/kdd_99/l_regresion```
		```conda activate jupiter```
		```sudo stress -c 4 -t 120s > /dev/null 2>&1 &```
		```time python LRegresion.py```  
	
	DataSet: El 35% de **10% Kdd_cup99** 
	Dispositivo: **Raspberry** **SIN CROSS VAL** **(CPU // WALL TIME)**  	
	
	| Modelo | Idle | 1 cpu | 2 cpu | 4 cpu |
	|--------|------|------|-------|------|
	|Regresión logística| 28 seg // **17 seg** | 38 seg // **22 seg**| 38 seg // **24 seg** | 35 seg // **29 seg** |
	|SVM | 25 seg // **24 seg** | 25 seg // **25 seg** | 26 seg // **26 seg** | 25 seg // **33 seg** | 
	
	Lo mismo.
	
	- Si estreso (por ejemplo) 6 cpus consigo aparentemente que el Wall time aumente, sin embargo el cpu se mantiene (seguir probando esto).  
			
* 30/3/22  
	- [Porque el cpu time es más grande que el wall time](https://stackoverflow.com/questions/17843622/benchmarking-cpu-time-bigger-than-wall-time) (por si sirve en algún momento).  
	- [What you can learn from different ratios](https://pythonspeed.com/articles/blocking-cpu-or-io/#:~:text=Wall%20clock%20time%20measures%20how,seconds%20the%20CPU%20was%20busy.)  
	*It’s easier to express the possible relationship as a ratio of (CPU time) / (wall clock time), which is to say CPU/second.*  

	*If this is a single-threaded process:*  

	* *CPU/second ≈ 1: The process spent all of its time using the CPU. A faster CPU will likely make the program run faster.*  
	* *CPU/second < 1: The lower the number, the more of its time the process spent waiting (for the network, or the harddrive, or locks, or other processes to release the CPU, or just sleeping). E.g. if CPU/second is 0.75, 25% of the time was spent waiting.*  
	
## Abril  
			  
* 2/4/22  
	
	- Estoy comprobando la temperatura que tiene la raspberry al ejecutar con diferentes niveles de estrés. Se supone que cuando la Raspberry alcanza 85ºC diminuye la frecuencia de las cpus para poder bajar la temperatura (info [aquí](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#measuring-temperatures)).   
			  
	*All Raspberry Pi models perform a degree of thermal management to avoid overheating under heavy load. The SoCs have an internal temperature sensor, which software on the GPU polls to ensure that temperatures do not exceed a predefined limit; this is 85°C on all models. It is possible to set this to a lower value, but not to a higher one. As the device approaches the limit, various frequencies and sometimes voltages used on the chip (ARM, GPU) are reduced. This reduces the amount of heat generated, keeping the temperature under control.*  
			  
	Para 4 cpus estresadas en regresión lineal llega a los 47 ºC. Si se ejecuta varias veces seguidas llega a unos 54ºC.  
	Con gradient se queda en unos 53ºC, de seguido llega a unos 55ºC.  
			  
* 4/4/22  
	
	- **CORREO 4/4/2022:** Parece que a menos que indiques de forma explícita cuántos cores quieres utilizar, sólo se utiliza uno, por lo que esto explicaría que los tiempos fueran iguales para todos los niveles de saturación: "This configuration argument allows you to specify the number of cores to use for the task. The default is None, which will use a single core."		  
	
	n_jobs= -1  
	DataSet: El 10% de **10% Kdd_cup99**  
	Dispositivo: **Raspberry** **SIN CROSS VAL** **(CPU // WALL TIME)**  			  
	
	| Modelo | Idle | 1 cpu | 2 cpu | 4 cpu |
	|--------|------|------|-------|------|
	|Regresión logística| 28 seg // **23 seg**| 27 seg // **22 seg** | 26 seg // **22 seg** | 26 seg // **23 seg** |
	|Random forest | 18 seg // **14 seg** | 17 seg // **14 seg** | 16 seg // **14 seg** | 16 seg // **15 seg** |  
			  
	Ni máquinas de soporte vectorial ni gradient tree boosting permiten paralelización, por lo tanto [no tienen parámetro n_jobs](https://github.com/scikit-learn/scikit-learn/issues/8026).    
			  
	n_jobs= 4  
	DataSet: El 10% de **10% Kdd_cup99**  
	Dispositivo: **Raspberry** **SIN CROSS VAL** **(CPU // WALL TIME)**  			  
	
	| Modelo | Idle | 1 cpu | 2 cpu | 4 cpu |
	|--------|------|------|-------|------|
	|Regresión logística| 28 seg // **21 seg**| 27 seg // **22 seg** | 26 seg // **22 seg** | 26 seg // **23 seg** |
	|Random forest | 18 seg // **14 seg** | 17 seg // **14 seg** | 16 seg // **14 seg** | 16 seg // **15 seg** |  		
			  
	Random forest no he ejecutado todo (solo para 1 y 4 cpus estresadas) pero viendo los resultados de esto supongo que van a volver a salir los mismos tiempos en los diferentes casos.  
			  
	n_jobs= 1  
	DataSet: El 10% de **10% Kdd_cup99**  
	Dispositivo: **Raspberry** **SIN CROSS VAL** **(CPU // WALL TIME)**  			  
	
	| Modelo | Idle | 1 cpu | 2 cpu | 4 cpu |
	|--------|------|------|-------|------|
	|Regresión logística| 16 seg // **13 seg** | 27 seg // **17 seg** | 27 seg // **19 seg** | 20 seg // **16 seg** |
	|Random forest | 15 seg // **15 seg** | 14 seg // **14 seg** | 15 seg // **15 seg** | 14 seg // **14 seg** |  	
			  
			  
	n_jobs= NO poniendolo  
	DataSet: El 10% de **10% Kdd_cup99**  
	Dispositivo: **Raspberry** **SIN CROSS VAL** **(CPU // WALL TIME)**  			  
	
	| Modelo | Idle | 1 cpu | 2 cpu | 4 cpu |
	|--------|------|------|-------|------|
	|Regresión logística| 15 seg // **12 seg** | 26 seg // **16 seg** | 26 seg // **18 seg** | 20 seg // **16 seg** |
	|Random forest | 14 seg // **14 seg** | 14 seg // **14 seg** | 14 seg // **14 seg** | 14 seg // **14 seg** |  	
			  
	
* 6/4/22  
	
	- No es lo mismo indicar n_jobs = 4 que n_jobs = -1, ya que n_jobs = -1 lo que dice es "the task will use all of the cores available on your system.". El matiz está en la palabra "available", esto no es seguro que signifique todos.	
			  
	- Voy a ejecutar n_jobs= 1 y n_jobs= 8 en el portátil para observar los tiempos que se obtienen (lo hago hasta con 8 cpus estresadas por ver como se comportan con el portátil totalmente estresado):	
			  
	n_jobs= 1  
	DataSet: El 10% de **10% Kdd_cup99**  
	Dispositivo: **Portátil** **SIN CROSS VAL** **(CPU // WALL TIME)**  			  
	
	| Modelo | Idle | 1 cpu | 2 cpu | 4 cpu | 8 cpu |
	|--------|------|------|-------|------|---------|
	|Regresión logística| 3 seg // **2 seg** | 3 seg // **2 seg** | 4 seg // **3 seg** | 6 seg // **5 seg** | 8 seg // **7 seg** |
	|Random forest | 2 seg // **2 seg** | 2 seg // **2 seg** | 3 seg // **3 seg** | 6 seg // **6 seg** | 6 seg // **7 seg** | 	
			  
	
	n_jobs= 4  
	DataSet: El 10% de **10% Kdd_cup99**  
	Dispositivo: **Portátil** **SIN CROSS VAL** **(CPU // WALL TIME)**  			  
	
	| Modelo | Idle | 1 cpu | 2 cpu | 4 cpu | 8 cpu |
	|--------|------|------|-------|------|---------|
	|Regresión logística| 4 seg // **3 seg** | 4-5 seg // **3 seg**  | 6 seg // **4 seg** | 10 seg // **7 seg** | 10 seg // **9 seg** |
	|Random forest | 2 seg // **2 seg** | 2-3 seg // **2 seg** | 4 seg // **3 seg** | 6 seg // **5 seg** | 6 seg // **7 seg**  | 			
			  
	- En regresión logistica con 1 cpu estresada al principio da valores de Cpu time= 4 seg, Wall time= 3 seg, pero pasados unos 30 seg (más o menos) los tiempos ascienden a Cpu time= 5 seg, Wall time= 3 seg y de ahí no incrementan más. Luego para obtener los verdaderos tiempos lo que hago es que **una vez ejecutado stress dejo que pasen unos cuantos segundos hasta recoger los datos**. En regresión logísitca con 2 cpus estresadas pasa un poco igual al inicio la cpu time esta sobre los 4 seg para luego ascender y mantenerse en los 6 seg.  
	Lo mismo pasa con random forest para 1 cpu al principio el CPu time son 2 seg y después de pasar unos cuantos segundos se queda en 3 seg.  
			  
	- ¿Por qué n_job= 1 más rápido que n_jobs= 4? [the reason n_jobs>1 is even more slow than n_jobs=1 is because of the cost to distribute resources for multiprocessing.](https://stackoverflow.com/questions/36250555/why-scikit-learn-neighbors-is-slower-with-n-jobs-1-and-forkserver). Otro [enlace](https://stats.stackexchange.com/questions/268828/why-is-random-forest-classifier-slower-when-n-jobs-increases) que explica esto.	 
	
	- Sabiendo esto he probado a ver si se cumplía utilizando el 100% del **10% Kdd_cup99**. Sin embargo aún utilizando todas esas filas el tiempo sigue aumentando con n_jobs= 4 en el caso de regresión logísitica.
	En random forest con el 100% del **10% Kdd_cup99** pasa lo mismo.
	
* 7/4/22  	
	
	**10% Kdd_cup99** Portátil
	| Modelo | Idle n_jobs= 1| Idle n_jobs= 4 | Idle n_jobs= 8 |
	|--------|---------------|----------------|----------------|
	|Regresión logística| 12 seg // **5 seg** | 24 seg // **13 seg** | 18 seg // **16 seg** |  
	|Random forest | 10 seg // **10 seg**  | 18 seg // **7 seg** | 36 seg // **8 seg** |  
	
	- Intentando descargarme el 100% de Kdd_cup99 (en el portátil) los datos me los he descargado de [aquí](https://www.kaggle.com/datasets/galaxyh/kdd-cup-1999-data?select=kddcup.data.gz). ~~Cambio el nombre del fichero de kddcup.data a kddcup.csv~~.
	Ejecuto Download_dataSet.py (poner la direccion del fichero correcta) para combertirlo en clasificacion binaria. De momento **NO** puedo al ejecutarlo me aparece Killed.
	Pruebo a intentar convertir el 20% de los datos. Para saber cuanto es el 20% hago regla de tres, si 10% -----> 494020, 20% -------> x, y de la misma forma que lo hago en los modelos lo he hecho en Download_dataSet.py. El 20% del fichero total son unas 979500 líneas  
	
	**20% Kdd_cup99** Portátil
	| Modelo | Idle n_jobs= 1 | Idle n_jobs= 8 |
	|--------|---------------|----------------|
	|Regresión logística| 23 seg // **10 seg** | 37 seg // **34 seg** |  
	|Random forest | 19 seg // **19 seg** | 77 seg // **15 seg** |  
	
	**40% Kdd_cup99** Portátil
	| Modelo | Idle n_jobs= 1 | Idle n_jobs= 8 |
	|--------|---------------|----------------|
	|Regresión logística| 44 seg // **19 seg** | 76 seg // **72 seg** |  
	|Random forest | 42 seg // **43 seg** | 172 seg // **31 seg** |  
	
	- Voy a intentar ver cual es el máximo % del fichero total que puedo leer. El máximo que he podido leer es el 50% unas 2470100 líneas.  
	
	**50% Kdd_cup99** Portátil
	| Modelo | Idle n_jobs= 1 | Idle n_jobs= 8 |
	|--------|---------------|----------------|
	|Regresión logística| 55 seg // **23 seg** | 98 seg // **95 seg** |  
	|Random forest | 52 seg // **53 seg** | 218 seg // **41 seg** |  
	
	Con n_jobs= 8 no veo que se pongan todas las cpus al 100% en regresión logística. Con random forest si.  
	
	- En la Raspberry no puedo leer el 50% del total, se muere el proceso. El 40% del fichero si, unas 1976080 líneas.  
	
	**40% Kdd_cup99** Raspberry
	| Modelo | Idle n_jobs= 1 | Idle n_jobs= 4 |
	|--------|---------------|----------------|
	|Regresión logística| 4 min 24 seg // **2 min 32 seg** | 6 min 17 seg // **7 min 14 seg** |  
	|Random forest | 3 min 59 seg // **4 min 31 seg**| 7 min 2 seg // **3 min 8 seg** |  
	
	Con regresion logistica en la Raspberry pasa lo mismo, a pesar de poner n_jobs= 4 solo está utilizando una cpu. Con Random forest si se ponen todas las cpus al 100%.  
	
* 8/4/22  
	
	- Creo que a Regresión logística no le afecta el n_jobs porque es binomial para que sea multithreading tendría que ser multiclase.  
		[sklearn.LogisticRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)  
		- *n_jobs=int, default=None  
		Number of CPU cores used when parallelizing over classes if multi_class=’ovr’”.*  
	
		- *multi_class{‘auto’, ‘ovr’, ‘multinomial’}, default=’auto’  
		If the option chosen is ‘ovr’, then a binary problem is fit for each label*
	
	- [Enlace](https://unix.stackexchange.com/questions/40694/why-real-time-can-be-lower-than-user-time) con información a cerca de que significa cuando wall time es mayor o menor que cpu. Puede ser útil para saber lo que está pasando.  
	
	-¿Por que cpu time incrementa con n_jobs mayores? [Respuesta](https://stackoverflow.com/questions/58998202/does-multithreading-increase-cpu-time#:~:text=For%20multiple%20cores%2C%20CPU%20time,but%20wall%20time%20may%20decrease.)   
	*For multiple cores, CPU time is measured as the total CPU time for all cores. So if you have a program with multiple threads, and if those threads are scheduled on multiple cores, the CPU time will increase, but wall time may decrease.*   
	
	- Tiempos estresando en diferentes niveles con el valor n_jobs= 4.    
		
	**10% Kdd_cup99** Raspberry
	| Modelo | Idle | 1 cpu | 2 cpu | 4 cpu |
	|--------|------|------|-------|------|
	|Random forest | 18 seg // **14 seg** | 17 seg // **14 seg** | 16 seg // **14 seg** | 16 seg // **15 seg** |  
	
	(Habría que hacer una tabla con todos los tiempos para el 40% Kdd_cup99 con todos los modelos)  
	
	**40% Kdd_cup99** Raspberry
	| Modelo | Idle | 1 cpu | 2 cpu | 4 cpu |
	|--------|------|------|-------|------|
	|Random forest | 7 min 13 seg // **3 min 12 seg** | 5 min 32 seg // **3 min 31 seg** | 4 min 46 seg // **3 min 57 seg** | 5 min // **4 min 3 seg** |   
	

* 9/4/22  
	
	- ~~**Cambiar la forma en la que se hace la clasificación por medio de máquinas de soporte vectorial ya que en la codumentación de [SVC])(https://scikit--learn-org.translate.goog/stable/modules/generated/sklearn.svm.SVC.html?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=sc) dice que puede no ser práctico más allá de decenas de miles de muestras. Utilizar en su lugar [SVC Linear](https://scikit--learn-org.translate.goog/stable/modules/generated/sklearn.svm.LinearSVC.html?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=sc#sklearn.svm.LinearSVC)**~~ Lo dejo como estaba porque a pesar de lo que pone tarda bastante más utilizando LinearSVC que SVC a secas.  
	
	- Redacción de la memoria  
	
* 10/4/22  
	
	- He conseguido que la limpieza del dataSet se haga en Download_dataSet.py. Pero me he dado cuenta de que se eliminan 365501 líneas porque están repetidas. En cambio limpiandolo dentro de el código del modelo se eliminan 367814 líneas del csv kddcup_10_perBinary (más o menos las mismas, teniendo en cuenta de que Clean contiene un 10% del total no del kffcup_10_per.data).  
	
	- Hay que volver a obtener los tiempos para este dataSet ya tratado.
	
	- He cambiado SVC a LinearSVC pero (a diferencia del otro) me está pidiendo que incremente el máximo número de iteraciones. El otro en max_iter tenía un -1 con lo que hacía todas las iteraciones que necesitase (no tenía limite).    
	
	- Resumen de lo de las línea del fichero:  
		El 10% de kdd_cup_99 tiene un total de 494020. Por ello podemos suponer que el dataset completo tiene un total de 4940200.  
		Al tratar (convertir a binrario y tartar los datos) el fichero que se guarda como Clean tiene un total de 145584 líneas limpias y listas para entrenar con ellas.  
		El dataset obtenido de leer el 40% de los datos, una vez convertido a binario y limpiado tiene un total de 479473 líneas.  
		El dataset obtenido de leer el 20% de los datos, una vez convertido a binario y limpiado tiene un total de 262379 líneas.  
	
	- A la hora de realizar las pruebas en la Raspberry comprobar que ambos csv tengan el mismo número de líneas. Para que estén en las mismas condiciones.  
	
	~~Con el 40% de los datos 479473 líneas no es capaz de entrenarlo (llega a el máximo) para regresión Logísitca. Los tiempos que ha devuelto (sin llegar a entrenar completamente) son de Wall time= 8 min 7 seg, Cpu time 8 min.~~ Luego voy a probar primero con un dataSet más pequeño, porque si no va a ser imposible sacar los tiempos estresado.  
	
	Con un 20% se supone que si se nota el efecto de n_jobs, puesto que para n_jobs= 1 Wall time= 1 min 40 seg, Cpu time= 1 min 39 seg. Y para n_jobs= 4, Wall time= 1 min 3 seg, Cpu time= 3 min 19 seg.  
	
	DataSet: El 20% de **Kdd_cup99** 
	Dispositivo: **Raspberry** **SIN CROSS VAL** **(CPU // WALL TIME)**  
	| Modelo | Idle | 1 cpu | 2 cpu | 4 cpu |
	|--------|------|------|-------|------|
	|Regresión logística| 1 min 36 seg // **38 seg** | 1 min 48 seg // **50 seg** | 1 min 33 seg // **56 seg** | 1 min 34 seg // **57 seg** |
	|SVM | 2 min 15 seg // **2 min 16 seg** | 2 min 17 seg // **2 min 18 seg** | 2 min 12 seg // **2 min 12 seg** | 2 min 18 seg // **2 min 18 seg** | 
	|Gradient tree boosting | 3 min 19 seg // **3 min 20 seg** | 3 min 19 seg // **3 min 20 seg** | 3 min 15 seg // **3 min 15 seg** | 3 min 16 seg // **3 min 17 seg** | 
	|Random forest | 3 min 4 seg // **1 min 3 seg** | 2 min 30 seg // **1 min 5 seg** | 2 min 3 seg // **1 min 10 seg** | 2 min 10 seg // **1 min 18 seg** |  
	
	En regresión logistica si pongo n_jobs= 4 solo utiliza una cpu. Si no pongo nada de n_jobs utiliza todas, todas se ponen al 100%. Si pongo n_jobs= 1 utiliza todas. Si pongo n_jobs= 2 solo utiliza una. Si pongo n_jobs= -1 usa solo una. [Relacionado](https://github.com/scikit-learn/scikit-learn/issues/8883) otro [enlace](https://stackoverflow.com/questions/39620185/sklearn-logistic-regression-with-n-jobs-1-doesnt-actually-parallelize) que ya he linkeado anteriormente.  
	Si pongo:  
	```
	from joblib import parallel_backend  
	...
	with parallel_backend('threading', n_jobs= 4):
		l_regr= LogisticRegression(max_iter= 400)
		l_regr.fit(x_scaled, y_train)
		...
		print("Total time", t_time)
	```  
	Mismos tiempos
	
	Respecto a la tabla anterior en Random forest el Wall time si va incrementando pero el cpu time no.  
	
	Con el 40% n_jobs= 1, Wall time 3 min 20 seg, Cpu time 3 min 22 seg. Con n_jobs= 4, Wall time= 2 min 8 seg, Cpu time= 6 min 37 seg.   
	
	n_jobs= 4  
	**40% Kdd_cup99** Raspberry
	| Modelo | Idle | 1 cpu | 2 cpu | 4 cpu |
	|--------|------|------|-------|------|
	|Random forest | 6 min 37 seg // **2 min 8 seg** | 5 min 32 seg // **2 min 16 seg** | 4 min 20 seg // **2 min 25 seg** | 4 min 34 seg // **2 min 38 seg** |   
	
	n_jobs= 2  
	**40% Kdd_cup99** Raspberry
	| Modelo | Idle | 1 cpu | 2 cpu | 4 cpu |
	|--------|------|------|-------|------|
	|Random forest | 4 min 20 seg // **2 min 24 seg** | 4 min 14 seg // **2 min 22 seg** | 4 min 14 seg // **2 min 27 seg** | 4 min 11 seg // **2 min 37 seg** |     
	
	Cuando ejecuto n_jobs= 2 aparecen tres procesos en htop. Cuando ejecuto n_jobs= 4 aparecen 5 procesos.  
	
* 20/4/22  
	
	* [Multiprocessong vs Multithreading](https://www.indeed.com/career-advice/career-development/multithreading-vs-multiprocessing#:~:text=Multiprocessing%20uses%20two%20or%20more,threads%20from%20a%20single%20process.)  
	* [Regresión logística n_jobs solo afecta si es milticlase](https://stackoverflow.com/questions/69762314/multiprocessing-in-logistic-regression-in-python)  
	
	n_jobs= 8  
	**40% Kdd_cup99** Portátil
	| Modelo | Idle | 2 cpu | 4 cpu | 8 cpu |
	|--------|------|------|-------|------|
	|Random forest | 2 min 40 seg // **28 seg** | 2 min 12 seg // **29 seg** | 2 min 1 seg // **34 seg** | 2 min 23 seg // **57 seg** |   
	
	n_jobs= 4  
	**40% Kdd_cup99** Portátil
	| Modelo | Idle | 2 cpu | 4 cpu | 8 cpu |
	|--------|------|------|-------|------|
	|Random forest | 1 min 25 seg // **26 seg** | 1 min 35 seg // **29 seg** | 1 min 42 seg // **36 seg** | 2 min 15 seg // **1 min 4 seg** |   
	
	n_jobs= 4 debería de tardar más porque dispone de menos cores para poder ejecutar el programa. Cpu time tiene que ser menor porque en n_jobs se está contando la suma de los tiempos de las 8 cpus y en n_jobs solo se suman 4 tiempos.    
	
	Dando mayor prioridad al stress en la Raspberry ejecutando sudo nice -n -5 stress -c 4 -t 200s sigo obteniendo los mismos resultados.  
	
* 20/4/22  
	
	* Ejecutando Random forest con n_jobs= 8 en idle el máximo valor que obtengo al ejecutar el código en la columna CPU% de htop es de 400 ~(entre todos los procesos que aparecen, 5 en total, el primero tiene un valor de 400 el resto tiene valor de 100 luego en total esta usando 800). Entre físicas y lógicas la Raspberry tiene un total de 8 cpus.~
	Sin embargo cuando hago lo mismo estresando las cuatro cpus lo el valor máximo es de 200 ~(entre todos los procesos de Random forest que aparecen, que son 5, suman un total de 400)~. ~Sumandole los porcesos de stress da unos 600~ (ya que los procesos de stress bajan a estar sobre el 50 cada uno) [Info relacionada](https://superuser.com/questions/575202/understanding-top-command-in-unix/575330#575330):  
	
	*%CPU -- CPU Usage : The percentage of your CPU that is being used by the process. By default, top displays this as a percentage of a single CPU. On multi-core systems, you can have percentages that are greater than 100%. For example, if 3 cores are at 60% use, top will show a CPU use of 180%.*  
	Otro [enlace](https://superuser.com/questions/457624/why-is-the-top-command-showing-a-cpu-usage-of-799) que puede ser útil:  

	*The scale used by top is 100% when a core is fully used. Or when one core is 20% and a second one is 80%. This lead to strange results on multicore computers because it easely can exceed 100%. If you have 8 cores, then top can display from 0% (idle system) to 800% (full power).*  

	*Your program is just using your 4 cores with hyperthreading (so 8 virtual cores) at maximum capacity. So top gives you nearly 8 x 100% = 800%.*
	
	* Con n_jobs= 2 en idle el primer proceso esta a 200 y los otros dos se quedan en 100, luego usa un total de 300 (3 cpus al 100%). Cuando se estresan las 4 cpus pasa lo mismo.  
	
	* De todas formas siempre los procesos de RForest ocupan más cpu que stress. Stress llega a bajar cada uno de los cuatro procesos (en casod e estresar las cuatro cpus) a un 50, en vez de estar a 100.
	
	* **A no ser que el primer proceso sea el que cuente de verdad, entonces tiene más sentido porque así en el caso de n_jobs= 4 estaría usando todas al 100% y n_jobs= 2 dos al 100%** Pero al estresar las 4 para n_jobs= 4 en en realidad solo está usando 2 ya que tiene que lidiar con los estreses que como son 4 procesos al 50% de cpu están usando en total dos cpus enteras solo para ellos. Luego con n_jobs= 4 RandomForest usa en total la mitad de las cpus y stress la otra mitad.    
		
	Luego usar más cores no está beneficiando la ejecución al revés la hace más lenta que cuando utiliza solo dos cores. Si nos fijamos bien en realidad los tiempos para cuando se estresan 2 y 4 cpus en n_jobs= 4 para la Raspberry son los mismos que para n_jobs= 2, porque en cuanto para ese valor de n_jobs y cpus estresadas hemos alcanzado el máximo de recursos que se pueden usar en la Raspberry.  
	Si ponemos n_jobs= 2 y 2 cpus estresadas una vez más RForest usara 2 cpus y stress otras 2 en total, si n_jobs= 2 y 3 cpus estresadas da igual porque va a ser otra vez lo mismo no hay más recursos que se puedan usar (lo pruebo y los resultados son RForest usa unos 200 y entre todos los stress suman 200 (80+60+60)).  
	
	* Ahora tengo que entender por qué en idle con 4 cores tarda más que con 2. Respuesta?: Es como cuando hice las pruebas para diferentes valores de n_jobs a mayor número de cores mayor el tiempo de ejecución.  
	
* 22/4/22  
	
	* Conclusiones de stress con los modelos de aprendizaje:  
	
		- Para los modelos de regresión lineal, máquinas de soporte vectorial y gradient tree boosting. Los tres modelos son monocore, es decir, que solo pueden usar una cpu (no se pueden dividir) ~luego en realidad solo le está afectando cuando se estresa una cpu puesto que aun que se estresen más cpus a los modelos no les importa porque tienen que seguir lidiando exacatmanete con la misma carga que cuando solo se estresa una cpu~. Estos tiempos son los mismos siempre porque stress siempre les "deja espacio" para que puedan ejecutar, es decir que si a máquinas de soporte vectorial estresamos 4 cpus, en realidad por medio de htop vemos que los cuatro procesos de stress están usando en total 3 cores, dejando la cuarta a el modelo para que pueda ejecutar.    
	
		- El modelo random forest si que modifica su comportamiento con más cpus estresadas. Pero aparece con más tiempo de cpu cuando está idle porque es ese en el único instante en que realmente todas las cpus están a su disposición. Cuando se estrese alguna cpu la Raspberry tendrá que lidiar a la vez con los stress y con el algoritmo. En el caso de estresar 4 cores tanto stress como el modelo usarán cada uno en total dos cpus (a pesar de que stress se le comanda estresar dos cpus como random forest también quiere usar 4 cpus se las distribuyen de esta forma).  
	
	* ~En Regresion logisitica aunque aparezcan las 4 cpus saturadas solo está usando unas 2-3 porque la cpu devuelve para ese proceso valor entre 200 y 300 (esto si no pongo nada de n_jobs)~ He vuelto a ahcer la prueba y si utiliza los 4 cores. Con n_jobs= 4 solo usa un core pero el nombre del proceso cambia se pasa a llamar /home/nuria/miniforge3/envs/juìter/bin/pyhton -m joblib.external.locky.backend.popen_loky_posix --process-name LokyProcess --pipe 13.  Tarda mucho tiempo asignando n_jobs=4 en total 8 min Wall time y 8 min 7 seg Cpu time. Al parecer n_jobs en regression logisitica está limitado a cross validation o algo así:  
	[*n_jobs parameter was limited to cross validation*](https://stackoverflow.com/questions/39969230/how-to-enable-multicore-processing-with-sklearn-logisticregression)   
	
	- En el portátil pasa lo mismo para n_jobs= 8 y estresar 8 cpus. Al final el modelo usa 4 cores y los stress (la suma de todos también).  
	
* 23/4/22  
	
	* Para n_jobs de Logisitc Regression que todavía no termino de entender muy bien:  
	
		[*Number of CPU cores used during the cross-validation loop*](https://stackoverflow.com/questions/20894671/speeding-up-sklearn-logistic-regression)  
		[*If your data does not have more than two classes, setting the n_jobs argument is virtually useless.*](https://stackoverflow.com/questions/69762314/multiprocessing-in-logistic-regression-in-python)  
	
	* Probar el dataSet de Occupancy para n_jobs= 4 en Random forest, por ver si cambian los valores. Son tan pocos los datos de este dataset que no hay apenas diferencia.   
	
	n_jobs= 4  
	
	**Occupancy** Raspberry SIN Cross validation
	| Modelo | Idle | 1 cpu | 2 cpu | 4 cpu |
	|--------|------|------|-------|------|
	|Regresión logística| 9 seg // **8 seg** | 12 seg // **9 seg** | 11 seg // **9 seg** | 11 seg // **9 seg** |
	|SVM | 7 seg // **6 seg** | 6 seg // **6 seg** | 6 seg // **6 seg** | 6 seg // **6 seg** | 
	|Gradient tree boosting | 8 seg // **8 seg** | 8 seg // **8 seg** | 8 seg // **8 seg** | 8 seg // **8 seg** | 
	|Random forest | 9 seg // **6 seg** | 8 seg // **6 seg** | 8 seg // **6 seg** | 8 seg // **7 seg**|  
	
	En Random forest apenas se nota la diferencia porque el data set es muy pequeño.  
	
* 25/4/22  
	
	- En Random forest cuando n_jobs= 4 y se estresan 2 cpus en realidad el modelo solo va a usar dos cpus (y stress las otras dos).   
	
	n_jobs= 8  
	**20% Kdd_cup99** Portátil
	| Modelo | Idle | 2 cpu | 4 cpu | 6 cpus | 8 cpu |
	|--------|------|------|--------|--------|-------|
	|Regresión logística| 58 seg // **30 seg** | 1 min 7 seg // **36 seg** | 1 min 23 seg // **47 seg** | 1 min 30 seg // **47 seg** | 1 min 46 seg // **1 min 22 seg** |
	|SVM | 31 seg // **31 seg** | 47 seg // **47 seg** | 1 min 21 seg // **1 min 21 seg** | 1 min 25 seg // **1 min 25 seg** | 1 min 32 seg // **1 min 34 seg** | 
	|Gradient tree boosting |  42 seg // **42 seg** | 56 seg // **57 seg** | 1 min 30 seg // **1 min 30 seg** | 1 min 26 seg // **1 min 27 seg** | 1 min 42 seg // **1 min 58 seg** | 
	|Random forest | 1 min 15 seg // **13 seg** | 1 min 1 seg // **15 seg** | 1 min 1 seg // **21 seg** | 1 min 1 seg // **25 seg** | 59 seg // **26 seg** |    
	
	Regresión logística en el portátil (idle, 2 cpus, 4cpus estresadas) usa dos cores. Con 8 cpus en el comando stress utiliza más o menos 6 cores para esta tarea y otros dos para el modelo (más o menos porque en el portátil si que hay otros procesos que tambien consumen cpu a diferencia de en la Raspberry).  
	
	En Gradient tree boosting oc n 8 cores estresados no llega a usar el modelo una cpu all completo se quea en el 86% más o menos, hay ratos que si sube al 90-96% pero no se mantiene en ese porcentaje casi nada (al contrario de lo que pasa en la Raspberry). Lo mismo pasa con máquinas de soporte vectorial que el proceso del modelo no se mantiene todo el rato arriba del todo (es decir, todo el rato en 100%) cuando se estresan 8 cores.    
	
	En Random forest con n_jobs= 8 y dos cpus estresadas, los procesos de stress usan en total 2 cores y el modelo 6. Con 4 estresadas el modelo usa en total 5 cores y stress 3. Al intentar estresar las 8 las cpus se dividen en 4 para el modelo y 4 para los procesos de stress.  
	
	Si se hace la division de los tiempos entre el verdadero número de cores (que se comenta justo en el párrafo anterior) que utilizan si se ve que ascienden los tiempos:  
	
		Si se divide 1 min 1 seg /6 cores = 10 seg por cada core.  
		Si se divide 1 min 1 seg /5 cores = 12 seg por cada core.  
		Si se divide 59 seg / 4 cores = 15 seg por cada core.  
	
* 26/4/22  
	
	Día horrible, no se por qué a dejado de funcionar lgpio en en el enviroment myenv y no había forma de que funcionase ni entiendo lo que ha pasado. El error que daba es: ImportError:liblgpio.so.1: cannot open shared object file: No such file or directory. 
	
	* He creado otro entorno 
		```conda create --name lgpio python=3.9  
		conda activate lgpio  
		conda install numpy  
		sudo apt-get install python3-lgpio
		(Mover todos los paquetes como expliqué en la tabla)  
		sudo env "PATH=$PATH" python LDR_data_lgpio.py
		```
	
	Y ha vuelto a ir.
	
	Lo que hay en la variable PATH (aun que este no haya sido el problema en el otro entorno pero por si acaso): /home/nuria/miniforge3/envs/lgpio/bin:/home/nuria/miniforge/condabin:/home/nuria/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/snap/bin
	
	
* 27/4/22  
	
	Generando un fichero que se llama read_timer, que estará leyendo los sensores hasta que se pulse CTR-C. Añade tiempo y la medida de un sensor (lo he estado probando con el de la luz). Voy a poner state= 1 - state para que cuando haya un 1 signifique que hay luz y un 0 cuando no la haya.  
	
	* Buscando explicación a por qué el portátil incrementa el tiempo. La Raspberry tiene un thread por core, el portátil tiene dos threads por core (no creo que tenga que ver con esto pero bueno).  
	
	* Lo que puede estar pasando para que cambien los tiempos de ejecución en el portátil es que cuando se estrese este causando que el proceso del modelo tenga menos frecuencia (de cpu) de ejecución haciendo que tarde más en terminar la tarea. (Tenía esto apuntado pero no se que ha pasado)
	La frecuencia del portátil media es de 850 MHz, la mínima de 400 MHz y la máxima de 3600 MHz.  
	Mientras que en la Raspberry no tenemos frecuencia media pero la mínima de 600 MHZ y la máxima es de 1500 MHz.  
	
* 28/4/22  
	
	* Estoy mirando la frecuencia a la que ejecutan cada una de las cpus estresadas en idle en Raspberry mediante el comando:
	
	```
	watch -n.1 "sudo cat /sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_cur_freq && sudo cat /sys/devices/system/cpu/cpu1/cpufreq/cpuinfo_cur_freq && sudo cat /sys/devices/system/cpu/cpu2/cpufreq/cpuinfo_cur_freq && sudo cat /sys/devices/system/cpu/cpu3/cpufreq/cpuinfo_cur_freq
	```
	*cpuinfo_cur_freq :*&nbsp;&nbsp;&nbsp;&nbsp;*Current frequency of the CPU as obtained from the hardware, in KHz. This is the frequency the CPU actually runs at.*  
	
	En idle los cuatro cores tienen una frecuencia de 1300000-1500000 KHz (luego unos 1300-1500 MHz), pero prácticamente todo el rato se encuentra en 150000. Este es el máximo de frecuencia al que puede ir la Raspberry luego stress no puede aumentar este valor. Puede ser esta la razón por la que los tiempos se mantienen iguales mientras que en e portátil si crecen?.  
	
	En el portatil ejecutando:  
	```watch -n.1 "grep \"^[c]pu MHz\" /proc/cpuinfo"```
	
	En idle están todas entre 900-1000 MHz. Si estreso 2 cores más o menos están todas sobre los 1800-2500 MHz. Con cuatro cores estresados 1700-1800 MHz. Con seis cores 1600-1800 MHz. Ocho cores 1600-1700 MHz.  
	
* 29/4/22  
	
	* Si ejecuto uno de los modelos en idle puedover que la cpu que lleva el proceso(que se ven en htop cual es) aumenta la frecuancia de ejecución hasta 3000-3330 MHz.  
	Cuando hago stress todas las frecuencias "suben" no solo las de los cores que lo están ejecutando.  
	Los tiempos que obtuve ayer sobre stress tienen sentido porque cuanto más stress menos frecuencia porque... (edición 2/5/22: porque hay más procesos intentando hacer cosas y por lo tanto para que todos puedan ejececutar cada vez hay más espcacio de tiempo entre que le dejan hacer algo y el siguiente instante, porque todos está más ocupado. Cuantas más tareas tengamos menos tiempo tendrá el núcleo para ejecutar cada una de ellas.) 
	
	* El script que va a ejecutar todos los modelos lo escibo en jupyter-notebook. Para ejecutarlo:  
	```ipython file.ipbn dataset_name```  
	
* 30/4/22    
	
	* Terminar programa pc_test. Voy a añadir los tiempos obtenidos al ejecutar este programa a la tabla de Overleaf.   
	

## Mayo  
	
* 2/5/22  
	
	* Redactando memoria todo desde el sábado.  
	
	* Tabla de los tiempos que obtueba al ejecutar el pc_test.  
	
	n_jobs= 8  
	**20% Kdd_cup99** Portátil
	| Modelo | Idle | 2 cpu | 4 cpu | 8 cpu |
	|--------|------|------|--------|-------|
	|Regresión logística| 18 seg // **7 seg** | 21 seg // **8 seg** | 29 seg // **14 seg** | 48 seg // **27 seg** |
	|SVM | 31 seg // **31 seg** | 43 seg // **43 seg** | 58 seg // **58 seg** | 1 min 22 seg // **1 min 32 seg** |
	|Gradient tree boosting |  41 seg // **41 seg** | 54 seg // **54 seg** | 1 min 27 seg // **1 min 27 seg** | 1 min 28 seg // **1 min 41 seg** |
	|Random forest | 1 min 16 seg // **13 seg** | 1 min 5 seg // **15 seg** | 58 seg // **19 seg** | 54 seg // **23 seg** |   
	
	
# **TO DO Memoria:**  
	
**Para guardar la memoria en git:**  
- Guardo el zip  
- Descomprimo zip  
- Descargo el pdf y lo guardo dentro de la carpeta generada por el zip  

Repasar estado del arte: Miniconda poner algo sobre que ofrece un mayor control sobre el entorno en el que se desarrolla el programa, respecto a los paquetes que se instalan. Además permite "compartir" el entorno de forma que se puede replicar ese enotorno virtual en otra máquina.  
~~Cambiar Miniconda!!! es **Miniforge3** !!~~  
~~¿Por qué lgpio?~~  
- [x] Pasar el desarrollo de los problemas de de instalación (miniconda, RPi.GPIO...) Al Anexo.  
	
Estado del arte meter las librerías de scikit-learn, pandas, jupyter-notebook?  
Comentar en la memoria que dado que es un gran número de ejemplos no es necesario utilizar stratified a pesar de que haya menor número de muestras en una clase que en otra. Mirar otra vez como he explicado lo de validación cruzada.
	
(Sobre la estratificación: Un aspecto importante a destacar de este set de datos es que hay una mayor cantidad de ejemplos de habitación no ocupada que de ocupada. En otros sets de datos esto podría representar un problema ya que puede dar lugar a que al realizar esta división de forma aleatoria, el conjunto de datos de entrenamiento apenas tenga ejemplos de una de las clases. Sin embargo al tener una gran cantidad de ejemplos en el que ambas clases tienen una gran cantidad de muestras, como es este caso, una división aleatoria no representa ningún inconveniente dado que el set de entrenamiento siempre tendrá la cantidad de muestras necesarias de ambas clases para entrenar correctamente. )  
			  
- [x] Añadir al estado del arte el sistema operativo que se utiliza: Ubuntu 21.10  
- [x] Añadir como se instaló o por lo menos hacer referencia al enlace que se utilizó para intstalarlo (día 28/1/22)  
- Añadir los resultados de las primeas pruebas, que bajo diferentes niveles de saturacion los tiempos no tenían mucho sentido, que se probó con un nuevo dataSet...	
- Añadir todo lo que he descubierto sobre n_jobs, SMP...  
- ¿Debería de explicar brevemente en qué consisten cada uno de los modelos de aprendizaje automático utilizados?¿Debería de ponerlo en el estado del arte o en el capítulo de desarrollo del trabajo?    
- ¿Debería de poner el modelo de portatil que utilizo para comparar los tiempos?
- Cambiar en la memoria la explicación de como y donde hago la limpieza de kdd_cup99.  
- Lo de que n_jobs= -1 solo utilice los cores avaible solo lo he visto en la pag que me paso la profe, pero en la documentación no veo que digan nada de eso.
	
- Volver a hacer los calculos de el tiempo que tarda en idle para cada uno de los modelos sin validación cruzada, para ponerlo que no se si los tiempos que he puesto están bien.  
	
	**Tutoría 29/2/22:**  
	
	- Memoria:   
		* Antes de explicar los difrentes componenetes hacer un apartado del contexto teórico de Raspberry y ML. ML en IoT, proyectos en los que se utilizar ML...  
		* Estado del arte. Fusionar dentro de sistema operativo la sección de el entorno de paquetes.  
		* Dentro del apartado de Python hacer subsecciones para Jupiter, librerías...  
		* A futuro habrá que añadir un apartado para describir los sensores que se han utilizado.  

		* En el capítulo 3 poner lo  pirmero el apartado de arquitectura general y en este apartado hacer primero una generalización, poner un poco en contexto. En que consiste el proyecto, añadir un diagrama que explique la estructura general.  
		* Explicación más profunda de los modelos usados (me ayuda Felipe).  
		* Al final del capítulo 3 poner las características del entorno de pruebas, es decir, características del PC y Raspberry.    

		* Capítulo 4: 1. Experimentos con la Raspberry, 2. Experimentos con el PC, 3. Comparativas (ayudandome de tablas, pedir ayuda a Felipe).     

	- [x] Hacer script para ejecutar todos los modelos consecutivamente y guardar en un fichero los tiempos (hacerlo probando con el dataset de Ocuppancy para tardar menos).    

	- Hacer una página web estática con los objetivos del proyecto, donde se indique donde está el código, resultados...A poder ser en inglés.   
