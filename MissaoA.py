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
    await chassi.seguirReto(740, Speed.VERY_FAST) 
    await chassi.virar(43, Speed.DEFAULT)

    await multitask(
        chassi.seguirReto(125, Speed.SLOW),
        anexo.girarAmbos(-330, 300, -700)
    )

    await anexo.girarAmbos(-350, 350,400) # Levantar
    await wait(200)
    await chassi.seguirReto(-35, Speed.VERY_FAST)


    await multitask(
        chassi.virar(-95, Speed.SLOW), #fazer pedras
        wait(2000),
        race=True
    )


    await chassi.seguirReto(-90, Speed.VERY_FAST) 
    await chassi.virar(-57, Speed.VERY_FAST)
    await chassi.seguirReto(-350, Speed.VERY_FAST)  # Da ré para empurrar as pedras
    
    await chassi.seguirReto(250,Speed.VERY_FAST)
    await chassi.virar(-44, Speed.VERY_FAST) #virar e ajeitar
    await chassi.seguirReto(650, Speed.VERY_FAST)

    
    await chassi.virar(60, Speed.VERY_FAST) #virar e ajeitar
    await chassi.seguirReto(-600, Speed.VERY_FAST)



 



if __name__ == "__main__":
    hub = Hub()
    chassi = Chassi(hub)
    anexo = Anexo(hub)
    run_task(run(chassi, anexo, hub))