from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task
from Chassi import Chassi, Speed

from Anexo import Anexo
from Hub import Hub

# Missão D - Descobrir areia do barco (Operação de resgate)
async def run(chassi: Chassi, anexo: Anexo, hub: Hub):
    await chassi.seguirReto(450)

    await chassi.seguirReto(-130, Speed.SLOW)   # Puxar areia


    await chassi.seguirReto(150, Speed.SLOW)    # Empurrar barco
    await chassi.seguirReto(110, Speed.SLOW)    # Empurrar barco

    await chassi.virar(10)  # Voltar
    await chassi.seguirReto(-600)



    
if __name__ == "__main__":
    hub = Hub()
    chassi = Chassi(hub)
    anexo = Anexo(hub)
    run_task(run(chassi, anexo, hub))