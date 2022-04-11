"""
@Author: Jayesh Dahiwale
@Date: 2022-04-09 15:10:00
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-09 19:11:00
@Title : EmployeeWage Assignment
"""

import random


class Employee:

    def __init__(self):
        self.attendance = random.randint(0, 1)
    """
    Below functions checks whether the employee is present or absent. And print the status
    """
    def check_attendance(self):
        if self.attendance == 0:
            print("Employee is absent")
        else:
            print("Employee is present")

print("Welcome to EmployeeWage computation program")
employee = Employee()
employee.check_attendance()
