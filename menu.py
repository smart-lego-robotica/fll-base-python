from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu, run_task
from Chassi import Chassi
from Anexo import Anexo
from Hub import Hub
from SoundEffects import SoundEffects



import MissaoA
import MissaoB
import MissaoC
import MissaoD
import MissaoE


hub = Hub()
sound = SoundEffects(hub= hub.hub)
chassi = Chassi(hub= hub)
anexo = Anexo(hub= hub)

sound.ligarRobo()
missionSelected = hub_menu("A", "B", "C", "D", "E")

while True:
    if (missionSelected == "A"): # Lado Azul
        sound.iniciarMissao()

        run_task(MissaoA.run(chassi= chassi, anexo= anexo, hub= hub))
        chassi.stop()
        sound.finalizarMissao()

        missionSelected = hub_menu("B", "A")

    elif (missionSelected == "B"): # Lado Azul
        sound.iniciarMissao()

        run_task(MissaoB.run(chassi= chassi, anexo= anexo, hub= hub, soundEffects=sound))
        chassi.stop()
        sound.finalizarMissao()

        missionSelected = hub_menu("C", "A", "B")

    elif (missionSelected == "C"): # Lado Vermelho
        sound.iniciarMissao()

        run_task(MissaoC.run(chassi= chassi, anexo= anexo, hub= hub))
        chassi.stop()
        sound.finalizarMissao()

        missionSelected = hub_menu("D", "C")

    elif (missionSelected == "D"): # Lado Vermelho
        sound.iniciarMissao()

        run_task(MissaoD.run(chassi= chassi, anexo= anexo, hub= hub))
        chassi.stop()
        sound.finalizarMissao()

        missionSelected = hub_menu("E", "D")

    elif (missionSelected == "E"): # Lado Vermelho
        sound.iniciarMissao()

        run_task(MissaoE.run(chassi= chassi, anexo= anexo, hub= hub))
        chassi.stop()
        sound.finalizarMissao()

        missionSelected = hub_menu("D", "E")