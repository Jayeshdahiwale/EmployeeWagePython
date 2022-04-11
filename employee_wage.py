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
        self.wage_per_hour = 20
        self.full_day_hour = 8
        self.part_time_hour = 4
        self.attendance = random.randint(0, 1)
        self.status = 0

    """
       Below functions checks whether the employee is present or absent. And print the status
    """

    def check_attendance(self):
        if self.attendance == 0:
            print("Employee is absent")
        else:
            self.check_employee_status()
    """
    Below function check whether the full time or part time employee present
    """
    def check_employee_status(self):
        self.status = random.randint(0, 1)
        if self.status == 0:
            print("Part time employee present")
        else:
            print("Full time employee present")


    """
    Below function  calculates the daily employee wage according to his attendance
    """

    def daily_emp_wage(self):
        if self.attendance == 0:
            daily_wage = 0
        else:
            if self.status == 0:
                daily_wage = self.wage_per_hour * self.part_time_hour
            else:
                daily_wage = self.wage_per_hour * self.full_day_hour
        print(f"The daily employee wage is Rs.{daily_wage}")


print("Welcome to EmployeeWage computation program")
employee = Employee()
employee.check_attendance()
employee.daily_emp_wage()
