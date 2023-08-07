from sqlalchemy import delete, insert, update
from sqlalchemy.sql.selectable import Alias


def query_insert_base(session, table, insert_dict: dict = {}, autocommit=True):

    if isinstance(table, Alias):
        table = table.element

    sql = insert(table).values(insert_dict)
    res = session.execute(sql)
    if autocommit:
        session.commit()
    return res


def query_update_base(
    session, table, where_list, update_dict: dict = {}, autocommit=True
):

    if isinstance(table, Alias):
        table = table.element

    sql = update(table).where(*[where for where in where_list]).values(update_dict)

    session.execute(sql)

    if autocommit:
        session.commit()


def query_delete_base(session,table, where_list, autocommit=True):
    sql = delete(table).where(*[where for where in where_list])

    session.execute(sql)

    if autocommit:
        session.commit()
