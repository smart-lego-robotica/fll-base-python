from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask
from Chassi import Chassi, Speed
from Anexo import Anexo
from Hub import Hub


async def run(chassi: Chassi, anexo: Anexo, hub: Hub):
    await multitask(
        chassi.seguirReto(300),
        anexo.girarMotorDireita(700, 500)
    )
    await multitask(
        chassi.virar(-90, Speed.FAST),
        anexo.girarMotorEsquerda(400, 1000)
    )
    
    await multitask(
        chassi.seguirReto(-300, Speed.FAST),
        anexo.girarMotorDireita(700, 500)
    )
