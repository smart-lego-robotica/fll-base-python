from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task
from Chassi import Chassi, Speed
from SoundEffects import SoundEffects
from Anexo import Anexo
from Hub import Hub

# Função para mostrar informações formatadas
def mostrarInformacoes(posicaoAtual: int, distancia: float, heading: float):
    print("\n" + "="*30)
    print(f"📍 Posição {posicaoAtual}")
    print("-"*30)
    print(f"📏 Distância percorrida: {distancia:>7.2f} mm")
    print(f"🧭 Ângulo de heading:    {heading:>7.2f}°")
    print("="*30 + "\n")

# Função principal assíncrona
async def run(chassi: Chassi, anexo: Anexo, hub: Hub, soundEffects: SoundEffects):
    def resetarDados():
        hub.hub.imu.reset_heading(angle=0)
        chassi.driveBase.reset(distance=0, angle=0)

    def pegarHeading():
        return hub.hub.imu.heading()

    def pegarDistancia():
        return chassi.driveBase.distance()

    posicaoAtual = 1

    await soundEffects.beep()
    print("🔄 Inicializando...")
    print("▶️ Aperte o botão central para começar")

    while Button.CENTER not in hub.hub.buttons.pressed():
        pass

    await soundEffects.beep(300, 200)
    resetarDados()

    while True:
        print(f"\n⏳ Aguardando leitura da {posicaoAtual}ª posição...")
        print("▶️ Aperte o botão central para registrar")

        while Button.CENTER not in hub.hub.buttons.pressed():
            pass

        await soundEffects.beep(300, 200)

        while Button.CENTER in hub.hub.buttons.pressed():
            pass

        await soundEffects.beep(100, 10)
        await soundEffects.beep(200, 50)
        await soundEffects.beep(500, 130)

        # Coleta e exibe os dados formatados
        distancia = pegarDistancia()
        heading = pegarHeading()
        mostrarInformacoes(posicaoAtual, distancia, heading)

        resetarDados()
        posicaoAtual += 1

# Execução principal
if __name__ == "__main__":
    hub = Hub()
    chassi = Chassi(hub)
    anexo = Anexo(hub)
    soundEffects = SoundEffects(hub=hub.hub)
    run_task(run(chassi, anexo, hub, soundEffects))
