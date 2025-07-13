'''
# 导入MySQL驱动:
import mysql.connector

# 注意把password设为你的root口令:
password = input('Please input MySQL root password: ')
conn = mysql.connector.connect(user='root', password=password, database='test')
cursor = conn.cursor()

# 创建user表:
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')

# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])

print(cursor.rowcount)

# 提交事务:
conn.commit()
cursor.close()

# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print(values)

# 关闭Cursor和Connection:
cursor.close()

conn.close()
'''

# how to use ORM框架 SQLAlchemy
# 导入:
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# 初始化数据库连接:
password = input('Please input mysql root\'s password: ')
engine = create_engine(f'mysql+mysqlconnector://root:{password}@localhost:3306/test') # 初始化数据库连接
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建session对象:
session = DBSession()
# 创建新User对象:
new_user = User(id='5', name='Bob')
# 添加到session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()

# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id=='5').one()
# 打印类型和对象的name属性:
print('type:', type(user))
print('name:', user.name)
# 关闭Session:
session.close()
