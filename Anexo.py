from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.tools import wait, StopWatch, multitask

class Speed:
    """
    Perfis de velocidade para os motores do anexo.

    Attributes:
        SLOW (list[int]): Movimento lento [velocidade, aceleração, --, --].
        DEFAULT (list[int]): Movimento padrão [velocidade, aceleração, --, --].
    """

    SLOW = [100, 200, 500, 800]
    DEFAULT = [100, 200, 500, 800]


class Constants:    
    """
    Constantes de configuração dos motores do anexo.

    Attributes:
        PORT_LEFT_MOTOR (Port): Porta do motor esquerdo.
        LEFT_POSITIVE_DIRECTION (Direction): Direção positiva do motor esquerdo.

        PORT_RIGHT_MOTOR (Port): Porta do motor direito.
        RIGHT_POSITIVE_DIRECTION (Direction): Direção positiva do motor direito.
    """
    
    PORT_LEFT_MOTOR = Port.B
    LEFT_POSITIVE_DIRECTION = Direction.COUNTERCLOCKWISE

    PORT_RIGHT_MOTOR = Port.F
    RIGHT_POSITIVE_DIRECTION = Direction.CLOCKWISE


class Anexo:
    """
    Classe responsável pelo controle dos motores de anexos do robô.

    Permite controlar motores adicionais conectados ao robô
    (por exemplo, braços ou garras).

    Attributes:
        hub (PrimeHub): Hub principal.
        leftMotor (Motor): Motor esquerdo do anexo.
        rightMotor (Motor): Motor direito do anexo.
    """

    def __init__(self, hub):
        """
        Inicializa os motores do anexo.

        Args:
            hub (PrimeHub): Hub principal do robô.
        """

        self.hub = hub
        self.leftMotor = Motor(port= Constants.PORT_LEFT_MOTOR, positive_direction= Constants.LEFT_POSITIVE_DIRECTION)
        self.rightMotor = Motor(port= Constants.PORT_RIGHT_MOTOR, positive_direction= Constants.RIGHT_POSITIVE_DIRECTION)


    def resetarLeftMotor(self):
        """
        Reseta o ângulo do motor esquerdo para 0 graus.

        Example:
            anexo.resetarLeftMotor()
        """
        self.leftMotor.reset_angle(0)

    def resetarRightMotor(self):
        """
        Reseta o ângulo do motor direito para 0 graus.

        Example:
            anexo.resetarRightMotor()
        """
        self.rightMotor.reset_angle(0)

    async def girarMotorEsquerda(self, graus, velocidade):
        """
        Gira o motor esquerdo um número de graus.

        Args:
            graus (int): Ângulo de rotação em graus.
            velocidade (int): Velocidade de rotação (graus/s).

        Example:
            await anexo.girarMotorEsquerda(graus=90, velocidade=500)
        """
        await self.leftMotor.run_angle(speed= velocidade, rotation_angle= graus, then=Stop.HOLD)

    async def girarMotorDireita(self, graus, velocidade):
        """
        Gira o motor direito um número de graus.

        Args:
            graus (int): Ângulo de rotação em graus.
            velocidade (int): Velocidade de rotação (graus/s).

        Example:
            await anexo.girarMotorDireita(graus=90, velocidade=500)
        """
        await self.rightMotor.run_angle(speed= velocidade, rotation_angle= graus, then=Stop.HOLD)

    def girarAmbos(self, grausEsquerda, grausDireita):
        """
        Gira os dois motores do anexo simultaneamente.

        Args:
            grausEsquerda (int): Ângulo para o motor esquerdo em graus.
            grausDireita (int): Ângulo para o motor direito em graus.
            velocidade (int): Velocidade de rotação (graus/s).

        Example:
            await anexo.girarAmbos(grausEsquerda=90, grausDireita=45, velocidade=400)
        """
        await multitask(
            self.girarMotorEsquerda(graus= grausEsquerda),
            self.girarMotorDireita(graus= grausDireita)
        )

    def stopLeft(self):
        """
        Interrompe imediatamente o motor esquerdo.
        """
        self.leftMotor.stop()

    def stopRight(self):
        """
        Interrompe imediatamente o motor direito.
        """
        self.rightMotor.stop()