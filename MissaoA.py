from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task
from Chassi import Chassi, Speed

from Anexo import Anexo
from Hub import Hub

# Missão A - Derruba pedra, virar a 
async def run(chassi: Chassi, anexo: Anexo, hub: Hub): 
    await chassi.seguirReto(681, Speed.FAST) 
    await chassi.virar(47, Speed.FAST) 
    await chassi.seguirReto(70, Speed.SLOW)
    await anexo.girarAmbos(-400, 400, 700) # Abaixar para pegar
    await chassi.seguirReto(47, Speed.FAST)
    await anexo.girarAmbos(-350, 350,-400) # Levantar
    await wait(200)
    await chassi.seguirReto(-25, Speed.FAST)


    await chassi.virar(-50, Speed.FAST) 
    await chassi.virar(50, Speed.FAST)

    await chassi.seguirReto(-62,Speed.FAST)
    await chassi.virar(-50, Speed.FAST)
    await chassi.seguirReto(76, Speed.FAST)
    await chassi.virar(-40, Speed.FAST) # Faz a missão de virar
    await chassi.virar(41, Speed.FAST)



    await chassi.seguirReto(-65) 
    await chassi.virar(-94, Speed.FAST)
    await chassi.seguirReto(-350, Speed.FAST)  # Da ré para empurrar as pedras
    
    await chassi.virar(5, Speed.FAST)

    await chassi.seguirReto(170,Speed.FAST)
    await chassi.virar(-39, Speed.FAST) #virar e ajeitar
    await chassi.seguirReto(600)

    
    await chassi.virar(50, Speed.FAST) #virar e ajeitar
    await chassi.seguirReto(-500, Speed.FAST)



 



if __name__ == "__main__":
    hub = Hub()
    chassi = Chassi(hub)
    anexo = Anexo(hub)
    run_task(run(chassi, anexo, hub))