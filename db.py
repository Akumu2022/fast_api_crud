from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_URL = "mysql+pymysql://root:@localhost:3307/my_database"

engine= create_engine(DB_URL)

SessionLocal= sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base=declarative_base()

