# Write your code here
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta
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
    choice = int(input("1) Today's tasks\n2) Week's tasks\n3) All tasks\n4) Add task\n0) Exit\n"))
    print("")
    today = datetime.today()
    day = today.day
    month = today.strftime('%b')
    weekday = today.weekday()
    if choice == 0:
        print("Bye!")
        return False
    if choice == 1:
        rows = session.query(Table).filter(Table.deadline == today.date()).all()
        print("Today {} {}:".format(day,month))
        if len(rows) == 0:
            print("Nothing to do!")
        else:
            for i in range(len(rows)):
                print("{}. {}".format(i+1, rows[i]))
        print("")
    if choice == 2:
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        for x in range(0,7):
            rows = session.query(Table).filter((today + timedelta(days=x)).date() == Table.deadline).all()
            print("{} {} {}:".format(days_of_week[(weekday + x) % 7], day+x, month))
            if len(rows) == 0:
                print("Nothing to do!\n")
            else:
                for i in range(len(rows)):
                    print("{}. {}".format(i+1, rows[i]))
                print("")
    if choice == 3:
        rows = session.query(Table).order_by(Table.deadline).all()
        if len(rows) == 0:
            print("Nothing to do!")
        else:
            print("All tasks:")
            for i in range(len(rows)):
                print("{}. {}. {}".format(i+1, rows[i], rows[i].deadline.strftime('%-d %b')))
            print("")
    if choice == 4:
        new_row = Table(task=input("Enter task"), deadline = datetime.strptime(input("Enter deadline"), '%Y-%m-%d'))
        session.add(new_row)
        session.commit()
        print("The task has been added!")
    return True

while menu():
    pass

