from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task
from Chassi import Chassi, Speed
from SoundEffects import SoundEffects
from Anexo import Anexo
from Hub import Hub

# Missão B - Rodar engrenagem e pegar Scale pan   (10 e 11)
async def run(chassi: Chassi, anexo: Anexo, hub: Hub, soundEffects: SoundEffects): 
    await soundEffects.beep()

    await chassi.seguirReto(240, Speed.VERY_FAST) 
    await chassi.virar(45, Speed.VERY_FAST)
    await chassi.seguirReto(260, Speed.VERY_FAST)
    await anexo.girarMotorEsquerda(500,-700)

    await soundEffects.beep()
    await chassi.virar(10, Speed.VERY_FAST)
    await multitask(

        chassi.seguirReto(-200, Speed.DEFAULT),
        anexo.girarMotorEsquerda(210, 100)
    )
    await multitask(

        chassi.seguirReto(-400, Speed.FAST),
        anexo.girarMotorEsquerda(80, 700)
    )


    await soundEffects.beep()

    chassi.stop()

    await multitask(
        anexo.girarMotorEsquerda(250, 700),
        soundEffects.beep(frequencia=700, duracao=2000)
    )



    # Chega na base
    # await wait(3000)
    await soundEffects.beep(frequencia=400, duracao=1000)

    # await wait(200)


    await chassi.seguirReto(870, Speed.FAST)
    await chassi.virar(-88)
    await chassi.seguirReto(90, Speed.SLOW) # Aproxima da missão

    # Faz a missão de levantar girando a engrenagem

    await multitask(
        anexo.girarMotorDireita(1800,-500),
        chassi.virar(-18,Speed.FAST)
    )


    await chassi.seguirReto(-90, Speed.FAST)
    await chassi.virar(30,Speed.FAST)         

    await chassi.seguirReto(-300, Speed.FAST)
    await wait(500)
    await chassi.seguirReto(100, Speed.VERY_FAST)    # Coleta o negocio de ré
    await chassi.virar(75, Speed.VERY_FAST)
    await chassi.seguirReto(950,Speed.VERY_FAST) # Chega na outra base



if __name__ == "__main__":
    hub = Hub()
    chassi = Chassi(hub)
    anexo = Anexo(hub)
    soundEffects =  SoundEffects(hub=hub.hub)
    run_task(run(chassi, anexo, hub, soundEffects))