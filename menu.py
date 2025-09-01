from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu, run_task
from Chassi import Chassi
from Anexo import Anexo
from Hub import Hub

import MissaoA
import MissaoB


missionSelected = hub_menu("A", "B")

hub = Hub()
chassi = Chassi(hub= hub)
anexo = Anexo(hub= hub)


while True:
    if (missionSelected == "A"):
        run_task(MissaoA.run(chassi= chassi, anexo= anexo, hub= hub))
        chassi.stop()
        missionSelected = hub_menu("B", "A")

    elif (missionSelected == "B"):
        run_task(MissaoB.run(chassi= chassi, anexo= anexo, hub= hub))
        chassi.stop()

        missionSelected = hub_menu("A", "B")
