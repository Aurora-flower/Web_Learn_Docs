# 成绩管理：
from sqlalchemy import Column, create_engine, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# 插入数据
# row, column 行，列；
# create_engine 创建-引擎；
# session-maker 会话，会议-制造者，制作者；
# ext 分机，declarative 声明性的；
# connector 连接器

# 构造基类
Base = declarative_base()

# __tableName__ = "math"  类和表建立联系
# 属性对应到字段（列）


class math(Base):
    __tablename__ = 'math'
    id = Column(String(20), primary_key=True)
    name = Column(String(50))
    ms = Column(Integer)


# 建立连接
# root 根,用户名
# @localhost:3306/[score]  本地主机（localhost）,固定连接方式
engine = create_engine('mysql+mysqlconnector://root:Liyanxia802.@localhost:3306/score')
DBSession = sessionmaker(bind=engine)   # bind 绑定(连接)
session = DBSession()

# 构造三个对象
white = math(id='001', name="XiaoBai", ms="89")
black = math(id='002', name="XiaoHei", ms="99")
red = math(id='003', name="XiaoHong", ms="69")

# 将数据，add加入数据库
session.add(white)
session.add(black)
session.add(red)

# 进行提交，并关闭
session.commit()
session.close()
# 1、列：行的组成单位，一个行可以包含一个或多个列，
# 每个列都有其类型、长度与所存储的值，该值为字段值。
# 2、行：行也就是记录，一行代表一条完整的信息。

