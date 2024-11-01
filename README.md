# hacka_forasteiros
Hackathon Magalu SECOMP UFSCAR 2024

# Interface de Linha de Comando - Gerenciador de Recursos com Terraform

Este projeto é uma interface de linha de comando (CLI) para gerenciar recursos como banco de dados, máquinas virtuais, volumes e aplicações usando o Terraform a partir de perfis de aplicações pré definidos. A CLI permite listar, criar e excluir recursos com comandos simples, integrando perfis e scripts Terraform para automação.

## Índice
- [Instalação](#instalação)
- [Uso](#uso)
  - [Banco de Dados](#banco-de-dados)
  - [Máquina Virtual](#máquina-virtual)
  - [Volume](#volume)
  - [Aplicação](#aplicação)
- [Exemplos](#exemplos)
- [Ajuda](#ajuda)

## Instalação

1. Clone o repositório:
   ```bash
   git clone <url-do-repositorio>
   cd <nome-do-repositorio>
   ```

2. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```

3. Certifique-se de que o Terraform está instalado e configurado.

4. Execute o script com o Python:
   ```bash
   python main.py
   ```

## Uso

### Banco de Dados

1. **Listar Perfis de Banco de Dados**
   ```bash
   python main.py db list
   ```

2. **Listar Perfis de Banco de Dados com todas as informações**
   ```bash
   python main.py db list --all
   ```

2. **Criar um Novo Banco de Dados**
   ```bash
   python main.py db create -f <flavor_id> -n <nome-do-banco> -u <usuario> -P <senha>
   ```
   - Parâmetros:
     - `-f` ou `--flavor_id`: ID do flavor do banco de dados
     - `-n` ou `--name`: Nome do banco de dados
     - `-u` ou `--user`: Nome de usuário do banco de dados
     - `-P` ou `--password`: Senha do banco de dados
     - `-e` ou `--engine_id`: ID do engine do banco de dados (padrão é o primeiro engine disponível)
     - `--volume_size`: Tamanho do volume em GB (padrão: 10)

### Máquina Virtual

1. **Listar Perfis de Máquina**
   ```bash
   python main.py machine list
   ```
2. **Listar Perfis de Máquina para obter todos dos dados**
   ```bash
   python main.py machine list --all
   ```
3. **Criar uma Nova Máquina Virtual**
   ```bash
   python main.py machine create -n <nome-da-maquina> -k <nome-da-chave-ssh>
   ```
   - Parâmetros:
     - `-n` ou `--name`: Nome da máquina virtual
     - `-m` ou `--machine_name`: Tipo da máquina (padrão: o primeiro tipo na lista de máquinas)
     - `-i` ou `--image_name`: Nome da imagem do sistema operacional (padrão: a primeira imagem disponível)
     - `-k` ou `--ssh_key_name`: Nome da chave SSH para acesso à máquina

### Volume

1. **Listar Volumes**
   ```bash
   python main.py volume list
   ```
2. **Criar um Novo Volume**
   ```bash
   python main.py volume create -n <nome-do-volume> -s <tamanho-do-volume>
   ```
   - Parâmetros:
     - `-n` ou `--volume_name`: Nome do volume
     - `-s` ou `--volume_size`: Tamanho do volume em GB (padrão: 10)

### Aplicação

1. **Listar Aplicações**
   ```bash
   python main.py application list
   ```
2. **Criar uma Nova Aplicação**
   ```bash
   python main.py application create -n <nome> -u <usuario> -p <senha> -c <codigo>
   ```
   - Parâmetros:
     - `-n` ou `--name`: Nome da aplicação
     - `-u` ou `--user`: Nome de usuário para a aplicação
     - `-p` ou `--password`: Senha da aplicação
     - `-c` ou `--code`: Código da aplicação
     - `-k` ou `--ssh_key_name`: Nome da chave ssh configurada no MGC
     - `-s` ou `--storage_key_id`: ID do key par do storage key
     - `-ss` ou `--storage_key_secret`: Secret do key par do storage key
     - `-sp` ou `--ssh_private_key_path`: Path para chave privada utilizada para acessar a VM via SSH

## Exemplos

1. **Criar um Banco de Dados**
   ```bash
   python main.py db create -f db-micro -n exemploDB -u admin -P senha123
   ```

2. **Criar uma Máquina Virtual com Chave SSH**
   ```bash
   python main.py machine create -n VMExemplo -k MinhaChaveSSH
   ```

3. **Criar um Volume com Nome e Tamanho Específicos**
   ```bash
   python main.py volume create -n VolumeExemplo -s 50
   ```

4. **Criar uma Aplicação**
   ```bash
   python main.py application create -n my_app -c PIOT12 -k my_key_name -s my_key_id -ss my_key_secret -u username -p password -sp ~/.ssh/my_private_key
   ```

## Ajuda

Para ajuda geral:
```bash
python main.py --help
```

Para ajuda específica em cada comando e subcomando:
```bash
python main.py <comando> --help
```

## Observações

Este projeto assume que você tenha uma configuração de ambiente pronta para o uso do Terraform, incluindo as credenciais necessárias. Ajuste os parâmetros no arquivo `constants.py` para refletir as configurações e IDs de flavor, engine, máquinas e imagens disponíveis.

Para que o projeto funcione corretamente e necessario que o login utilizando o mgc cli tenha sido realizado, além disto apenas o comando application gera o arquivo terraform e executa o mesmo, os outros param logo após a geração.