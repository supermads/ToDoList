# Write your code here
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///todo.db?check_same_thread=False')

Base = declarative_base()

class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def menu():
    choice = int(input("1) Today's tasks\n2) Add task\n0) Exit"))
    if choice == 0:
        print("Bye!")
        return False
    if choice == 1:
        rows = session.query(Table).all()
        if len(rows) == 0:
            print("Nothing to do!")
        else:
            print(rows) # Will print value of the string_field
    else:
        new_row = Table(task=input("Enter task"))
        session.add(new_row)
        session.commit()
        print("The task has been added!")
    return True

while menu():
    pass

