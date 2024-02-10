# Desafio de Código - Pipeline

Este projeto consiste em uma solução para um desafio de criar uma pipeline eficiente para extração, transformação e carregamento (ETL) de dados de um banco de dados inicial para um banco de dados final.

## Como Usar

### Configuração Inicial

1. Certifique-se de ter o Docker instalado em sua máquina.
2. Abra o terminal e navegue até a pasta do projeto.
3. Execute `docker-compose build` para construir as imagens necessárias.
4. Em seguida, execute `docker-compose up` para iniciar os serviços conforme definido no `docker-compose.yml`.


## Funcionalidades

O script fornecido realiza as seguintes tarefas:

- **Importação de Dados**: Importa dados de arquivos CSV em um banco de dados PostgreSQL de origem.
- **Exportação de Dados**: Exporta dados de um banco de dados PostgreSQL de origem para arquivos CSV.

## Como Usar

1. Certifique-se de ter o Python e o psycopg2 instalados em seu ambiente.
2. Configure as informações de conexão para os bancos de dados de origem e destino no script `import_export.py`.
3. Execute o script `import_export.py`. Ele importará dados do banco de dados de origem para o banco de dados de destino e exportará dados do banco de dados de origem para arquivos CSV.

## Pré-requisitos

- Python 3.x
- psycopg2
- Bancos de dados PostgreSQL de origem e destino configurados corretamente.

## Resultado Final

Após a execução bem-sucedida dos scripts, um arquivo CSV final com todos os dados das tabelas estará disponível para análise. O projeto demonstra a habilidade de transferir dados entre bancos de dados, mantendo a organização e a integridade dos dados.
