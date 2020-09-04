from sqlalchemy import create_engine
from sqlalchemy import desc

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta

##
from sqlalchemy.orm import sessionmaker


def main():

    engine = create_engine('sqlite:///todo.db?check_same_thread=False')
    Base = declarative_base()

    class Table(Base):
        __tablename__ = 'task'
        id = Column(Integer, primary_key=True)
        task = Column(String, default='default_value')
        deadline = Column(Date, default=datetime.today())

        def __repr__(self):
            return self.string_field

    Base.metadata.create_all(engine)

    ###
    class Todo:
        def __init__(self):
            self.today = datetime.today()
            self.daydict = {
                0:'Monday',
                1:'Tuesday',
                2:'Wednesday',
                3:'Thursday',
                4:'Friday',
                5:'Saturday',
                6:'Sunday'
            }
            self.current_state()


        def current_state(self):
            print("1) Today\'s tasks")
            print("2) Week\'s tasks")
            print("3) All tasks")
            print("4) Missed tasks")
            print("5) Add task")
            print("6) Delete task")
            print("0) Exit")

            temp = input()
            if temp == '1':
                self.today_tasks()
            elif temp == '2':
                self.week_tasks()
            elif temp == '3':
                self.all_tasks()
            elif temp == '4':
                self.missed_tasks()
            elif temp == '5':
                self.add_task()
            elif temp == '6':
                self.delete_task()
            elif temp == '0':
                self.exit()

        def today_tasks(self):
            Session = sessionmaker(bind=engine)
            session = Session()


            rows = session.query(Table).filter(Table.deadline == self.today.date()).all()

            print(f'Today',
                  f'{self.today.strftime("%#d %b")}')

            if len(rows) == 0:
                print('Nothing to do')
            else:
                for num, row in enumerate(rows):
                    print(str(num+1) + '.', row.task)

            self.current_state()

        def add_task(self):
            Session = sessionmaker(bind=engine)
            session = Session()

            task_text = input('Enter task\n')
            task_deadline = datetime.strptime(input('Enter deadline\n'), '%Y-%m-%d')
            new_row = Table(task=task_text,
                            deadline=task_deadline)

            session.add(new_row)
            session.commit()
            print('Task has been added!')

            self.current_state()

        def week_tasks(self):
            Session = sessionmaker(bind=engine)
            session = Session()

            for i in range(0, 7):
                query_day = self.today + timedelta(days=i)
                rows = session.query(Table).filter(Table.deadline == query_day.date()).all()

                print(f'{self.daydict[query_day.weekday()]} {query_day.strftime("%#d %b")}')

                if len(rows) == 0:
                    print('Nothing to do')
                else:

                    for num, row in enumerate(rows):
                        print(f'{str(num+1)}. {row.task}. {row.deadline.strftime("%#d %b")}')
                print()

            self.current_state()

        def all_tasks(self):
            Session = sessionmaker(bind=engine)
            session = Session()
            rows = session.query(Table).order_by(Table.deadline).all()

            # print(f'Today {self.today.day()} {self.today.strftime("%b")}')

            if len(rows) == 0:
                print('Nothing to do')
            else:
                print('Today:')
                for num, row in enumerate(rows):
                    print(f'{str(num+1)}. {row.task}. {str(row.deadline.day)} {row.deadline.strftime("%b")}')

            print()
            self.current_state()


        def missed_tasks(self):
            Session = sessionmaker(bind=engine)
            session = Session()
            rows = session.query(Table).filter(Table.deadline < self.today.date()).order_by(Table.deadline).all()

            if len(rows) == 0:
                print('Nothing is missed!')
            else:
                for num, row in enumerate(rows):
                    print(f'{str(num+1)}. {row.task}. {row.deadline.strftime("%#d %b")}')
            print()

            self.current_state()


        def delete_task(self):
            Session = sessionmaker(bind=engine)
            session = Session()
            rows = session.query(Table).all()

            if len(rows) == 0:
                print('Nothing to delete!')
            else:
                print("Choose the number of the task you want to delete:")
                for num, row in enumerate(rows):
                    print(f'{str(num + 1)}. {row.task}. {row.deadline.strftime("%#d %b")}')
            print()

            #temp = int(input())
            #try:
            #    spec_row = rows[temp - 1]
            #    session.delete(spec_row)
            #    session.commit()
            #    print('The task has been deleted!')
            #except:
            #    print('Incorrect row number!')
            t = int(input())
            spec_row = rows[t - 1]
            session.delete(spec_row)
            session.commit()
            print('The task has been deleted!')

            self.current_state()


        def exit(self):
            print('Bye!')

    a = Todo()


if __name__ == "__main__":
    main()
