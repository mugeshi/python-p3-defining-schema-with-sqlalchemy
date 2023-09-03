#!/usr/bin/env python3
#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


Base = declarative_base()

class Student(Base):
    __tablename__ = "students"  # Corrected typo: "__tablename__" instead of "__t5ablename__"

    id = Column(Integer, primary_key=True)  # Corrected "column" to "Column" and added "primary_key=True"
    name = Column(String)  # Corrected "column" to "Column" and removed unnecessary parentheses

if __name__ == '__main__':

 engine = create_engine('sqlite:///students.db')  # Replace with your desired database connection
 Base.metadata.create_all(engine)
