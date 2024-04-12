

class Employee():
    """Python class to implement a basic version of a hotel employee.

    This Python class implements the basic functionalities of a hotel employee in a 
    simple hotel management system.

    Syntax
    ------
    obj = Employee(emp_id, name, position, salary)

    Parameters
    ----------
    [in] emp_id : int
        Unique identifier for the employee.
    [in] name : str
        Name of the employee.
    [in] position : str
        The job position of the employee (e.g., 'Receptionist', 'Housekeeper', 'Manager').
    [in] salary : float
        The salary of the employee.

    Returns
    -------
    obj : Employee
        Python object output parameter that represents an instance of the class Employee.

    Attributes
    ----------
    """
    #Here you start your code.



class Employee:
    def __init__(self, emp_id, name, position, salary):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.salary = salary

    # Getter methods
    def get_emp_id(self):
        return self.emp_id

    def get_name(self):
        return self.name

    def get_position(self):
        return self.position

    def get_salary(self):
        return self.salary

    # Setter methods
    def set_emp_id(self, emp_id):
        self.emp_id = emp_id

    def set_name(self, name):
        self.name = name

    def set_position(self, position):
        self.position = position

    def set_salary(self, salary):
        self.salary = salary



def main():
    #TESTING
    print("=================================================================")
    print("Test Case 1: Create an Employee.")
    print("=================================================================")
    employee1 = Employee(1, "John Doe", "Receptionist", 30000)

    if employee1.get_emp_id() == 1:
        print("Test PASS. The parameter emp_id has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if employee1.get_name() == "John Doe":
        print("Test PASS. The parameter name has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if employee1.get_position() == "Receptionist":
        print("Test PASS. The parameter position has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if employee1.get_salary() == 30000:
        print("Test PASS. The parameter salary has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


    # Position and Salary Update Test
    print("=================================================================")
    print("Test Case 2: Update Employee's Position and Salary.")
    print("=================================================================")
    employee1.set_position("Manager")
    employee1.set_salary(50000)

    if employee1.get_position() == "Manager":
        print("Test PASS. The employee's position has been correctly updated.")
    else:
        print("Test FAIL. Check the method set_position().")

    if employee1.get_salary() == 50000:
        print("Test PASS. The employee's salary has been correctly updated.")
    else:
        print("Test FAIL. Check the method set_salary().")



if __name__ == "__main__":
    main()
