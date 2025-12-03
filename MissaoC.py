from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task
from Chassi import Chassi, Speed

from Anexo import Anexo
from Hub import Hub

# Missão  C - Pegando Pincel e virando o negocio
async def run(chassi: Chassi, anexo: Anexo, hub: Hub):
    """

        await chassi.seguirReto(500, Speed.FAST)
        await chassi.seguirReto(200, Speed.FAST)
        await chassi.seguirReto(-200, Speed.FAST)

        await chassi.virar(50)

        await chassi.seguirReto(260)
        await chassi.virar(-95, Speed.DEFAULT)

        await chassi.seguirReto(280, Speed.DEFAULT)
        await chassi.virar(10, Speed.FAST)
        await chassi.virar(-10, Speed.FAST)


        await multitask(
            chassi.seguirReto(-190, Speed.FAST),
            anexo.girarMotorDireita(-250, 500) #pegar negocio verde
        )

        await chassi.virar(-46)

        await wait(500)

        await multitask(
            anexo.girarMotorEsquerda(-350, 600),

            chassi.seguirReto(120, Speed.SLOW)
        )

        await anexo.girarMotorEsquerda(300, 600),

        await chassi.seguirReto(-170, Speed.FAST)
        await chassi.virar(120, Speed.FAST)
        await chassi.seguirReto(-810, Speed.FAST)
        # )
    """
    
    await chassi.seguirReto(distancia=720.00, velocidade=Speed.VERY_FAST)
    await chassi.seguirReto(distancia=-164.00, velocidade=Speed.VERY_FAST)
    await chassi.seguirReto(distancia=210.00, velocidade=Speed.VERY_FAST)
    await chassi.seguirReto(distancia=-60.00, velocidade=Speed.VERY_FAST)
    await chassi.virar(-10, Speed.VERY_FAST)
    await chassi.seguirReto(distancia=50, velocidade=Speed.VERY_FAST)
    await chassi.seguirReto(-30,Speed.VERY_FAST)
    await anexo.girarMotorEsquerda(graus=280, velocidade=200)
    await anexo.girarMotorEsquerda(graus=180, velocidade=-700)



    await chassi.virar(10, Speed.DEFAULT)

    await chassi.seguirReto(distancia=75, velocidade=Speed.DEFAULT)

    await multitask (
        anexo.girarMotorEsquerda(graus=160, velocidade=-500),
        chassi.seguirReto(distancia=100, velocidade=Speed.DEFAULT)

    )

    await anexo.girarMotorEsquerda(graus=150, velocidade=700)


    await chassi.virar(-7, Speed.DEFAULT)
    await chassi.seguirReto(7)
    await multitask(
        anexo.girarMotorDireita(graus=400, velocidade=-600),   # Coletar negocio
        chassi.seguirReto(distancia=-10, velocidade=Speed.SLOW)
    )


    await chassi.seguirReto(distancia=-10, velocidade=Speed.VERY_FAST)


    await chassi.virar(angulo=-3, velocidade=Speed.VERY_FAST)

    
    await multitask (
          chassi.seguirReto(distancia=-80.00, velocidade=Speed.VERY_FAST),
          anexo.girarMotorEsquerda(graus=-70,velocidade=600),
          chassi.seguirReto(distancia=-700.00, velocidade=Speed.VERY_FAST)
    )


if __name__ == "__main__":
    hub = Hub()
    chassi = Chassi(hub)
    anexo = Anexo(hub)
    run_task(run(chassi, anexo, hub))