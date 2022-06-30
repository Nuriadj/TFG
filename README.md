# Entrenamiento y Aplicación de Modelos de Aprendizaje Automático en Dispositivos con Capacidad de Cómputo Limitada
### Trabajo de Fin de Grado
#### Grado en Ingenería de Robótica Software
**Autora: Nuria Díaz Jérica**  
**Tutora: Katia Leal Algara**  
**Cotutor: Felipe Ortega Soto**  

Respositorio con todo el contenido utilizado en el Trabajo de Fin de Grado.

Las carpetas: 

* [occupancy](https://github.com/Nuriadj/TFG/tree/main/occupancy)
* [kdd_cup99](https://github.com/Nuriadj/TFG/tree/main/kdd_cup99) 
* [sensors](https://github.com/Nuriadj/TFG/tree/main/sensors)

Contiene cada una su respectivo/s datasets así como los resultados obtenidos para dichos datasets en ambas máquinas.

La carpeta kdd_cup99 también contiene el fichero que se encarga de leer un porcentaje de este dataset y prepararlo para poder entrenar con él [prepare_kddcup.ipynb](https://github.com/Nuriadj/TFG/blob/main/kdd_cup99/prepare_kddcup.ipynb)

La carpeta sensors también contiene:
* Un ejemplo sencillo de como utilizar LGPIO [LDR_data_lgpio.py](https://github.com/Nuriadj/TFG/blob/main/sensors/LDR_data_lgpio.py)
* Código para generar nuestro propio dataset [read_sensors.ipynb](https://github.com/Nuriadj/TFG/blob/main/sensors/read_sensors.ipynb)

Por otra parte, la carpeta [Models](https://github.com/Nuriadj/TFG/tree/main/Models) contiene todos los códigos necesarios para generar cada uno de los modelos de aprendizaje automático que se utilizan en este proyecto.

Los ficheros [pc_enviroment.yaml](https://github.com/Nuriadj/TFG/blob/main/pc_enviroment.yaml) y [rasp_enviroment.yaml](https://github.com/Nuriadj/TFG/blob/main/rasp_enviroment.yaml) contienen una lista de todos los paquetes que se han instalado en cada entorno de conda en cada una de las máquinas.
