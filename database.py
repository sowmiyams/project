from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:postgres@localhost/projectDatabase'
# postgresql://qrhjcjsb:9aGmHLmvivL9rNLfBSGwphXkWT3qrevp@rajje.db.elephantsql.com/qrhjcjsb

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
