import pickle
import os

FILE_NAME = 'Employee_DB.dat'

def read_employees():
    if not os.path.exists(FILE_NAME):
        return []
    
    if os.path.getsize(FILE_NAME) == 0:
        return []
    
    with open(FILE_NAME,'rb') as input_file:
        return pickle.load(input_file)
    
def write_employees(employees):
    with open(FILE_NAME,'wb') as out_file:
        pickle.dump(employees,out_file)