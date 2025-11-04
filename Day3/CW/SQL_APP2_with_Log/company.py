import logging
from employee import Employee
from db_config import session

class Company:

    def add_employee(self, employee):
        session.add(employee)
        session.commit()
        logging.info(f"Added employee: {employee}")
        print("Employee Added Successfully")

    def search_employee(self, emp_id):
        emp = session.query(Employee).filter_by(id=emp_id).first()
        if emp:
            logging.info(f"Found employee: {emp}")
        else:
            logging.warning(f"Employee not found for ID: {emp_id}")
        return emp

    def update_employee(self, emp_id, new_salary):
        emp = self.search_employee(emp_id)
        if emp:
            old_salary = emp.salary
            emp.salary = new_salary
            session.commit()
            logging.info(f"Updated employee ID {emp_id} salary from {old_salary} to {new_salary}")
            print("Employee Updated Successfully")
        else:
            logging.warning(f"Employee not found for update: ID {emp_id}")
            print("Employee not found")

    def delete_employee(self, emp_id):
        emp = self.search_employee(emp_id)
        if emp:
            session.delete(emp)
            session.commit()
            logging.info(f"Deleted employee: {emp}")
            print("Employee Deleted Successfully")
        else:
            logging.warning(f"Employee not found for deletion: ID {emp_id}")
            print("Employee not found")

    def display_all(self):
        employees = session.query(Employee).all()
        if not employees:
            print("Employee DB is Empty")
            logging.info("Displayed all employees: none found")
        else:
            print("Employee List\n")
            for emp in employees:
                print(emp)
            logging.info(f"Displayed all employees: total {len(employees)}")
