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
    await chassi.virar(45, Speed.VERY_FAST) #ficar na direção para a missão
    await chassi.seguirReto(240, Speed.VERY_FAST)
    await anexo.girarMotorEsquerda(500,-700) #fazer missão balança

    await soundEffects.beep()
    await chassi.virar(8, Speed.VERY_FAST)
    await multitask(
        chassi.seguirReto(-200, Speed.DEFAULT),
        anexo.girarMotorEsquerda(200, 100)
    )
    await multitask(
        chassi.seguirReto(150, Speed.FAST),
        anexo.girarMotorEsquerda(265, 700)
    )
    await chassi.virar(-50, Speed.VERY_FAST)
    await chassi.seguirReto(-450, Speed.FAST),
        
   

    await soundEffects.beep()

    chassi.stop()

    await multitask(
        soundEffects.beep(frequencia=700, duracao=2000),
        chassi.piscarTemporizador(2000)
    )



    # Chega na base
    await soundEffects.beep(frequencia=400, duracao=1000)


    await chassi.seguirReto(850, Speed.FAST)
    await chassi.virar(-83)
    await chassi.seguirReto(120, Speed.DEFAULT) # Aproxima da missão

    # Faz a missão de levantar girando a engrenagem

    await multitask(
        anexo.girarMotorDireita(-1150,800),
        chassi.virar(-18, Speed.SLOW),
        race=True
    )
    await chassi.virar(12, Speed.VERY_FAST),


    # await chassi.seguirReto(-90, Speed.FAST)
    # await chassi.virar(18,Speed.FAST)         

    await chassi.seguirReto(-330, Speed.FAST)
    await chassi.seguirReto(100, Speed.VERY_FAST)    # Coleta o negocio de ré


    await chassi.virar(85, Speed.VERY_FAST)


    await chassi.curva(1800, -30, Speed.VERY_FAST)
    # await chassi.seguirReto(950,Speed.VERY_FAST) # Chega na outra base



if __name__ == "__main__":
    hub = Hub()
    chassi = Chassi(hub)
    anexo = Anexo(hub)
    soundEffects =  SoundEffects(hub=hub.hub)
    run_task(run(chassi, anexo, hub, soundEffects))