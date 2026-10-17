🇺🇸 [English](README.md) | 🇧🇷 Português

# Animal Fighters

#### Vídeo de Demonstração: <https://youtu.be/HC67CvCWaks?si=LUa3g9nLADjX3Ni3>

## Descrição
Um jogo de RPG 1v1 por turnos, no estilo clássico, que roda diretamente no terminal (CLI). O jogo é baseado em recursos de texto, formatação de texto e efeitos de texto usando as bibliotecas `sys` e `time`, com programação orientada a objetos. Cada lutador animal é um objeto com suas próprias habilidades, dano, vida, nome e figura. Os campeões só são criados quando o jogador os escolhe; o programa usa aleatoriedade com a biblioteca `random` para escolher o lutador animal da CPU e quem começa a luta. Quem zerar a vida primeiro perde a luta. O usuário e a CPU têm um turno cada. Quando a luta termina, o vencedor é exibido e o programa volta para o menu. Por fim, o projeto inclui testes em `test_project.py` que cobrem cada função importante, usando monkeypatch para facilitar e capsys para observar os efeitos colaterais das funções.

Este projeto foi desenvolvido como Projeto Final do **CS50's Introduction to Programming with Python (CS50P)**, de Harvard University.

---

## Funcionalidades
- **Efeitos de Texto**: Todos os efeitos de luta e o design da batalha foram feitos com strings literais e bibliotecas úteis como `sys` e `time`.
- **Validação de CLI**: O projeto inclui rotinas de validação personalizadas para tratar respostas vazias, limites de opções numéricas e quantidades não positivas, de modo que o programa não quebre com entradas inválidas.
- **Testes Unitários Robustos**: Inclui testes com pytest para a lógica principal do jogo, usando monkeypatch e capsys.

---

## Estrutura de Arquivos e Arquitetura do Sistema
- **`project.py`**: O ponto de entrada do projeto. Contém o loop principal da CLI (`main()`), a seleção das opções do menu (`get_menu_choice()`), a escolha do campeão (`choose_your_champion()`) e todo o fluxo da batalha com (`start_battle()`), (`user_action_sequence()`) e (`cpu_action_sequence()`).

- **`champions.py`**: Cuida das estruturas dos campeões/lutadores, com dicionários representativos como (`animals`) e (`animals_play_number`), além do método especial (`__init__()`) que gera os lutadores, do método de classe (`create_champions()`) que retorna os campeões a serem criados, de (`get_cpu_champion()`) e (`get_user_champion()`) para acessar os valores correspondentes dentro dos dicionários, das opções de luta com (`fight_options()`), da contagem de dano de cada rodada com (`damage_count()`) e da mensagem do vencedor com (`display_winner()`).

- **`helper.py`**: Este módulo guarda funções que ajudam o projeto a rodar melhor, como obter um número válido com (`get_number()`), o efeito de texto RPG do jogo com (`rpg_text_effect()`) e todas as funções que representam o fluxo visual da batalha, ou seja, o que está acontecendo e como isso é mostrado ao usuário, com (`battle_text_round_begin()`), (`battle_text_round_end()`), (`battle_formatter()`) e (`visual_action_to_do()`).

- **`test_project.py`**: O módulo de testes das funções. Inclui testes para funções lógicas, funções de criação, validação de entrada, efeitos colaterais, `monkeypatch` e `capsys`.

---

## Decisões de Design
1. **Separação de Responsabilidades (SoC)**: O projeto foi desenhado com o objetivo de separar o código o máximo possível; por isso, cada função tem um 'trabalho' específico, o que facilita os testes. Por exemplo: o projeto não pede um número em cada função; em vez disso, uso funções do `helper` como (`get_number()`), cujo propósito de vida é obter um número válido apesar dos erros e retorná-lo.
2. **Defensividade do Projeto**: O projeto trata os erros de digitação do usuário, garantindo que o jogo não quebre durante a execução por causa dele, e que não quebre ao obter informações, como em (`get_menu_choice()`).
3. **Type Hints**: Toda função conta com type hints, o que facilita o entendimento do propósito das funções.

---

## Passo a Passo

### Pré-requisitos
- Python 3.12+

1. **Clone o repositório**
   ```bash
   git clone https://github.com/PedroG021/animal-fighters.git
   cd animal-fighters
   ```
2. **Crie um ambiente virtual** (mantém as bibliotecas do projeto isoladas)
   ```bash
   python -m venv .venv
   ```
3. **Ative o ambiente virtual**
   - Windows (PowerShell): `.venv\Scripts\Activate.ps1`
   - Windows (CMD): `.venv\Scripts\activate.bat`
   - Linux / macOS: `source .venv/bin/activate`
   
4. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```
5. **Rode os testes** (opcional, mas recomendado)
   ```bash
   pytest test_project.py
   ```
6. **Inicie o jogo**
   ```bash
   python project.py
   ```
7. **Jogue**: escolha `3` no menu, escolha seu animal pelo número jogável (1-5) e, a cada turno, digite `1` (ataque básico), `2` (habilidade) ou `3` (fugir). Quem zerar a vida primeiro perde.

---

## Links Importantes Recebidos via Duck AI Para as Funções do Projeto

Para o Efeito de Texto RPG:
https://docs.python.org/3/library/sys.html |
https://docs.python.org/3/library/time.html

Para a Aleatoriedade no Jogo:
https://docs.python.org/3/library/random.html

Para Testar Funções Complexas de Maneira Mais Simples:
https://docs.pytest.org/en/stable/how-to/monkeypatch.html

Para Garantir Que Efeitos Colaterais de Funções Como `print` ou `Mensagens de Erro` Sejam Exibidos:
https://docs.pytest.org/en/stable/how-to/capture-stdout-stderr.html

Para Entender Como Passar Uma Sequência de Entradas na Mesma Linha do MonkeyPatch:
https://docs.python.org/3/library/functions.html#iter |
https://docs.python.org/3/library/functions.html#next

Para Poder Usar Type Hints Como `ANY`:
https://docs.python.org/3/library/typing.html

Ajuda Básica Para o Modelo de Arquivo README:
https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax |
https://www.freecodecamp.org/news/how-to-structure-your-readme-file/

---

## Limitações Conhecidas

- Não há persistência para o usuário, como acompanhar quantas batalhas já foram travadas, nem um espaço para que os usuários tenham suas próprias contas, com seus nomes, para guardar esses dados.
- Não há efeitos sonoros nem música de fundo.

---