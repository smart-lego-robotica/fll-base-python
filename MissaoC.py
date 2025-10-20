from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task
from Chassi import Chassi, Speed

from Anexo import Anexo
from Hub import Hub

# Missão  C - Pegando Pincel e virando o negocio
async def run(chassi: Chassi, anexo: Anexo, hub: Hub):
    await chassi.seguirReto(500, Speed.FAST)
    await chassi.seguirReto(200, Speed.FAST)
    await chassi.seguirReto(-200, Speed.FAST)

    await chassi.virar(50)

    await chassi.seguirReto(260)
    await chassi.virar(-95, Speed.DEFAULT)

    await chassi.seguirReto(300, Speed.SLOW)
    await chassi.virar(10, Speed.FAST)
    await chassi.virar(-10, Speed.FAST)

    await chassi.seguirReto(-30, Speed.FAST)
    await anexo.girarMotorDireita(-250, 700) #pegar negocio verde
    await chassi.seguirReto(-170, Speed.FAST)

    await chassi.virar(-42)
    await anexo.girarMotorEsquerda(-570, 600) 

    await wait(500)
    await chassi.seguirReto(110, Speed.SLOW)

    await anexo.girarMotorEsquerda(300, 600),

    await chassi.seguirReto(-170, Speed.FAST)
    await chassi.virar(120, Speed.FAST)
    await chassi.seguirReto(-810, Speed.FAST)
    # )





if __name__ == "__main__":
    hub = Hub()
    chassi = Chassi(hub)
    anexo = Anexo(hub)
    run_task(run(chassi, anexo, hub))