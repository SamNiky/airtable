from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


# PostgreSQL connection settings
USER = 'ucsrjadngdcnco'
PASSWORD = 'fd0220f006745991272e2543f9512dd9016a581df2e6a85687fa82400c042c66'
DB_NAME = 'd4ilqgrunfrtev'
HOST = 'ec2-108-128-104-50.eu-west-1.compute.amazonaws.com'
PORT = 5432


# Airtable API settings
AT = {
    'URL_REQ': 'api.airtable.com/v0/',
    'API_KEY': 'keyJnqTCPtMLLSWyV',
    'BASE_ID': 'appgru70CpzqkRsg1',
    'TABLE_NAME': 'Psychotherapists'
}
ATURL = f"https://{AT['URL_REQ']}{AT['BASE_ID']}/{AT['TABLE_NAME']}?api_key={AT['API_KEY']}"

# SQLAlchemy settings
DataBase = declarative_base()
engine = create_engine(f'postgres://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}', echo=True)
maker = sessionmaker(bind=engine)
session = maker()