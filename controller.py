from flask import jsonify
from sqlalchemy import asc, desc, insert

from base_model import query_delete_base, query_insert_base, query_update_base
from database import db
from mock_empresa import mock_empresa
from model import Empresa
from utils.converters import (is_cnpj_valido, query_to_dict,
                              query_to_list_of_dicts)


class EmpresaController:
    def __init__(self):
        self.model = Empresa

    def get_empresa_cnpj(self,cnpj):
        empresa = db.query(self.model).filter(self.model.c.cnpj==cnpj).first()
        if empresa:
            return query_to_dict(empresa)
        else:
            return None

    def create_empresa(self,data):
        if is_cnpj_valido(data['cnpj']):
            empresa = self.get_empresa_cnpj(data["cnpj"])
            if not empresa:
                res_insert = query_insert_base(db, Empresa, data)
                if res_insert:
                    empresa = self.get_empresa_cnpj(data["cnpj"])
                    return jsonify({'message': 'Empresa cadastrada com sucesso!',"empresa":empresa}), 201
                return jsonify({'message': 'Empresa não cadastrada!'}), 400
            else:
                return jsonify({'message': 'Empresa já cadastrada!',"empresa":empresa}), 400
        else:
            return jsonify({'message': 'CNPJ inválido!'}), 400

    def update_empresa(self,empresa_id, data):
        empresa = db.query(self.model).filter(self.model.c.id==empresa_id).first()
        if not empresa:
            return jsonify({'message': 'Empresa não encontrada'}), 404

        query_update_base(db, Empresa, [Empresa.c.id==empresa_id], data)
        empresa = db.query(self.model).filter(self.model.c.id==empresa_id).first()
        res = query_to_dict(empresa)
        return res

    def delete_empresa(self,empresa_id):
        empresa = db.query(self.model).filter(self.model.c.id==empresa_id).first()
        if not empresa:
            return jsonify({'message': 'Empresa não encontrada'}), 404
        query_delete_base(db, Empresa, [Empresa.c.id==empresa_id])
        return jsonify({'message': 'Empresa excluida com sucesso!'}), 200

    def get_items(self, start=1, limit=10, sort='id', dir='asc'):
        sort_column = getattr(self.model.c, sort)
        sort_direction = desc(sort_column) if dir == 'desc' else asc(sort_column)
        offset = (start - 1) * limit
        query = db.query(self.model).order_by(sort_direction).offset(offset).limit(limit).all()
        return query_to_list_of_dicts(query)
    
    def get_empresa_id(self, empresa_id):
        empresa = db.query(self.model).filter(self.model.c.id==empresa_id).first()
        if not empresa:
            return jsonify({'message': 'Empresa não encontrada'}), 404
        query = db.query(self.model).filter(self.model.c.id==empresa_id).first()
        return query_to_dict(query)

    def gera_empresas(self):
        empresas =  mock_empresa()
        sql = insert(self.model).values(empresas)
        res = db.execute(sql)
        db.commit()
        return empresas
