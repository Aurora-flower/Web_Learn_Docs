# 查询数据

from sqlalchemy import Column, create_engine, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class math(Base):
    __tablename__ = "math"
    id = Column(String(20), primary_key=True)
    name = Column(String(50))
    ms = Column(Integer)


engine = create_engine('mysql+mysqlconnector://root:Liyanxia802.@localhost:3306/score')
DBSession = sessionmaker(bind=engine)   # bind 绑定(连接)
session = DBSession()

# query 查询
user = session.query(math.id, math.name, math.ms).all()

print('type:', type(user))

for i in user:
    print(i)
session.close()
