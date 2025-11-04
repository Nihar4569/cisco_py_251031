from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, String, Integer, Float, create_engine

Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String(255),nullable=False)
    job_title = Column(String(255),nullable=False)
    salary = Column(Float,nullable=False)

def __repr__(self):
    return f"ID: {self.id}, Name: {self.name}, Title: {self.job_title}, Salary: {self.salary}"

# Database setup
engine = create_engine('sqlite:///employees.db.sqlite', echo=True) #create database if not exists
Base.metadata.create_all(engine) #create table for the first time if not exists

# Create a configured "Session" class fro crud operations
Session = sessionmaker(bind=engine)
session = Session()

dravid = Employee(name = 'Dravid', job_title = 'Batsman', salary = 1200)
session.add(dravid)
session.commit()

nihar = Employee(name = 'Nihar', job_title = 'SAE', salary = 38000)
session.add(nihar)
session.commit()

Employees = session.query(Employee).all()

emp_nihar = session.query(Employee).filter_by(name='Nihar').first()
print(emp_nihar)

emp_nihar.salary = 40000
session.commit()

set_emp = set()
for emp in Employees:
    if emp.name in set_emp:
        print(f"Duplicate Employee found: {emp}")
        session.delete(emp)
        session.commit()
    else:
        set_emp.add(emp.name)

employees = session.query(Employee).all()
for emp in employees:
    print(emp.name)