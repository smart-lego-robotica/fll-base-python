from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task
from Chassi import Chassi, Speed

from Anexo import Anexo
from Hub import Hub


async def run(chassi: Chassi, anexo: Anexo, hub: Hub):


    await chassi.seguirReto(-890)
    await chassi.seguirReto(155, Speed.SLOW)
    await chassi.virar(-97)
    await chassi.seguirReto(180, Speed.SLOW)
    await anexo.girarMotorEsquerda(-800,300)

    await wait(1000)

    await chassi.seguirReto(-50)

    await anexo.girarMotorDireita(-500, 700)

    await chassi.seguirReto(-100)
    await chassi.virar(50, Speed.FAST)

    await chassi.virar(-90, Speed.FAST)
    await chassi.seguirReto(-100, Speed.FAST)

    await chassi.virar(-40, Speed.FAST)
    await chassi.seguirReto(-750, Speed.FAST)


    #await anexo.girarMotorEsquerda(650,600)
    #await chassi.seguirReto(100, Speed.SLOW)


    
if __name__ == "__main__":
    hub = Hub()
    chassi = Chassi(hub)
    anexo = Anexo(hub)
    run_task(run(chassi, anexo, hub))