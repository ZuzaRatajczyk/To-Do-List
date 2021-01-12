# To-Do-List

In this project I use basics of SQLAlchemy and SQLLite data management.

# Create database
To create database I've used `create_engine()` method where `todo.db` is file name:

`from sqlalchemy import create_engine`
`engine = create_engine('sqlite:///todo.db?check_same_thread=False')`

# Create table

`from sqlalchemy.ext.declarative import declarative_base`
`Base = declarative_base()`

The `declarative_base()` returns a new base class from which mapped class Table will inherit. This is the base class for the model

```
class Table(Base):
    __tablename__ = 'task'
    id = Column('id', Integer, primary_key=True)
    task = Column('task', String)
    deadline = Column('deadline', Date, default=datetime.today())

    def __repr__(self):
        return self.task
 ```
 
Above table is described in its model class.
