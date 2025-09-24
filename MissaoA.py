from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task
from Chassi import Chassi, Speed

from Anexo import Anexo
from Hub import Hub

# Missão A - Derruba pedra, vira o negocio, e abaixa o balde
async def run(chassi: Chassi, anexo: Anexo, hub: Hub): 
    await chassi.seguirReto(681)
    await chassi.virar(50, Speed.SLOW)
    await chassi.seguirReto(80, Speed.SLOW)
    await anexo.girarAmbos(-458, 458, 400) # Abaixar para pegar
    await chassi.seguirReto(47)
    await anexo.girarAmbos(-350, 350, -400) # Levantar
    await wait(1000)
    await chassi.seguirReto(-30)


    await chassi.virar(-50, Speed.SLOW)
    await chassi.virar(50)

    await chassi.seguirReto(-57)
    await chassi.virar(-50)
    await chassi.seguirReto(76)
    await chassi.virar(-42) # Faz a missão de virar
    await chassi.virar(40)



    await chassi.seguirReto(-50)
    await chassi.virar(-90)
    await chassi.seguirReto(-350, Speed.FAST)  # Da ré para empurrar as pedras
    
    await chassi.seguirReto(250)
    await chassi.virar(-5)
    await chassi.seguirReto(170)
    await anexo.girarAmbos(-500,500,900) # Abaixar para abaixar balde
    await chassi.virar(8)
    await chassi.virar(-2)
    await anexo.girarAmbos(450, -450, 400) # Voltar para posição normal

    await chassi.seguirReto(-50)
    await chassi.virar(65) #virar e ajeitar
    await chassi.seguirReto(-152)
    await chassi.virar(-105) #virar para empurrar
    await chassi.seguirReto(210) #empurrar pino vermelho
    await chassi.seguirReto(-210)

    await chassi.virar(150) #voltar para base
    await chassi.seguirReto(-500, Speed.FAST)




 



if __name__ == "__main__":
    hub = Hub()
    chassi = Chassi(hub)
    anexo = Anexo(hub)
    run_task(run(chassi, anexo, hub))