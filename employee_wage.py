'''
@Author: Jayesh Dahiwale
@Date: 2022-04-09 15:10:00
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2022-04-09 15:20:00
@Title : EmployeeWage Assignment
'''

import random


class Employee:
    def __init__(self):
        self.wage_per_hour = 20;
        self.full_day_hour = 8;

    def check_attendance(self):
        attendance = random.randint(0, 1)
        if attendance == 0:
            print("Employee is present")
        else:
            print("Employee is absent")

    def daily_emp_wage(self):
        daily_wage = self.wage_per_hour * self.full_day_hour
        print(f"The daily employee wage is Rs.{daily_wage}")


print("Welcome to EmployeeWage computation program")
employee = Employee()
employee.check_attendance()
employee.daily_emp_wage()