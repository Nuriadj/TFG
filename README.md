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
	- sudo apt install python3-rpi.gpio  (para que no de error hay que ejecutarlo con sudo).
