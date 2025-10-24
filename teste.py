from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task
from Chassi import Chassi, Speed

from Anexo import Anexo
from Hub import Hub

# Missão F -
async def run(chassi: Chassi, anexo: Anexo, hub: Hub):
    await chassi.seguirReto(distancia=0.00, velocidade=Speed.VERY_FAST)
    await chassi.seguirReto(distancia=406.00, velocidade=Speed.VERY_FAST)
    await chassi.virar(angulo=86.89, velocidade=Speed.VERY_FAST)
    await chassi.seguirReto(distancia=231.00, velocidade=Speed.VERY_FAST)
    await chassi.seguirReto(distancia=-236.00, velocidade=Speed.VERY_FAST)
    await chassi.virar(angulo=-88.96, velocidade=Speed.VERY_FAST)
    await chassi.seguirReto(distancia=-423.00, velocidade=Speed.VERY_FAST)


    
if __name__ == "__main__":
    hub = Hub()
    chassi = Chassi(hub)
    anexo = Anexo(hub)
    run_task(run(chassi, anexo, hub))