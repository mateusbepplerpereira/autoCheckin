# AutoCheckin

O presente projeto não possui nenhum fim ílicito, o autoCheckin possui apenas a finalidade de ser um lembrete para que as pessoas não esqueçam de realizar o checkin, de tal forma que não será necessário o uso de alarmes de sonoridade no meio dos periodos de estudo, além disso o autoCheckin possibilita que o checkin seja feito de forma automática em segundo plano, dessa forma economizando tempo que pode ser direcionado a outras tarefas, deixando claro que o checkin só consegue ser realizado dentro do campus, necessitando que você esteja conectado em uma das redes do mesmo.

## Guia de instalação

### 1. Clonar o seguinte repositório
O primeiro passo é clonar este repositório na sua máquina:


**Caso você estiver com dificuldades para clonar este repositório, também é possível realizar a instalação manual dele, acessando as tags do projeto e instalar o source_code, caso você opte por esta instalação manual você tera a limitação de atualização, caso existam futuras atualizações você precisará reinsatalar manualmente o projeto (Isso só se aplica a instalação manual, clonando o repositório, com um git pull você puxa as novas atualizações)**
```

git clone https://github.com/mateusbepplerpereira/autoCheckin.git

```

### 2. Instalação do Python
Para o seguinte projeto é nessessário a instalação do Python 3.12.2 ou superior; pode ser instalado no seguinte link [Instalação do Python](https://www.python.org/downloads/)

### 3. Instalação das bibliotecas utilizadas pelo Python
No terminal cole o seguinte comando:
```

pip install -r requirements.txt

```

## 4. Instalação do FireFox
Este projeto utiliza a biblioteca Selenium, essa biblioteca é responável pelo ambiente de simulação do navegador, para este projeto utilizei o geckodriver, simulador de ambiente do navegador FireFox, para que ele rode normalmente você deve realizar a instalação padrão do navegador FireFox. [Instalação do navegador FireFox](https://www.mozilla.org/pt-BR/firefox/download/thanks/)


## 5. Configuração das variaveis de ambiente
Abra o terminal na pasta raiz deste projeto e cole este comando
```

cp config/.env.example config/.env

```
#### RUN
Dentro do arquivo .env você encontrará a variavel de ambiente "RUN", essa váriavel controla o funcionamento do autoCheckin, caso você queira parar a execução do bot temporariamente deixe RUN="False", os valores permitidos são "True" e "False".
#### EMAIL_ADALOVE
Dentro do arquivo .env você encontrará a váriavel de ambiente "EMAIL_ADALOVE", você deve colocar o seu e-mail de acesso da Adalove.
#### PASSWORD_ADALOVE
Dentro do arquivo .env você encontrará a váriavel de ambiente "PASSWORD_ADALOVE", você deve colocar a sua senha do acesso da Adalove.
### ***SEGURANÇA DE DADOS**
Todos os dados que você escrever no arquivo .env ficarão salvos apenas na sua máquina, **os dados desse documento não serão vazados ou disponibilizados em nenhum local**.

## 6. Adicionar o atalho na pasta de inicialização do windowns
Agora que o ambiente já está configurado, vamos adicionar o arquivo "autoCheckin - Atalho.lnk" dentro da pasta de arquivos de inicialização do windowns para que o bot seja executado toda vez ao ligar a máquina. Pressione **"WINDOWS" + "R"** e cole o seguinte comando:


**Existe a possibilidade de você não conseguir copiar e colar o comando inteiro! Caso não consiga digite o comando**
```

%appdata%\Microsoft\windows\start menu\programs\startup

```
Após isso copie o arquivo "autoCheckin - Atalho.lnk" deste repositório e cole no diretório aberto.

## CONCLUSÃO
Após seguir o passo a passo descrito neste documento, você já será capaz de rodar de forma automática o autoCheckin em seu computador. Caso você tenha complicações na instalação deste projeto ou caso tenha alguma ideia de complementação do projeto, entre em contato comigo! Segue o meu Slack: **mateus.pereira**.

## Versões
### [v1.0 - 23/02/2024](https://github.com/mateusbepplerpereira/autoCheckin/releases/tag/v1.0)
