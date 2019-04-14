from sqlalchemy import Column,String,create_engine,Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'
    sid = Column(String(10),primary_key=True)
    sname = Column(String(20))
    sage = Column(String(3))
    ssex = Column(String(2))

engine = create_engine('mysql+mysqlconnector://root:root@127.0.0.1:3306/studentsys')
DBsession = sessionmaker(bind=engine)
sess = DBsession()
# stu = Student(sid=5,sname='lipeng',sage=30,ssex='男')
# sess.add(stu)
# sess.commit()
# sess.close()
stu = sess.query(Student)
for student in stu.all():
    print(student.sid,student.sname,student.sage,student.ssex)

# student = sess.query(Student)
# print(student)
