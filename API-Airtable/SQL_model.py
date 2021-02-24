from sqlalchemy import Column, Integer, String, ARRAY, DateTime, JSON
from settings import DataBase, session, engine
from datetime import datetime

class Cleardata(DataBase):
     __tablename__ = "Airtable"
     id = Column('id', Integer, primary_key=True)
     recid = Column('recid', String)
     name = Column('name', String)
     photo = Column('photo', String)
     method = Column('method', ARRAY(String))
     upload = Column('upload', DateTime)

class Rawdata(DataBase):
     __tablename__ = "Airtable-rowdata"
     id = Column('id', Integer, primary_key=True)
     upload = Column('upload', DateTime)
     data = Column('data', JSON)

def updateclear(name, photo, method, recid, date):
     update = session.query(Cleardata).filter_by(recid=recid).first()
     update.name = name
     update.photo = photo
     update.method = method
     update.upload = date
     session.commit()
     session.close()

def addclear(name, photo, method, recid, date):
     cleardata = Cleardata()
     cleardata.name = name
     cleardata.photo = photo
     cleardata.method = method
     cleardata.recid = recid
     cleardata.upload = date
     session.add(cleardata)
     session.commit()
     session.close()

def addraw(json_response):
     rawdata = Rawdata()
     rawdata.upload = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
     rawdata.data = json_response
     session.add(rawdata)
     session.commit()
     session.close()

def searchclear(recid):
     answer = session.query(Cleardata).filter_by(recid=recid).first()
     return answer

def removeclear(date):
     ondelete = session.query(Cleardata).filter(Cleardata.upload < date)
     if ondelete is not None:
          for data in ondelete:
               print('delete '+data.recid)
               session.delete(data)
          session.commit()
          session.close()
     else:
          print('delete is none')