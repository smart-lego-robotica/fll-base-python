from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

class Constants:
    """
    Constantes de configuração do Hub.

    Attributes:
        TOP_SIDE (Axis): Eixo superior do Hub (orientação).
        FRONT_SIDE (Axis): Eixo frontal do Hub (orientação).
    """

    TOP_SIDE = -Axis.X
    FRONT_SIDE = Axis.Y


class Hub:
    """
    Classe responsável pelo gerenciamento do PrimeHub.

    Permite configurar a orientação do Hub, além de acessar e
    manipular a guinada (heading) do giroscópio interno.

    Attributes:
        hub (PrimeHub): Instância do Hub principal.
    """

    def __init__(self):
        """
        Inicializa o Hub com a orientação definida em `Constants`.
        """
        self.hub = PrimeHub(top_side= Constants.TOP_SIDE, front_side= Constants.FRONT_SIDE)

    def resetarGuinada(self):
        """
        Reseta a guinada (heading) do giroscópio para 0 graus.

        Example:
            hub.resetarGuinada()
        """
        self.hub.imu.reset_heading(0)

    def pegarGuinada(self):
        """
        Obtém o valor atual da guinada (heading) do giroscópio.

        Returns:
            int: Ângulo atual em graus, relativo à orientação definida.

        Example:
            angulo = hub.pegarGuinada()
            print(angulo)  # ex: 45
        """
        return self.hub.imu.heading()
