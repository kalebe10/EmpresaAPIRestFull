from sqlalchemy import Column, Integer, MetaData, String, Table

meta = MetaData()

Empresa = Table("empresa", meta,
                Column("id",Integer,primary_key=True),
                Column("cnpj",String(14), nullable=False),
                Column("nome_razao",String(120), nullable=False),
                Column("nome_fantasia",String(120), nullable=False),
                Column("cnae",String(10), nullable=False))
