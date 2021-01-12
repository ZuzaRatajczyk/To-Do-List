from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta

engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base = declarative_base()


class Table(Base):
    __tablename__ = 'task'
    id = Column('id', Integer, primary_key=True)
    task = Column('task', String)
    deadline = Column('deadline', Date, default=datetime.today())

    def __repr__(self):
        return self.task


Base.metadata.create_all(engine)  # create table in db according to the model we described
Session = sessionmaker(bind=engine)
session = Session()


def main():
    exit_input = False
    while not exit_input:
        print("\n1) Today's tasks\n2) Week's tasks\n3) All tasks\n4) Missed tasks"
              "\n5) Add task\n6) Delete task\n0) Exit")
        user_input = input()
        if user_input == "1":
            tasks_for_today = session.query(Table).filter(Table.deadline == datetime.today().date()).all()
            print(f"\nToday {datetime.today().strftime('%d ' '%b')}")
            for i, task in enumerate(tasks_for_today):
                print(f"{i + 1}. {task}")
            if not tasks_for_today:
                print("Nothing to do!\n")
        elif user_input == "2":
            date = datetime.today().date()
            for i in range(7):
                print(date.strftime('\n%A ' '%d ' '%b:'))
                tasks_for_day = session.query(Table).filter(Table.deadline == date).all()
                if not tasks_for_day:
                    print("Nothing to do!")
                else:
                    for j, task in enumerate(tasks_for_day):
                        print(f"{j +1}. {task}")
                date += timedelta(days=1)
        elif user_input == "3":
            all_tasks = session.query(Table).order_by(Table.deadline).all()
            print("\nAll tasks:")
            for i, task in enumerate(all_tasks):
                print(f"{i + 1}. {task}. {task.deadline.strftime('%d ' '%b')}")
        elif user_input == "4":
            missed_tasks = session.query(Table).filter(Table.deadline < datetime.today().date())\
                .order_by(Table.deadline).all()
            print("Missed tasks:")
            if not missed_tasks:
                print("Nothing is missed!")
            else:
                for i, task in enumerate(missed_tasks):
                    print(f"{i + 1}. {task}. {task.deadline.strftime('%d ' '%b')}")
        elif user_input == "5":
            print("\nEnter task")
            user_task = input()
            print("Enter deadline YYYY-MM-DD")
            user_deadline = input().split('-')
            deadline_as_date = datetime(int(user_deadline[0]), int(user_deadline[1]), int(user_deadline[2]))
            new_row = Table(task=user_task, deadline=deadline_as_date)
            session.add(new_row)
            session.commit()
            print("The task has been added!\n")
        elif user_input == "6":
            all_tasks = session.query(Table).order_by(Table.deadline).all()
            print("\nChoose the number of the task you want to delete:")
            for i, task in enumerate(all_tasks):
                print(f"{i + 1}. {task}. {task.deadline.strftime('%d ' '%b')}")
            num_of_task = int(input())
            task_to_delete = all_tasks[num_of_task - 1]
            session.delete(task_to_delete)
            session.commit()
            print("The task has been deleted!")
        elif user_input == "0":
            exit_input = True
            print("\nBye!")



if __name__ == "__main__":
    main()
