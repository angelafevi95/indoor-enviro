<<<<<<< HEAD
# Indoor monitoring

This project contains the necessary scripts to generate documents and upload them on MongoDB Atlas. 

The scripts are written un Python code. 

## Software Requierements

To execute this projects will be needed:
- Python version 2 and 3
- Pip 


## Hardware Requirements

This projects uses the following hardware to work: 
- Raspberry Pi (2)
- Pimoroni Enviro
- A/D MCP3008
- MQ2 sensor

## Script List

Below can be found a list of the existing scripts contained in this project:
- enviro.py : object that provide us with weather values
- indoor_gas.py: main clase to execute in order to obtain gas values. 
    -- Requierements: MCP3008.py, mq.py and mongoDB.py objects.
- main_indoor_monitor.py: uses Pimoroni Enviro weather values to create a MongoDB document
    -- Requierements: enviro.py and mongoDB.py


## Installation and usage

The document requirements.txt already contains all the Python Libraries to be used. 
Use the following code on your terminal

>> pip install requirements.txt

Finally, we need to use the following lines to measure the enviromental values chosen: 

>> python main_indoor_monitor.py
>> python3 indoor_gas.py


---------------------

Angela Fernandez Vilches  | Universidad de Granada | Trabajo Fin de Grado|
Diseño de nodos inalámbricos para la monitorización de las condiciones ambientales de trabajo | 2020 
=======
# indoor-enviro
>>>>>>> f8de5c2878293cc4eea0864d08722707aab1640f
