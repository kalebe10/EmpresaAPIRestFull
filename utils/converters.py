from itertools import cycle

LENGTH_CNPJ = 14

def query_to_list_of_dicts(query_result):
    lista_de_dicts = [dict(zip(result._fields, result)) for result in query_result]
    return lista_de_dicts

def query_to_dict(query_result):
    lista_de_dicts = dict(zip(query_result._fields, query_result))
    return lista_de_dicts


def is_cnpj_valido(cnpj: str) -> bool:
    cnpj = cnpj.replace(".","").replace("-","").replace("/","")
    if len(cnpj) != LENGTH_CNPJ:
        return False

    if cnpj in (c * LENGTH_CNPJ for c in "1234567890"):
        return False

    cnpj_r = cnpj[::-1]
    for i in range(2, 0, -1):
        cnpj_enum = zip(cycle(range(2, 10)), cnpj_r[i:])
        dv = sum(map(lambda x: int(x[1]) * x[0], cnpj_enum)) * 10 % 11
        if cnpj_r[i - 1:i] != str(dv % 10):
            return False

    return True


class FormatCpfCnpj(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not v:
            return "NÃO INFORMADO/IDENTIFICADO"

        v = v.replace(".","").replace("-","").replace("/","")
        if len(v) == 14:
            v = v[:2] + "." + v[2:5] + "." + v[5:8] + "/" + v[8:12] + "-" + v[12:]

        elif len(v) == 11:
            v = v[:3] + "." + v[3:6] + "." + v[6:9] + "-" + v[9:]

        return v
