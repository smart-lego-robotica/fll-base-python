from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

class Constants:
    TOP_SIDE = -Axis.X
    FRONT_SIDE = Axis.Y


class Hub:
    def __init__(self):
        self.hub = PrimeHub(top_side= Constants.TOP_SIDE, front_side= Constants.FRONT_SIDE)

    def resetarGuinada(self):
        self.hub.imu.reset_heading(0)

    def pegarGuinada(self):
        return self.hub.imu.heading()
