from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task
from Chassi import Chassi, Speed

from Anexo import Anexo
from Hub import Hub

# Missão D - Missão Compartilhada e pega extração
async def run(chassi: Chassi, anexo: Anexo, hub: Hub):

    await anexo.girarMotorDireita(-100,600)
    await chassi.seguirReto(-890)
    await chassi.seguirReto(155, Speed.SLOW)
    await chassi.virar(-95)
    await wait (1000)
    await chassi.seguirReto(180, Speed.SLOW)
    await multitask(
        anexo.girarMotorEsquerda(-850,500),
        anexo.girarMotorDireita(-450, 400)
    )

    await chassi.virar(-10)

    await chassi.seguirReto(-200) #sair extração segura
    await chassi.virar(75, Speed.SLOW) 

    await multitask(
        chassi.seguirReto(200,Speed.FAST), # entregar extração segura 
        anexo.girarMotorEsquerda(800,600)
    )
   
    await chassi.seguirReto(-100, Speed.FAST)
    await chassi.virar(50, Speed.FAST)

    
    await chassi.seguirReto(550, Speed.FAST)
    
if __name__ == "__main__":
    hub = Hub()
    chassi = Chassi(hub)
    anexo = Anexo(hub)
    run_task(run(chassi, anexo, hub))