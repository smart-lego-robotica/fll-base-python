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
        self.hub.display.orientation(up=Side.RIGHT)
        self.hub.system.set_stop_button(Button.BLUETOOTH)
        self.verificarNivelBateria()

    def verificarNivelBateria(self):
        """
        Verifica o nível da bateria do Hub e acende o LED indicador.

        O método mede a tensão da bateria e exibe o estado usando
        o LED central do Hub, com base nos seguintes intervalos:

            - 🟢 Verde: Bateria carregada (voltagem > 8200 mV)
            - 🟡 Amarelo: Nível médio (7500 < voltagem <= 8200 mV)
            - 🔴 Vermelho: Bateria fraca (voltagem <= 7500 mV)

        Example:
            hub.verificarNivelBateria()
            # O LED acenderá em verde, amarelo ou vermelho dependendo do nível.
    """
        voltage = self.hub.battery.voltage()
        print(voltage)
        if (voltage > 8200):
            # Carregada
            self.hub.light.on(Color.GREEN)
        elif (voltage > 7500 and voltage <= 7900):
            # Médio
            self.hub.light.on(Color.YELLOW)
        else:
            # Descarregada
            self.hub.light.on(Color.RED)


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
