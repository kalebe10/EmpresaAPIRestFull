from typing import List

from flask import jsonify, request
from flask_jwt_extended import create_access_token, jwt_required
from flask_openapi3 import APIBlueprint, Tag

from controller import EmpresaController, get_lookup
from serializer import (EmpresaGetPaginateSerializer, EmpresaGetSerializer,
                        EmpresaInputSerializer, EmpresaParamSerializer,
                        EmpresaPatchSerializer, EmpresaSerializer,
                        LimitSerializer, LoginSerializer, TokenSerializer,
                        Unauthorized)
from utils.query_filter import prepary_filter

jwt = {
    "type": "http",
    "scheme": "bearer",
    "bearerFormat": "JWT"
}
security_schemes = {"jwt": jwt}

empresa_tag = Tag(name="Empresa", description="")
security = [{"jwt": []}]
api = APIBlueprint(
    '/empresa',
    __name__,
    url_prefix='/api',
    abp_tags=[empresa_tag],
    abp_security=security,
    abp_responses={"401": Unauthorized},
    doc_ui=True
)


@api.post('/token', methods=['POST'], responses={200:TokenSerializer})
def login(body:LoginSerializer):
    payload = vars(body)
    username = payload['username']
    password = payload['password']
    
    if username == 'homolog' and password == 'Cz[b77SUUo':
        access_token = create_access_token(identity=username)
        return jsonify({'access_token': access_token}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401


@api.get("/empresa", tags=[empresa_tag], responses={200:EmpresaSerializer})
@jwt_required()
def get_list(query:EmpresaGetSerializer):
    res = EmpresaController().get_items(**vars(query))
    return res

@api.get("/empresa/pages", tags=[empresa_tag])
@jwt_required()
def get_list_paginate():
    res = EmpresaController().get_paginate()
    return res

@api.get("/empresa/<int:id>", tags=[empresa_tag], responses={200:EmpresaSerializer})
@jwt_required()
def get(path:EmpresaParamSerializer):
    id = path.id
    res = EmpresaController().get_empresa_id(id)
    return res

@api.get("/empresa_mock", tags=[empresa_tag], responses={200:EmpresaSerializer})
@jwt_required()
def get_mock_empresa():
    res = EmpresaController().gera_empresas()
    return res

@api.post("/empresa", tags=[empresa_tag])
@jwt_required()
def post(body:EmpresaInputSerializer):
    payload = vars(body)
    return EmpresaController().create_empresa(payload)

@api.put("/empresa/<int:id>", tags=[empresa_tag])
@jwt_required()
def put(path:EmpresaParamSerializer,body:EmpresaPatchSerializer):
    payload = vars(body)
    id = path.id
    return EmpresaController().update_empresa(id,payload)

@api.delete("/empresa/<int:id>", tags=[empresa_tag])
@jwt_required()
def delete(path:EmpresaParamSerializer):
    id = path.id
    return EmpresaController().delete_empresa(id)


@api.post("/lookup/filter", responses={201:EmpresaSerializer})
@jwt_required()
def get_lookup_filter(path:LimitSerializer):
    limit = path.limit
    data = request.get_json(force=True)
    params = prepary_filter(data.items())
    if len(params) and limit > 1:
        limit = 0
    res = get_lookup("empresa", params, limit)
    return res

@api.post("/requestReport", responses={201:EmpresaSerializer})
# @jwt_required()
def request_report():
    res = EmpresaController().get_items()
    return res
