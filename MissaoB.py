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

    await chassi.seguirReto(200) 
    await chassi.virar(45)
    await chassi.seguirReto(260)
    await anexo.girarMotorEsquerda(400,-500)
    await chassi.seguirReto(-200, Speed.SLOW)   # Levanta o negocio
    await chassi.seguirReto(20)
    await anexo.girarMotorEsquerda(-200,-400)
    await soundEffects.beep()


    await multitask(
        anexo.girarMotorEsquerda(graus=200, velocidade=500),
        chassi.seguirReto(-400,Speed.FAST)

    )
    await soundEffects.beep()
    chassi.stop()

    await wait(2500)
    await soundEffects.beep()
    await wait(200)


    await chassi.seguirReto(870, Speed.FAST)
    await chassi.virar(-94)
    await chassi.seguirReto(90, Speed.SLOW)

    await multitask(
        anexo.girarMotorDireita(1800,-500),
        chassi.virar(-20,Speed.FAST)         
    )
    await chassi.seguirReto(-90, Speed.FAST)
    await chassi.virar(35,Speed.FAST)         

    await chassi.seguirReto(-300, Speed.FAST)
    await chassi.seguirReto(100, Speed.FAST)
    await wait(500)
    await chassi.virar(70)
    await chassi.seguirReto(950,Speed.FAST)
    await chassi.virar(-90,Speed.FAST)
    await chassi.seguirReto(150,Speed.FAST)



if __name__ == "__main__":
    hub = Hub()
    chassi = Chassi(hub)
    anexo = Anexo(hub)
    soundEffects =  SoundEffects(hub=hub.hub)
    run_task(run(chassi, anexo, hub, soundEffects))