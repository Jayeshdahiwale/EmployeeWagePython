'''
@Author: Jayesh Dahiwale
@Date: 2022-04-09 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2021-02-11 18:00:30
@Title : EmployeeWage Assignment
'''

import random

class Employee:
    def __init__(self):
        pass
    def check_attendance(self):
        attendance = random.randint(0,1)
        if attendance == 0:
            print("Employee is present")
        else:
            print("Employee is absent")

print("Welcome to EmployeeWage computation program")
employee = Employee()
employee.check_attendance()