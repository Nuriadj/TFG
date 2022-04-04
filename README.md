# TFG
Repositorio para ir subiendo todos los avances respecto a mi Tfg que vaya realizando

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
	|SVM | 5 seg | 6 seg | 6 seg | 6 seg|
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
	Con el 10% todo bien, he podido convertirlo en binario (código de [Download_dataSet](https://github.com/Nuriadj/TFG/blob/main/kdd_cup99/Download_dataSet.ipynb)).  
	Con el 100% no he podido pasarlo a clasificación binaria, la propia Raspberry se queda un rato pillada y luego ella sola lo mata. He probado a ejecutarlo en el teminal (porque con notebook después de un rato pillada perdia la conexión con el kernel) pero después de estar pillada un rato aparece un mensaje de Killed y temina la ejecución. De momento haré las pruebas solo con el 10%.  
	
	- De ese 10% voy a utilizar el 70% para entrenar y 30% para validar. En la primera fila hay columnas que tienen valores extraños como 0.00.1 por lo que para quitarlo elimino la primera fila. Y quitar la primera columna que es el índice. He hecho que el csv que se guarda no contenga ni la cabecera ni el indice (primera fila y primera columna) ya está preparado para directamente utilizarlo. Esto se hace también en [Download_dataSet](https://github.com/Nuriadj/TFG/blob/main/kdd_cup99/Download_dataSet.ipynb)  
 
	- Quito la columna 19 y 20 porque contienen todo el rato el mismo valor (en ambos casos el cero). Se pone axis= 1 para indicar que se quiere eliminar la columna 19 (no la fila) e inplace se pone a true para que la variable dataset sea "actualizada".  
	
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
	|Regresión logística| 16 seg // **13 seg** | |||
	|Random forest |||||  	
	
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
