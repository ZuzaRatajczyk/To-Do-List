# To-Do-List

In this project I use basics of SQLAlchemy and SQLLite data management.

# Create database
To create database I've used `create_engine()` method where `todo.db` is file name:

```
from sqlalchemy import create_engine

engine = create_engine('sqlite:///todo.db?check_same_thread=False')
```

# Create table

```
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
```

The `declarative_base()` returns a new base class from which mapped class Table will inherit. This is the base class for the model

```
from sqlalchemy import Column, Integer, String, Date

class Table(Base):
    __tablename__ = 'task'
    id = Column('id', Integer, primary_key=True)
    task = Column('task', String)
    deadline = Column('deadline', Date, default=datetime.today())

    def __repr__(self):
        return self.task
 ```
 
Above table is described in its model class.

# Create table in database

`Base.metadata.create_all(engine)` creates a table in database by generating SQL queries according to the model.

# Access to database 

 To access the databes I've created an a session:
 
 ```
 from sqlalchemy.orm import sessionmaker
 
 Session = sessionmaker(bind=engine)
session = Session()
```

 
