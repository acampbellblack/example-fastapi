from pkg_resources import declare_namespace
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
import time
from .config import settings

SQLALCHEMY_DATABASE_URL = 'postgresql://{usr}:{pwd}@{host}:{port}/{db}'.format(
    usr=settings.database_username, 
    pwd=settings.database_password,
    host=settings.database_hostname, 
    port=settings.database_port, 
    db=settings.database_name
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# while True:
#     try:
#         conn = psycopg2.connect(host='localhost', dbname='fastapi',
#                                 user='postgres', password='password')

#         cursor = conn.cursor()
#         print("database connection was successful")
#         break

#     except Exception as error:
#         print("connecting to database failed")
#         print("Error: ", error)
#         time.sleep(2)
