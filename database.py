import os
import sys

from sqlalchemy import Table, create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker
from sqlalchemy_utils import create_database, database_exists

from model import Empresa, meta

SQLALCHEMY_DATABASE_URL = 'sqlite:///database2.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

if not database_exists(engine.url):
    create_database(engine.url)
    meta.create_all(engine)

Base = declarative_base()

SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, class_=Session
)

db = SessionLocal()

def get_columns_base(session, table, filter: dict, limit: int = 0):
    table = Table(table, Base.metadata, autoload_with=engine)
    query = session.query(table)
    for attr, value in filter.items():
        column = table.c[attr]
        type_column = column.type.python_type
        if type_column == int:
            query = query.filter(column == value)
        elif type_column == str:
            query = query.filter(column.ilike("%%%s%%" % value))
    if limit:
        query = query.limit(limit)
    if limit == 1:
        return query.first()
    return query.all()
