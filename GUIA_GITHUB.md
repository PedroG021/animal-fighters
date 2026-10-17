# Guia: publicando o Animal Fighters no GitHub

## 0. Pré-requisitos
- Python 3.12+ instalado (`python --version`)
- Git instalado (`git --version`)
- Conta no GitHub

## 1. Organize a pasta do projeto
A pasta final deve ficar assim:

```text
animal-fighters/
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── champions.py
├── helper.py
├── project.py
└── test_project.py
```

> A pasta `.venv` **não** vai para o GitHub. Ela é local (cada pessoa cria a sua) e o `.gitignore` já a ignora.
> Quem baixar o projeto recria o ambiente com `requirements.txt`.

## 2. Crie o ambiente virtual (.venv)
Dentro da pasta do projeto:

```bash
python -m venv .venv
```

Ative:
- Windows PowerShell: `.venv\Scripts\Activate.ps1`
- Windows CMD: `.venv\Scripts\activate.bat`
- Linux/macOS: `source .venv/bin/activate`

Instale as dependências e teste:

```bash
pip install -r requirements.txt
pytest test_project.py
python project.py
```

> Se o PowerShell bloquear o script de ativação, rode uma vez:
> `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`

## 3. Edite dois detalhes antes de publicar
- `LICENSE`: troque `SEU NOME AQUI` pelo seu nome.
- `README.md`: troque `YOUR-USERNAME` pelo seu usuário do GitHub.

## 4. Crie o repositório no GitHub
1. Acesse https://github.com/new
2. Nome: `animal-fighters`
3. Deixe **Public**
4. **Não** marque "Add a README", ".gitignore" ou "license" (você já tem esses arquivos)
5. Clique em **Create repository**

## 5. Envie o código
Na pasta do projeto, com o terminal aberto:

```bash
git init
git branch -M main
git add .
git status
git commit -m "Initial commit: Animal Fighters CLI game"
git remote add origin https://github.com/SEU-USUARIO/animal-fighters.git
git push -u origin main
```

Confira no `git status` (antes do commit) que `.venv/` e `__pycache__/` **não** aparecem na lista.

Na primeira vez, o Git pode pedir login. Use um Personal Access Token como senha
(GitHub → Settings → Developer settings → Personal access tokens) ou o GitHub CLI (`gh auth login`).

## 6. Depois de publicado
- Adicione uma descrição e *topics* (`python`, `cli-game`, `rpg`, `cs50p`) na página do repositório.
- Para atualizar no futuro:
  ```bash
  git add .
  git commit -m "Descreva a mudança"
  git push
  ```

## Opcional: checagens de qualidade
O `requirements.txt` já inclui `mypy` e `black`:

```bash
black .
mypy .
```
