import random

from faker import Faker


def mock_empresa(qtd:int=100):
    fake = Faker('pt_BR')
    cnae_list = ['CNAE1', 'CNAE2', 'CNAE3', 'CNAE4', 'CNAE5']
    empresas = []
    for _ in range(qtd):
        cnpj = fake.cnpj()
        nome_razao = fake.company()
        nome_fantasia = fake.company_suffix()
        cnae = random.choice(cnae_list)
        empresas.append({
            "cnpj": cnpj,
            "nome_razao": nome_razao,
            "nome_fantasia": nome_fantasia,
            "cnae": cnae
        })
    return empresas
