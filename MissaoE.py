from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task
from Chassi import Chassi, Speed

from Anexo import Anexo
from Hub import Hub

# Missão E - Rodar engrenagem e pegar Scale pan   (10 e 11)
async def run(chassi: Chassi, anexo: Anexo, hub: Hub): 
    await chassi.seguirReto(830)
    await chassi.virar(-80)
    await   chassi.seguirReto(100, Speed.SLOW)

    await multitask(
        anexo.girarMotorDireita(1700,-500),
        chassi.virar(-15,)         
    )
    await chassi.seguirReto(-290)
    await chassi.seguirReto(150,Speed.FAST)
    await chassi.curva(100,-75,Speed.FAST)
    await chassi.seguirReto(630,Speed.FAST)



if __name__ == "__main__":
    hub = Hub()
    chassi = Chassi(hub)
    anexo = Anexo(hub)
    run_task(run(chassi, anexo, hub))