import os
import sys

from sqlalchemy import create_engine
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
