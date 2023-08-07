from typing import List

from flask import jsonify
from flask_jwt_extended import create_access_token, jwt_required
from flask_openapi3 import APIBlueprint, Tag

from controller import EmpresaController
from serializer import (EmpresaGetSerializer, EmpresaInputSerializer,
                        EmpresaParamSerializer, EmpresaPatchSerializer,
                        EmpresaSerializer, LoginSerializer, TokenSerializer,
                        Unauthorized)

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
