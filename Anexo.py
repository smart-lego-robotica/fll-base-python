from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask

class Speed:
    SLOW = [100, 200, 500, 800]
    DEFAULT = [100, 200, 500, 800]


class Constants:
    PORT_LEFT_MOTOR = Port.B
    LEFT_POSITIVE_DIRECTION = Direction.COUNTERCLOCKWISE

    PORT_RIGHT_MOTOR = Port.F
    RIGHT_POSITIVE_DIRECTION = Direction.CLOCKWISE


class Anexo:
    def __init__(self, hub):
        self.hub = hub
        self.leftMotor = Motor(port= Constants.PORT_LEFT_MOTOR, positive_direction= Constants.LEFT_POSITIVE_DIRECTION)
        self.rightMotor = Motor(port= Constants.PORT_RIGHT_MOTOR, positive_direction= Constants.RIGHT_POSITIVE_DIRECTION)


    def resetarLeftMotor(self):
        self.leftMotor.reset_angle(0)

    def resetarRightMotor(self):
        self.rightMotor.reset_angle(0)

    def setSpeed(self, velocidade):
        self.driveBase.settings(
            straight_speed= velocidade[0],
            straight_acceleration= velocidade[1],
            turn_rate= velocidade[2],
            turn_acceleration= velocidade[3]
        )

    async def girarMotorEsquerda(self, graus, velocidade):
        await self.leftMotor.run_angle(speed= velocidade, rotation_angle= graus, then=Stop.HOLD)

    async def girarMotorDireita(self, graus, velocidade):
        await self.rightMotor.run_angle(speed= velocidade, rotation_angle= graus, then=Stop.HOLD)

    def girarAmbos(self, grausEsquerda, grausDireita):
        await multitask(
            self.girarMotorEsquerda(graus= grausEsquerda),
            self.girarMotorDireita(graus= grausDireita)
        )

    def stopLeft(self):
        self.leftMotor.stop()

    def stopRight(self):
        self.rightMotor.stop()