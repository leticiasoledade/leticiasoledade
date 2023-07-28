#!/usr/bin/env pybricks-micropython
# importação da biblioteca micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# configuração da motor da garra
gripper_motor = Motor(Port.A)

# Configuração elbow motor (cotovelo do motor), sentido antihorário (valores positivos fazem os braços se moverem)
elbow_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE, [8, 40])

# motor da base
base_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE, [12, 36])

# configuração sensor de toque
touch_sensor = TouchSensor(Port.S1)

# configuração sensor de cor (luz refletida)
color_sensor = ColorSensor(Port.S3)

#PEGA

# inicialização da garra
gripper_motor.run_until_stalled(200, Stop.COAST, 50)
gripper_motor.reset_angle(0)

#SOBE 

# inicialização elbow motor
elbow_motor.run_target(60, -45)
elbow_motor.run_target(60, 0, Stop.HOLD)
elbow_motor.run_time(-30, 100)
elbow_motor.run(15)
while color_sensor.reflection() < 30:
    wait(10)
elbow_motor.stop(Stop.HOLD)
elbow_motor.reset_angle(0)

#VIRA 

#Base
base_motor.run(-60)
while not touch_sensor.pressed():
    wait(10)
base_motor.stop(Stop.HOLD)
base_motor.reset_angle(0)

#DESCE

#Finalização elbow motor
elbow_motor.run_target(60, -50)

#SOLTA

#Finalização da garra
gripper_motor.run_target(200, -90)

#SOBE2

#Retorno elbow motor
elbow_motor.run_target(60, -45)
elbow_motor.run_target(60, 0, Stop.HOLD)
elbow_motor.run_time(-30, 100)
elbow_motor.run(15)
while color_sensor.reflection() < 30:
    wait(10)
elbow_motor.stop(Stop.HOLD)
elbow_motor.reset_angle(0)

#VIRA 

#Base
#Gire a base para o centro 
CENTER= 100
base_motor.run_target(60, CENTER, Stop.HOLD)

#DESCE

#Finalização elbow motor
elbow_motor.run_target(60, -50)


# - - - - - - - - - - - PARTE 2 (Retorno)- - - - - - - - - #

#SOBE 

# inicialização elbow motor
elbow_motor.run_target(60, -45)
elbow_motor.run_target(60, 0, Stop.HOLD)
elbow_motor.run_time(-30, 100)
elbow_motor.run(15)
while color_sensor.reflection() < 30:
    wait(10)
elbow_motor.stop(Stop.HOLD)
elbow_motor.reset_angle(0)

#VIRA 

#Base
base_motor.run(-60)
while not touch_sensor.pressed():
    wait(10)
base_motor.stop(Stop.HOLD)
base_motor.reset_angle(0)''

#DESCE

#Finalização elbow motor
elbow_motor.run_target(60, -50)


# inicialização da garra
gripper_motor.run_until_stalled(200, Stop.COAST, 50)
gripper_motor.reset_angle(0)

#SOBE 

# inicialização elbow motor
elbow_motor.run_target(60, -45)
elbow_motor.run_target(60, 0, Stop.HOLD)
elbow_motor.run_time(-30, 100)
elbow_motor.run(15)
while color_sensor.reflection() < 30:
    wait(10)
elbow_motor.stop(Stop.HOLD)
elbow_motor.reset_angle(0)

#VIRA 

#Base
#Gire a base para o centro 
CENTER= 100
base_motor.run_target(60, CENTER, Stop.HOLD)

#DESCE

#Finalização elbow motor
elbow_motor.run_target(60, -50)

#SOLTA

#Finalização da garra
gripper_motor.run_target(200, -90)

# ------------ RETORNO FINAL ------------- #
#SOBE3

#Retorno elbow motor
elbow_motor.run_target(60, -45)
elbow_motor.run_target(60, 0, Stop.HOLD)
elbow_motor.run_time(-30, 100)
elbow_motor.run(15)
while color_sensor.reflection() < 30:
    wait(10)
elbow_motor.stop(Stop.HOLD)
elbow_motor.reset_angle(0)

#VIRA 

#Base
#Base
base_motor.run(-60)
while not touch_sensor.pressed():
    wait(10)
base_motor.stop(Stop.HOLD)
base_motor.reset_angle(0)
#DESCE

#Finalização elbow motor
elbow_motor.run_target(60, -50)
