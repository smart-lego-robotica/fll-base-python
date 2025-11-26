from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task
from Chassi import Chassi, Speed

from Anexo import Anexo
from Hub import Hub
from SoundEffects import SoundEffects

# Missão D - Missão Compartilhada e pega extração
async def run(chassi: Chassi, anexo: Anexo, hub: Hub, soundEffects: SoundEffects):
    await multitask(
        anexo.girarMotorDireita(-60,600),
        anexo.girarMotorEsquerda(50,600),

        chassi.seguirReto(-890, Speed.VERY_FAST)
    )


    await chassi.seguirReto(130, Speed.SLOW)
    await chassi.virar(-92, Speed.VERY_FAST)
    # await chassi.seguirReto(190, Speed.SLOW)


    await multitask(
        chassi.seguirReto(190, Speed.SLOW),
        anexo.girarMotorDireita(graus=-100, velocidade=50)

    )


    await multitask(
        anexo.girarMotorEsquerda(-850,500),
        anexo.girarMotorDireita(-350, 400)
    )


    await chassi.seguirReto(-210, Speed.DEFAULT) #sair extração segura
    await chassi.virar(66, Speed.SLOW) 


    await chassi.seguirReto(250, Speed.VERY_FAST)



    await multitask(
        anexo.girarMotorEsquerda(graus=600, velocidade=600), # Abaixar descoberta para cair
        chassi.seguirReto(-200, Speed.SLOW)
    )

    # Teste pescoço
    await multitask(
        chassi.virar(angulo=-28, velocidade=Speed.VERY_FAST),
        anexo.girarMotorDireita(graus=500, velocidade=600),
        anexo.girarMotorEsquerda(graus=-200, velocidade=600)

    )


    await chassi.seguirReto(380, Speed.VERY_FAST)   # Ir até o pescoço
    await multitask(
        chassi.virar(-25, Speed.DEFAULT),
        wait(1000),
        race=True
    )
    # await chassi.virar(-25, Speed.DEFAULT)

    await chassi.virar(25, Speed.VERY_FAST)
    await chassi.seguirReto(-400, Speed.VERY_FAST)



    # Volta para a base
    await chassi.virar(angulo=80, velocidade=Speed.VERY_FAST)

    await multitask(
        anexo.girarMotorDireita(graus=-400, velocidade=600),
        chassi.seguirReto(600, Speed.VERY_FAST)
    )
    chassi.stop()
    await soundEffects.beep(frequencia=200, duracao=100)


    await multitask(
        chassi.piscarTemporizador(4000),
        soundEffects.beep(frequencia=700, duracao=4000)

    )
    
    await soundEffects.beep(frequencia=200, duracao=100)


    # Realiza as entregas dos elementos

    await chassi.seguirReto(550, Speed.VERY_FAST)
    
    await multitask(
        chassi.seguirReto(-200, Speed.SLOW),
        anexo.girarMotorDireita(graus=350, velocidade=600)

    )
    await anexo.girarMotorDireita(-200,350)
    await chassi.seguirReto(150, Speed.SLOW)
    await chassi.seguirReto(-500, Speed.VERY_FAST)


    
if __name__ == "__main__":
    hub = Hub()
    chassi = Chassi(hub)
    anexo = Anexo(hub)
    soundEffects =  SoundEffects(hub=hub.hub)
    run_task(run(chassi, anexo, hub, soundEffects))