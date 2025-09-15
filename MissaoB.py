from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task
from Chassi import Chassi, Speed

from Anexo import Anexo
from Hub import Hub


async def run(chassi: Chassi, anexo: Anexo, hub: Hub):
    await chassi.curva(490, -45)
    await chassi.virar(80)
    await chassi.seguirReto(220, Speed.FAST) #bater no pino 
    await chassi.seguirReto(-180, Speed.FAST) 
    await chassi.seguirReto(400) #frente antes 2
    await chassi.virar(-80)
    await chassi.seguirReto(150) #missão 2
    await anexo.girarMotorDireita(-500,300) 
    await chassi.seguirReto(50)
    await chassi.seguirReto(-250)





if __name__ == "__main__":
    hub = Hub()
    chassi = Chassi(hub)
    anexo = Anexo(hub)
    run_task(run(chassi, anexo, hub))