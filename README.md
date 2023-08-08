# EmpresaAPIRestFull-flask

Apresentação de uma APIRestFull feito em flask com documentaçao em Swagger
Projeto feito em Python versão 3.7
Api contém 9 endpoints sendo
1. GET /api/empresa
    - params: 
        - start
        - defult = 1
        - description = Para paginação
    - limit
      - defult = 10 
      - description = Limit de dados no retorno
    - sort
      - defult = id
      - description = Para ordenaçãp
    - dir
      - defult = asc
      - description = Tipo de ordenação
2. GET /api/empresa/pages
    - sem parametros, retorna a quantidade de paginas sem filtro
3. GET /api/empresa/<int:id>
    - parametro do tipo path repassando o id da empresa
4. GET /api/empresa_mock
    - endpoint para geração de 100 empresas aleatorias
5. POST /api/empresa
    - endpoint para criação de empresa, contém validação de cnpj
    - body {
        "cnae": "string",
        "cnpj": "string",
        "nome_fantasia": "string",
        "nome_razao": "string"
    }
6. POST /api/lookup/filter
    - endpoint para filtro de dados, 
    - versao reduzida somente para busca dados da empresa
    - params:
        - limit
            - default=10
            - description = limite de dados de retorno
    - body
        - exemplo {'nome_razao': 'Ltda'}
        - nesse caso ira busca na coluna nome_razao os dados
        - que tenha Ltda utilizando ilike na requisição SQL
7. POST /api/token
    - endpoint para geração do access token, 
    - versao reduzida com usuario fixo em codigo
    - body {
            "password": "homolog",
            "username": "Cz[b77SUU"
        }
8. PUT /api/empresa/<int:id>
    - endpoint para atualizar a empresa
    - parametro do tipo path repassando o id da empresa
    - esse endpoint so permite atualizar cnae e nome_fantasia
    - como esse endpoint nao recebe todo o objeto da empresa 
    - poderia ser o metodo PATH 
    - body {
            "cnae": "string",
            "nome_fantasia": "string"
        }
9. DELETE /api/empresa/<int:id>
    - endpoint para deletar a empresa
    - parametro do tipo path repassando o id da empresa


Na raiz do projeto contém a coleção do postman para a API
APIRestfull.postman_collection.json

## Instalaçao

Criar ambiente virtual
Windows

```bash
python -m venv env
```

```bash
python3 -m venv env
```

linux

Ativar ambiente virtual

Windows

```bash
env\Scripts\Activate.ps1
```

linux

```bash
source env/bin/activate
```

Instalar dependecias

```bash
pip install -r requirements.txt
```

## Execução do projeto

```bash
flask run
```

ou

```bash
flask --degub run
```
