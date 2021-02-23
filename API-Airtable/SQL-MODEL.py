from sqlalchemy import create_engine, Column, Integer, String, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

DataBase = declarative_base()

class Cleardata(DataBase):
     __tablename__ = "Airtable"
     id = Column('id', Integer, primary_key=True)
     name = Column('name', String)
     photo = Column('photo', String)
     method = Column('method', ARRAY(String))



engine = create_engine('postgres://ucsrjadngdcnco:fd0220f006745991272e2543f9512dd9016a581df2e6a85687fa82400c042c66@ec2-108-128-104-50.eu-west-1.compute.amazonaws.com:5432/d4ilqgrunfrtev', echo=True)
DataBase.metadata.create_all(bind=engine)
maker = sessionmaker(bind=engine)

session = maker()
# cleardata = Cleardata()
# cleardata.id = 0
# cleardata.name = 'Nick'
# cleardata.photo = 'url.ph'
# cleardata.method = ['method1', 'method2']

answers = session.query(Cleardata).all()
for answer in answers:
    print(answer.id)
    print(answer.name)
    print(answer.photo)
    print(answer.method)

# session.add(cleardata)
# session.commit()
session.close()