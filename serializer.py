from typing import Optional

from pydantic import BaseModel, Field

from utils.converters import FormatCpfCnpj


class EmpresaSerializer(BaseModel):
    id: Optional[int]
    cnpj: FormatCpfCnpj
    nome_razao: str
    nome_fantasia: str
    cnae: str

class EmpresaInputSerializer(BaseModel):
    cnpj: FormatCpfCnpj
    nome_razao: str
    nome_fantasia: str
    cnae: str
    
class EmpresaPatchSerializer(BaseModel):
    nome_fantasia: Optional[str]
    cnae: Optional[str]
    
class Unauthorized(BaseModel):
    code: int = Field(-1, description="Status Code")
    message: str = Field("Unauthorized!", description="Exception Information")


class EmpresaGetSerializer(BaseModel):
    start: int=1
    limit:int=10
    sort:str="id"
    dir:str="asc"


class EmpresaParamSerializer(BaseModel):
    id:int


class LoginSerializer(BaseModel):
    username:str
    password:str
    
class TokenSerializer(BaseModel):
    access_token:str
