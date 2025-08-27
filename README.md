# 🤖 Projeto FLL - Base Pybricks

Este repositório contém uma estrutura de projeto em **Python (Pybricks)** para equipes da **FIRST LEGO League (FLL)**.  
O objetivo é servir como **base** para organização, manutenção e expansão da programação do robô, facilitando a colaboração da equipe.

---

## 📂 Estrutura do Projeto

```
├── Anexo.py      # Código relacionado ao uso de anexos/mecanismos adicionais
├── Chassi.py     # Funções principais de movimentação do robô (chassi/base)
├── Hub.py        # Configuração e inicialização do hub (motores, portas, sensores)
├── MissaoA.py    # Estratégia e programação da Missão A
├── MissaoB.py    # Estratégia e programação da Missão B
└── menu.py       # Ponto de entrada do programa (seleção de missões)
```

Essa organização permite separar cada parte do robô em **módulos independentes**, tornando o código mais limpo, reutilizável e fácil de manter.

---

## 🛠️ Personalização

- Crie novos arquivos para cada missão: `MissaoC.py`, `MissaoD.py`, etc.  
- Adicione novas funções no `Chassi.py` para diferentes movimentações do robô.  
- Atualize `menu.py` para incluir as novas opções de missões.  
- Configure novos motores e sensores no `Hub.py` sempre que houver mudanças no robô.

---

## 👥 Contribuindo

Este projeto foi feito para ajudar a equipe FLL a **trabalhar em conjunto**.  
Sugestões de melhorias, novas estratégias e ideias são sempre bem-vindas!  
