# AutoCheckin

O presente projeto tem como único propósito servir como um lembrete para que as pessoas não esqueçam de realizar o check-in durante seus períodos de estudo, o autoCheckin foi desenvolvido para eliminar a necessidade de alarmes sonoros intrusivos, permitindo, ainda, que o check-in seja feito automaticamente em segundo plano, vale ressaltar que o check-in só pode ser efetuado dentro do campus, sendo necessário estar conectado a uma das redes disponíveis.

**O autoCheckin só funcionará enquanto o computador estiver ligado!**

## Guia de Instalação

### 1. Clonar o Repositório
O primeiro passo consiste em clonar este repositório em sua máquina. Caso encontre dificuldades, é possível realizar a instalação manual, acessando as tags do projeto e instalando o source_code. No entanto, esta abordagem implica em limitações de atualização. Para evitar esse problema, é recomendável clonar o repositório, permitindo futuras atualizações através do comando `git pull`.

```bash
git clone https://github.com/mateusbepplerpereira/autoCheckin.git
```

### 2. Instalação do Python
Certifique-se de ter o Python 3.12.2 ou uma versão superior instalada em sua máquina. Caso necessário, faça o download em [Instalação do Python](https://www.python.org/downloads/).

### 3. Instalação das Bibliotecas Python
No terminal, execute o seguinte comando para instalar as bibliotecas necessárias listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 3.1 Erro: pip não é reconhecido como um comando interno
Se encontrar esse erro, siga as instruções detalhadas no [passo a passo](https://dicasdeprogramacao.com.br/resolvido-pip-nao-e-reconhecido-como-um-comando-interno/) do blog "Dicas de Programação".

### 4. Instalação do Firefox
O projeto utiliza a biblioteca Selenium com o geckodriver para simulação do navegador Firefox. Certifique-se de realizar a instalação padrão do Firefox através do link [Instalação do navegador Firefox](https://www.mozilla.org/pt-BR/firefox/download/thanks/).

### 5. Configuração das Variáveis de Ambiente
No terminal, na pasta raiz do projeto, execute o comando:

```bash
cp config/.env.example config/.env
```

Dentro do arquivo `.env`, configure as variáveis de ambiente conforme as instruções:

- `RUN`: Controla o funcionamento do autoCheckin. Configure como "True" para ativação e "False" para desativação temporária.
- `EMAIL_ADALOVE`: Insira o e-mail de acesso da Adalove.
- `PASSWORD_ADALOVE`: Insira a senha de acesso da Adalove.

### **Segurança de Dados**
Os dados no arquivo .env ficam armazenados localmente, sem qualquer vazamento ou disponibilização externa.

### 6. Adicionar Atalho na Pasta de Inicialização do Windows
Adicione o arquivo "autoCheckin - Atalho.lnk" à pasta de inicialização do Windows para que o bot seja executado automaticamente ao ligar o computador. Pressione **"WINDOWS" + "R"** e cole o comando:

```bash
%appdata%\Microsoft\windows\start menu\programs\startup
```

Copie o arquivo "autoCheckin - Atalho.lnk" do repositório e cole no diretório aberto.

## Conclusão
Ao seguir este guia, você estará apto a executar o autoCheckin de forma automática em seu computador. Em caso de complicações na instalação ou sugestões de melhorias, entre em contato pelo Slack: **mateus.pereira**.

## Versões
- [v1.0.0 - 23/02/2024](https://github.com/mateusbepplerpereira/autoCheckin/releases/tag/v1.0.0)
- [v1.1.0 - 23/02/2024](https://github.com/mateusbepplerpereira/autoCheckin/releases/tag/v1.1.0)
- [v1.1.1 - 26/02/2024](https://github.com/mateusbepplerpereira/autoCheckin/releases/tag/v1.1.1)
