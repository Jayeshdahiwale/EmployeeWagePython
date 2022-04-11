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
        self.status = random.randint(0, 1)

    """
       Below functions checks whether the employee is present or absent. And print the status
    """

    def check_attendance(self):
        print(self.switcher_one(self.attendance))
        if self.attendance == 1:
            self.check_employee_status()
    """
    This is the switch case for checking employee present or not
    """
    def switcher_one(self, argument):
        switch = {
            0: "Employee is Absent",
            1: "Employee is Present",
        }
        return switch.get(argument, "nothing")


    """
    Below function check whether the full time or part time employee present
    """

    def check_employee_status(self):
        print(self.switcher_two(self.status))
        self.daily_emp_wage()

    """Below function is  switch case for checking part time or full time employee present"""
    def switcher_two(self, argument):
        switch = {
            0: "Part time employee is present",
            1: "Full time Employee is Present",
        }
        return switch.get(argument, "nothing")
    """
    Below function  calculates the daily employee wage according to his attendance
    """

    def daily_emp_wage(self):
        if self.status == 0:
            daily_wage = self.wage_per_hour * self.part_time_hour
        else:
            daily_wage = self.wage_per_hour * self.full_day_hour
        print(f"The daily employee wage is Rs.{daily_wage}")


print("Welcome to EmployeeWage computation program")
employee = Employee()
employee.check_attendance()
