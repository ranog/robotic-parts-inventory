# Inventory control
CRUD básico para cadastro de peças.

## Instalar as dependências do projeto

### instalar o pyenv
https://github.com/pyenv/pyenv#installation

### dependências para compilar e instalar o python
`sudo apt-get update; sudo apt-get install make gcc build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev`

### instalar a versão 3.11.3 do python
`pyenv install 3.11.3`

### configurar versão 3.11.3 na sessão do terminal aberto
`pyenv local 3.11.3`

### instalar depêdencias do projeto
`pip install --upgrade pip setuptools wheel poetry`

### criar o ambiente virtual através poetry
`poetry env use 3.11.3`

### ativar o ambiente virtual através poetry
`source $(poetry env info --path)/bin/activate`

### rodar o comando pra instalar as depedencias da aplicação
`make install-deps`

## Arquivo .env

Faça um cópia do arquivo .env.local removendo o sufixo .local

## Criar peça:
```
curl --request POST \
  --url http://127.0.0.1:8080/v1/parts/ \
  --header 'Content-Type: application/json' \
  --data '{
  "name": "Stepper motor",
  "quantity": 100,
	"description": "NEMA 17 stepper motor"
}'
```

## Ler uma peça por vez:
```
curl --request GET \
  --url http://127.0.0.1:8080/v1/parts/1
```

## Ler todas as peças:
```
curl --request GET \
  --url http://127.0.0.1:8080/v1/parts/
```

## Atualizar peça:
```
curl --request PUT \
  --url http://127.0.0.1:8080/v1/parts/1 \
  --header 'Content-Type: application/json' \
  --data '{
	"name": 'DC motor'
}'
```

## Deletar peça:
```
curl --request DELETE \
  --url http://127.0.0.1:8080/v1/parts/1
```
