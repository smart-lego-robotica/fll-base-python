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
    await chassi.seguirReto(680, Speed.VERY_FAST) 
    await chassi.virar(47, Speed.VERY_FAST) 
    # await chassi.seguirReto(70, Speed.DEFAULT)
    # await anexo.girarAmbos(-400, 400, 700) # Abaixar para pegar
    # await chassi.seguirReto(47, Speed.SLOW)

    await multitask(
        chassi.seguirReto(117, Speed.SLOW),
        anexo.girarAmbos(-400, 400, 700)
    )

    await anexo.girarAmbos(-350, 350,-400) # Levantar
    await wait(200)
    await chassi.seguirReto(-40, Speed.VERY_FAST)


    await chassi.virar(-50, Speed.DEFAULT) #fazer pedras
    
    await chassi.seguirReto(-57,Speed.VERY_FAST)
    await chassi.virar(-10, Speed.VERY_FAST)
    await chassi.seguirReto(95, Speed.VERY_FAST)

    await chassi.virar(-23, Speed.DEFAULT), # Faz a missão de virar

    await chassi.virar(40, Speed.VERY_FAST)



    await chassi.seguirReto(-65, Speed.VERY_FAST) 
    await chassi.virar(-91, Speed.VERY_FAST)
    await chassi.seguirReto(-350, Speed.VERY_FAST)  # Da ré para empurrar as pedras
    
    await chassi.seguirReto(170,Speed.VERY_FAST)
    await chassi.virar(-45, Speed.VERY_FAST) #virar e ajeitar
    await chassi.seguirReto(650, Speed.VERY_FAST)

    
    await chassi.virar(60, Speed.VERY_FAST) #virar e ajeitar
    await chassi.seguirReto(-600, Speed.VERY_FAST)



 



if __name__ == "__main__":
    hub = Hub()
    chassi = Chassi(hub)
    anexo = Anexo(hub)
    run_task(run(chassi, anexo, hub))