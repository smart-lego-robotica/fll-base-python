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



hub = Hub()
sound = SoundEffects(hub= hub.hub)
chassi = Chassi(hub= hub)
anexo = Anexo(hub= hub)

sound.ligarRobo()
missionSelected = hub_menu("A", "B")

while True:
    if (missionSelected == "A"):
        sound.iniciarMissao()

        run_task(MissaoA.run(chassi= chassi, anexo= anexo, hub= hub))
        chassi.stop()
        sound.finalizarMissao()

        missionSelected = hub_menu("B", "A")

    elif (missionSelected == "B"):
        sound.iniciarMissao()

        run_task(MissaoB.run(chassi= chassi, anexo= anexo, hub= hub))
        chassi.stop()
        sound.finalizarMissao()

        missionSelected = hub_menu("A", "B")
