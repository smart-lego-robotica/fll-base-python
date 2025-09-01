# 🤖 Projeto FLL - Base Pybricks

Este repositório contém uma estrutura de projeto em **Python
(Pybricks)** para equipes da **FIRST LEGO League (FLL)**. O objetivo é
servir como **base** para organização, manutenção e expansão da
programação do robô.

------------------------------------------------------------------------

## 📂 Estrutura do Projeto

    ├── Anexo.py      # Código relacionado ao uso de anexos/mecanismos adicionais
    ├── Chassi.py     # Funções principais de movimentação do robô (chassi/base)
    ├── Hub.py        # Configuração e inicialização do hub (motores, portas, sensores)
    ├── MissaoA.py    # Estratégia e programação da Missão A
    ├── MissaoB.py    # Estratégia e programação da Missão B
    └── menu.py       # Ponto de entrada do programa (seleção de missões)

Essa organização permite separar cada parte do robô em **módulos
independentes**, tornando o código mais limpo, reutilizável e fácil de
manter.

------------------------------------------------------------------------

## ⚙️ Especificações Técnicas

### 🔩 Chassi

-   **Motor Esquerdo:** Porta A (rotação no sentido anti-horário)
-   **Motor Direito:** Porta E (rotação no sentido horário)
-   **Diâmetro da Roda:** 62 mm
-   **Distância entre Rodas (Axle Track):** 80 mm
-   **Sensores Suportados:**
    -   Giroscópio interno do hub
    -   Sensores adicionais podem ser configurados em `Hub.py`

### 🔧 Anexo

-   **Motor Esquerdo do Anexo:** Porta B
-   **Motor Direito do Anexo:** Porta F

------------------------------------------------------------------------

## 🛠️ Personalização

-   Crie novos arquivos para cada missão: `MissaoC.py`, `MissaoD.py`,
    etc.
-   Adicione novas funções no `Chassi.py` para diferentes movimentações
    do robô.
-   Atualize `menu.py` para incluir as novas opções de missões.
-   Configure novos motores e sensores no `Hub.py` sempre que houver
    mudanças no robô.

------------------------------------------------------------------------

## 🔋 Nível de Bateria

A cor do indicador representa o nível atual da bateria com base na voltagem medida:

| Cor         | Nível da Bateria | Faixa de Voltagem      |
|-------------|------------------|-------------------------|
| 🟢 Verde    | Bateria Cheia    | > 8200 mV               |
| 🟡 Amarelo  | Bateria Média    | 7500 mV – 8200 mV       |
| 🔴 Vermelho | Bateria Fraca    | < 7500 mV               |
