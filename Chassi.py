from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

class Speed:
    """
        straight_speed
        straight_acceleration
        turn_rate
        turn_acceleration

    """
    SLOW = [100, 200, 500, 800]
    DEFAULT = [400, 400, 500, 800]
    FAST = [1000, 800, 1200, 800]



class Constants:
    PORT_LEFT_MOTOR = Port.A
    LEFT_POSITIVE_DIRECTION = Direction.COUNTERCLOCKWISE

    PORT_RIGHT_MOTOR = Port.E
    RIGHT_POSITIVE_DIRECTION = Direction.CLOCKWISE

    WHEEL_DIAMETER = 62
    AXLE_TRACK = 80


class Chassi:
    def __init__(self, hub):
        self.hub = hub
        LEFT_MOTOR = Motor(port= Constants.PORT_LEFT_MOTOR, positive_direction= Constants.LEFT_POSITIVE_DIRECTION)
        RIGHT_MOTOR = Motor(port= Constants.PORT_RIGHT_MOTOR, positive_direction= Constants.RIGHT_POSITIVE_DIRECTION)
        self.driveBase = DriveBase(
            left_motor= LEFT_MOTOR,
            right_motor= RIGHT_MOTOR,
            wheel_diameter= Constants.WHEEL_DIAMETER,
            axle_track= Constants.AXLE_TRACK
        )
        # (7558, 0, 1889, 6, 11)
        # kp, kd, ki, integral_deadzone, integral_rate
        self.driveBase.heading_control.pid(9000, 0, 2500, 70, 11)
        self.driveBase.use_gyro(use_gyro=True)

    def setSpeed(self, velocidade):
        self.driveBase.settings(
            straight_speed= velocidade[0],
            straight_acceleration= velocidade[1],
            turn_rate= velocidade[2],
            turn_acceleration= velocidade[3]
        )

    async def seguirReto(self, distancia, velocidade=Speed.DEFAULT):
        self.setSpeed(velocidade)
        await self.driveBase.straight(distance= distancia, then=Stop.HOLD)

    async def virar(self, angulo, velocidade=Speed.DEFAULT):
        self.setSpeed(velocidade)
        await self.driveBase.turn(angle= angulo, then=Stop.HOLD)

    async def curva(self, raio, angulo, velocidade=Speed.DEFAULT):
        self.setSpeed(velocidade)
        await self.driveBase.curve(radius= raio, angle= angulo, then=Stop.HOLD)

    def stop(self):
        self.driveBase.stop()