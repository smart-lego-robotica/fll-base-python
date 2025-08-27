from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from Chassi import Chassi, Speed
from Anexo import Anexo
from Hub import Hub


async def run(chassi: Chassi, anexo: Anexo, hub: Hub):
    for i in range(4):
        await chassi.seguirReto(300, Speed.FAST)
        await chassi.virar(90, Speed.FAST)
    await chassi.seguirReto(300, Speed.FAST)
