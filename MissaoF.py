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
    await chassi.seguirReto(400)
    await anexo.girarMotorDireita(-300, 400)
    await anexo.girarMotorDireita(200, 500)
    await anexo.girarMotorDireita(-250, 400)
    await anexo.girarMotorDireita(200, 500)
    await wait(500)
    await anexo.girarMotorDireita(-200, 600)
    await anexo.girarMotorDireita(400, 300)


if __name__ == "__main__":
    hub = Hub()
    chassi = Chassi(hub)
    anexo = Anexo(hub)
    run_task(run(chassi, anexo, hub))