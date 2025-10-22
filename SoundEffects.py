from pybricks.tools import wait
from pybricks.hubs import PrimeHub

class SoundEffects:
    """
    Sons auxiliares para indicar eventos do robô:
    início/fim de missão, entrega e controle da garra.
    """

    def __init__(self, hub: PrimeHub):
        """Recebe o hub para usar o alto-falante."""
        self.hub = hub
    
    def ligarRobo(self):
        """Som de inicialização do robô."""

        self.hub.speaker.beep()

        self.hub.speaker.beep(600, 120)
        wait(50)
        self.hub.speaker.beep(800, 150)
        wait(50)
        self.hub.speaker.beep(1000, 200)

    def iniciarMissao(self):
        """Som curto de início de missão."""
        self.hub.speaker.beep(800, 150)
        wait(50)
        self.hub.speaker.beep(1000, 200)

    def finalizarMissao(self):
        """Som de finalização de missão."""
        self.hub.speaker.beep(1000, 150)
        wait(50)
        self.hub.speaker.beep(700, 300)

    def entregarElemento(self):
        """Som de entrega/realização de missão."""
        self.hub.speaker.beep(900, 150)
        wait(50)
        self.hub.speaker.beep(1100, 150)
        wait(50)
        self.hub.speaker.beep(1300, 250)

    def pegarElemento(self):
        """Som ao pegar algum elemento."""
        self.hub.speaker.beep(600, 150)
        wait(50)
        self.hub.speaker.beep(900, 200)

    async def beep(self, frequencia=600, duracao=40):
        """
        Realiza um beep para sinalizar algo

        Args:
            frequencia (int): Frequencia do som emitido.
            duracao (int): Duracação do som emitido.

        Example:
            await sound.beep(frequencia=50, duracao=100)
        """
        await self.hub.speaker.beep(frequency= frequencia, duration= duracao)
