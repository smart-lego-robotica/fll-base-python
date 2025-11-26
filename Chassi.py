from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

class Speed:
    """
    Conjunto de perfis de velocidade para o robô.

    Cada perfil define:
        - straight_speed: Velocidade de translação (mm/s)
        - straight_acceleration: Aceleração de translação (mm/s²)
        - turn_rate: Velocidade de giro (°/s)
        - turn_acceleration: Aceleração de giro (°/s²)

    Attributes:
        SLOW (list[int]): Movimento lento.
        DEFAULT (list[int]): Movimento padrão.
        FAST (list[int]): Movimento rápido.
    """

    SLOW = [100, 200, 50, 100]
    DEFAULT = [400, 400, 500, 800]
    FAST = [1000, 800, 1200, 800]

    VERY_FAST = [1000, 700, 1400, 700]



class Constants:
    """
    Constantes de configuração do robô.

    Attributes:
        PORT_LEFT_MOTOR (Port): Porta do motor esquerdo.
        LEFT_POSITIVE_DIRECTION (Direction): Direção positiva do motor esquerdo.

        PORT_RIGHT_MOTOR (Port): Porta do motor direito.
        RIGHT_POSITIVE_DIRECTION (Direction): Direção positiva do motor direito.

        WHEEL_DIAMETER (int): Diâmetro da roda em milímetros.
        AXLE_TRACK (int): Distância entre rodas (eixo) em milímetros.
    """

    PORT_LEFT_MOTOR = Port.A
    LEFT_POSITIVE_DIRECTION = Direction.COUNTERCLOCKWISE

    PORT_RIGHT_MOTOR = Port.E
    RIGHT_POSITIVE_DIRECTION = Direction.CLOCKWISE

    WHEEL_DIAMETER = 62
    AXLE_TRACK = 80

    PORT_ULTRASSONIC = Port.D


class Chassi:
    """
    Classe responsável pelo controle de movimentação do robô.

    Permite realizar deslocamentos retos, curvas e giros
    utilizando os motores do chassi.

    Attributes:
        hub (PrimeHub): Hub principal conectado ao robô.
        driveBase (DriveBase): Instância de controle de locomoção.
    """

    def __init__(self, hub):
        """
        Inicializa o chassi com motores e drive base configurados.

        Args:
            hub (PrimeHub): Hub principal do robô.
        """

        self.hub = hub
        LEFT_MOTOR = Motor(port= Constants.PORT_LEFT_MOTOR, positive_direction= Constants.LEFT_POSITIVE_DIRECTION)
        RIGHT_MOTOR = Motor(port= Constants.PORT_RIGHT_MOTOR, positive_direction= Constants.RIGHT_POSITIVE_DIRECTION)
        self.driveBase = DriveBase(
            left_motor= LEFT_MOTOR,
            right_motor= RIGHT_MOTOR,
            wheel_diameter= Constants.WHEEL_DIAMETER,
            axle_track= Constants.AXLE_TRACK
        )

        # Ajuste de PID para controle de heading
        # kp, kd, ki, integral_deadzone, integral_rate
        self.driveBase.heading_control.pid(27000, 0, 2000, 100, 30)


        # (38, 20)
        self.driveBase.heading_control.target_tolerances(speed=8, position=4)
        self.driveBase.use_gyro(use_gyro=True)

        self.ultrassonico = UltrasonicSensor(port=Constants.PORT_ULTRASSONIC)

    def setSpeed(self, velocidade):
        """
        Define a velocidade de movimento do robô.

        Args:
            velocidade (list[int]): Um dos valores da classe `Speed`.
                - Speed.SLOW : Movimento Lento
                - Speed.DEFAULT : Movimento Normal
                - Speed.FAST : Movimento Rápido

        Example:
            chassi.setSpeed(velocidade = Speed.FAST)
        """

        self.driveBase.settings(
            straight_speed= velocidade[0],
            straight_acceleration= velocidade[1],
            turn_rate= velocidade[2],
            turn_acceleration= velocidade[3]
        )

    async def seguirReto(self, distancia, velocidade=Speed.DEFAULT):
        """
        Movimenta o robô em linha reta.

        Args:
            distancia (int): Distância em milímetros.
            velocidade (list[int], opcional): Perfil de velocidade. 
                Padrão: Speed.DEFAULT.

        Example:
            await chassi.seguirReto(distancia= 300, velocidade= Speed.SLOW)
        """

        self.setSpeed(velocidade)
        await self.driveBase.straight(distance= distancia, then=Stop.HOLD)

    async def virar(self, angulo, velocidade=Speed.FAST):
        """
        Realiza um giro no próprio eixo do robô.

        Args:
            angulo (int): Ângulo em graus.
            velocidade (list[int], opcional): Perfil de velocidade.
                Padrão: Speed.DEFAULT.

        Example:
            await chassi.virar(angulo=90, velocidade=Speed.FAST)
        """

        self.setSpeed(velocidade)
        await self.driveBase.turn(angle= angulo, then=Stop.HOLD)

    async def curva(self, raio, angulo, velocidade=Speed.DEFAULT):
        """
        Movimenta o robô em curva com raio definido.

        Args:
            raio (int): Raio da curva em milímetros.
            angulo (int): Ângulo da curva em graus.
            velocidade (list[int], opcional): Perfil de velocidade.
                Padrão: Speed.DEFAULT.

        Example:
            await chassi.curva(raio=150, angulo=45, velocidade=Speed.SLOW)
        """

        self.setSpeed(velocidade)
        await self.driveBase.curve(radius= raio, angle= angulo, then=Stop.HOLD)

    def stop(self):
        """
        Interrompe imediatamente o movimento do robô.
        """

        self.driveBase.stop()

    """
    Pisca as luzes do sensor ultrassonico

    Args:
        duracao (int): duração em milisegundos.

    Example:
        await chassi.piscarLuz(duracao= 1000)
    """
    async def piscarTemporizador(self, duracao=2000):
        tempo = StopWatch()
        while tempo.time() < duracao:
            # Calcula quanto tempo falta
            restante = duracao - tempo.time()

            # Define o intervalo de piscada proporcional ao tempo restante
            # Quanto menor o tempo restante, menor o intervalo (mais rápido pisca)
            intervalo = max(50, int(restante / 20))  
            # aqui o mínimo é 50ms para não ficar rápido demais

            # Liga a luz
            await self.ultrassonico.lights.on(100)
            await wait(intervalo)

            # Desliga a luz
            await self.ultrassonico.lights.off()
            await wait(intervalo)

    def piscarQuantidade(self, quantidade=3):
        for i in range(3):
            self.ultrassonico.lights.on(100)
            wait(20)

            self.ultrassonico.lights.off()
            wait(20)

    async def loopLuzes(self, duracao=4000):
        tempo = StopWatch()
        indice = 0  # começa no LED 0
        
        while tempo.time() < duracao:
            restante = duracao - tempo.time()

            # Cria uma tupla com todos apagados
            leds = [0, 0, 0, 0]

            # Acende apenas o LED atual
            leds[indice] = 100
            await self.ultrassonico.lights.on(tuple(leds))

            await wait(20)

            # Apaga todos
            await self.ultrassonico.lights.off()
            await wait(20)

            # Avança para o próximo LED (0→1→2→3→0…)
            indice = (indice + 1) % 4