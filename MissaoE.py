from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task
from Chassi import Chassi, Speed

from Anexo import Anexo
from Hub import Hub

# Missão E - Descobrir areia do barco (Operação de resgate)
async def run(chassi: Chassi, anexo: Anexo, hub: Hub, soundEffects: SoundEffects):
    await soundEffects.beep()
    
    await chassi.seguirReto(-580, Speed.VERY_FAST)
    await chassi.seguirReto(550, Speed.VERY_FAST)

    await soundEffects.beep()

    chassi.stop()

    await soundEffects.beep(frequencia=600, duracao=2000)
    await soundEffects.beep(frequencia=400, duracao=1000)



    await chassi.seguirReto(520)

    await chassi.seguirReto(-190, Speed.FAST)   # Puxar areia


    await chassi.seguirReto(150, Speed.SLOW)    # Empurrar barco
    await chassi.seguirReto(110, Speed.SLOW)    # Empurrar barco

    await chassi.virar(5)  # Voltar
    await chassi.seguirReto(-600)



    
if __name__ == "__main__":
    hub = Hub()
    chassi = Chassi(hub)
    anexo = Anexo(hub)
    soundEffects =  SoundEffects(hub=hub.hub)

    run_task(run(chassi, anexo, hub, soundEffects))