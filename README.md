# AutoCheckin

O presente projeto não possui nenhum fim ílicito, o autoCheckin possui apenas a finalidade de ser um lembrete para que as pessoas não esqueçam de realizar o checkin, de tal forma que não será nessessário o uso de alarmes de sonoridade no meio dos periodos de estudo, além disso o autoCheckin possibilita que o checkin seja feito de forma automática em segundo plano, dessa forma economizando tempo que pode ser direcionado a outras tarefas, deixando claro que o checkin só consegue ser realizado dentro do campus, nessessitando que você esteja conectado em uma das redes do mesmo.

## Guia de instalação##

### 1. Clonar o seguinte repositório
O primeiro passo é clonar este repositório em sua máquina
```

git clone https://github.com/mateusbepplerpereira/autoCheckin.git

```

### 2.Instalação do Python
Para o seguinte projeto é nessessário a instalação do Python 3.12.2 ou superior; pode ser instalado no seguinte link [Instalação do Python](https://www.python.org/downloads/)

### 3.Instalação das bibliotecas utilizadas pelo Python
No terminal cole o seguinte comando:
```

pip install -r requirements.txt

```

## 4.Configuração das variaveis de ambiente
Abra o terminal na pasta raiz do projeto e cole este comando
```

cp config/.env.example config/.env

```
#### RUN
Dentro do arquivo .env você encontrará a variavel de ambiente "RUN", essa váriavel controla o funcionamento do autoCheckin, caso você queira parar a execução do bot temporariamente deixe RUN="False", os valores permitidos são "True" e "False".
#### EMAIL_ADALOVE
Dentro do arquivo .env você encontrará a váriavel de ambiente "EMAIL_ADALOVE", você deve colocar o seu e-mail de acesso da Adalove.
#### PASSWORD_ADALOVE
Dentro do arquivo .env você encontrará a váriavel de ambiente "PASSWORD_ADALOVE", você deve colocar a sua senha do acesso da Adalove.
#### ***SEGURANÇA DE DADOS**
Todos os dados que você escrever no arquivo .env ficarão salvos apenas na sua máquina, **os dados desse documento não serão vazados ou disponibilizados em nenhum local**.

