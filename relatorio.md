# Relatório Final Grupo Forasteiros

## 1. Introdução
- Somos o grupo Forasteiros, formado por alunos do curso de Engenharia de Computação da Unicamp.

- Nosso projeto visa a integração facilitada de módulos pré-configurados de Terraform para perfis de usuários mais comuns em cloud (usando um CLI ou Interface gráfica), como Ciência de Dados de Alta Performance, Aplicativos Móveis, Aplicações Web Leves, dentre outros. Dessa maneira, o serviço se torna atrativo para novos usuários que não possuem familiaridade com essa linguagem, possibilitando que criem novos módulos mais escaláveis e personalizáveis a partir dos já existentes, uma vez que ela terá acesso os códigos de Terraform, o que se torna uma atrativo frente aos concorrentes.

## 2. Fase de Ideação
- **Definição do Problema**: Dificuldade de iniciar e configurar um projeto em Terraform, tanto na criação de um módulo quanto na integração deles. Além da dificuldade de definir quais recursos são realmente necessários para a aplicação.



- **Proposta de Solução**:
    - Interface amigável ao usuário final para configuração de um conjunto de serviços da Cloud automaticamente, tanto por CLI quanto pelo Console da Magalu Cloud.
    - Configuração de um conjunto de serviços da Cloud automaticamente.
    - União de módulos para criar configurações voltadas para cada perfil de uso.

## 3. Definição do MVP (Produto Mínimo Viável)

- **Características Principais**: Levantamento dos principais perfis de aplicação e de seus requisitos.

### Principais Serviços que Tentaremos Atender com Eficiência

#### Armazenamento de Dados
- **Banco de dados** - níveis de permissão
- **Redundância** - Object Storage

#### Hospedagem de Sites e Aplicativos
- **Banco de Dados**
- **Backup** (facultativo)
- **Balancear DNS** (release futura)

#### Computação de Alta Performance (HPC)
- **Banco de Dados** (pensando em IA)
- Máximo de hardware possível
- **Docker** para balancear carga em várias VMs (release futura)

#### Desenvolvimento e Testes
- **Docker** com Jenkins
- **CI** (Integração Contínua)

#### Análise de Dados e Big Data
- **Banco de Dados**
- **Banco de dados** - níveis de permissão
- **Redundância** - Object Storage
- **Docker** para paralelizar em várias VMs (release futura)

#### Inteligência Artificial e Machine Learning
- Semelhante a HPC

#### Backup e Recuperação de Desastres
- **Snapshot** - backup - frequência baixíssima (release futura)

#### Aplicações de IoT
- **Snapshot** - backup - frequência alta (release futura)
- **Banco de Dados**
- **Docker** com Jenkins, MQTT, Redis, Grafana, InfluxDB

### Principais Funcionalidades a Serem Abordadas neste MVP
- **Banco de dados**
- **Armazenamento**
- **VM**
- **Provisionamento rápido**
- **Docker**


## 4. Apresentação da Solução
- **Arquitetura do Sistema**: Diagrama ou descrição da arquitetura proposta.
- **Tecnologias Utilizadas na Solução**: Docker, Terraform, Python e mgc cli.
- [Apresentação](https://drive.google.com/file/d/1nWcbEnVSCK01eBLsrpjtPwlVc5-U-fjI/view?usp=drive_link)
- [Protótipo](https://www.figma.com/proto/gcAxuzDE8L7YRSC6nkszUd/Ex.-Magalu?node-id=14-1013&node-type=canvas&t=cL8TvUTnLBA5tn4g-1&scaling=min-zoom&content-scaling=fixed&page-id=0%3A1)
-  **Protótipo de extenção ao console magalu cloud:** [Figma](https://www.figma.com/design/gcAxuzDE8L7YRSC6nkszUd/Ex.-Magalu?node-id=0-1&t=a3R81wjfULayWrRP-1)
- **Repositório no** [GitHub](https://github.com/Henrique-hpds/hacka_forasteiros)

Nossa solução consiste em uma extensão a ser implementada nos serviços já existentes do Magalu Cloud, tanto na interface gráfica (Console Magalu) quanto na linha de comando (mgc cli). Essa ferramenta será projetada para ser familiar para os usuários atuais, utilizando a mesma interface com a qual já estão acostumados, ao mesmo tempo em que simplifica a construção e a utilização dos serviços existentes. Além de atrair novos usuários devido a sua personalização, escalabilidade e facilidade de utilização.

Isso tudo é possível graças à junção de módulos Terraform criada por nossa interface. A partir do perfil da aplicação, são selecionados módulos ideais para VM, armazenamento e banco de dados, considerando as necessidades específicas de cada aplicação. Tudo isso sem a menor necessidade de conhecimento dessa linguagem de descrição de infraestrutura.

Além disso, ao complementar os recursos já disponíveis, nossa solução visa proporcionar uma experiência mais fluida e eficiente, permitindo que os usuários explorem novas funcionalidades sem a necessidade de aprender um novo sistema.


## 5. Roadmap
- **Próximos Passos**: Após a entrega do MVP, o próximo passo é permitir que o script aceite uma pasta ou arquivo como parâmetro, carregando-o na VM. Isso possibilitará a execução de containers Docker pré-configurados diretamente na VM, facilitando a implantação de aplicações.
- **Planejamento de Releases Futuras**: Cronograma para futuras versões e mais perfis e maior personalização.

## 6. Issues Abertas para Correção de Bugs
- **Lista de Bugs Conhecidos**: Descrição dos problemas conhecidos e seu status.
    - Problemas com os exemplos disponibilizados de Terraform, pois alguns deles vinham com valores que não deveriam estar presentes. Por exemplo, no exemplo simples de VMs, havia uma key no meio do código que, ao executar `terraform apply`, resultava em erro 500 e não instanciava o módulo.
    - Dificuldade inicial para encontrar os valores utilizáveis para cada tipo de configuração do Terraform para o Magalu Cloud, pois esses valores não estavam listados na documentação e só eram encontrados em alguns exemplos.
    - A alternativa encontrada foi usar o `mgc cli` para listar esses valores e usar um `grep` para selecionar o que era necessário, como no exemplo:
        ```sh
        mgc vm machine-types list | grep "name"
        ```
    - Conceitos de `api_key`, `key_id` e `key_secret` não estavam claros, especialmente que `key_id` e `key_secret` eram apenas para serviços de object storage. Além disso, não era necessário definir o valor de `api_key` no manifesto do Terraform, pois já estava definido por padrão ao estar logado no `mgc`.
    - Após criar cerca de 15 VMs e receber o erro "create_error", foi percebido que não era possível criar nomes de chave SSH na cloud que continham o caractere ".", sem receber nenhum log de erro.
    - A versão v0.28.4 do mgc cli tenta explicar o erro ocorrido durante o processo, enquanto a v0.29.0 não fornece feedback algum, dificultando o entendimento do problema. Além disso, na v0.29.0, o comando `mgc vm machine-types list` não funciona.
    - No console Magalu Cloud, há um limite de listagem de 50 instâncias, não indicado em nenhum local, dando a entender que instâncias após a 50ª não existem ou não foram criadas.
    - É possível criar `api_key` com data de expiração anterior à data atual, resultando em uma key já expirada.
    - Bug na página de ID Magalu que impede a criação de uma `api_key` e também não permite fazer logout.


## 7. Conclusão
Nosso projeto visa simplificar a utilização de Terraform para usuários com pouca familiaridade, oferecendo uma interface amigável e módulos pré-configurados para diferentes perfis de uso na nuvem. Através da definição  do problema e da proposta de solução, foi possível atender diversas necessidades dos usuários, desde armazenamento de dados até computação de alta performance e IoT.

Devido à nauteza modularizada deste projeto, apresentam-se diversas oportunidades de criação de novos módulos que integrem outros serviços do Magalu Cloud não contemplados aqui. Além disso, há muito espaço para desenvolvimento de patchs de correção de bugs como os apresentados acima.

Por fim, reiteramos que nossa solução trará benefícios da infraestrutura como código de maneira eficiente e personalizada, pois permite uma grande escalabilidade e modularização, para além da facilidade, devido a integração dessa modularização tanto do ponto de vista de infraestrutura de cloud (Terraform) quanto de conteinerização de ferramentas (Docker).
