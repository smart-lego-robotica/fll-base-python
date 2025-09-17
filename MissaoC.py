from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task
from Chassi import Chassi, Speed

from Anexo import Anexo
from Hub import Hub


async def run(chassi: Chassi, anexo: Anexo, hub: Hub):
    await chassi.seguirReto(-890, Speed.FAST)
    await chassi.seguirReto(168, Speed.SLOW)
    await chassi.virar(-96, Speed.SLOW)
    await chassi.seguirReto(220, Speed.SLOW)
    await anexo.girarMotorEsquerda(78,200)
    await anexo.girarMotorDireita(-400, 800)
    
if __name__ == "__main__":
    hub = Hub()
    chassi = Chassi(hub)
    anexo = Anexo(hub)
    run_task(run(chassi, anexo, hub))