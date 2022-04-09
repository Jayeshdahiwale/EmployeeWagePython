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
        self.wage_per_hour = 20
        self.full_day_hour = 8
        self.part_time_hour = 4
        self.days_of_month = 20
        self.attendance = random.randint(0, 2)

    def check_attendance(self):
        if self.attendance == 0:
            print("Employee is absent")
        elif self.attendance == 1:
            print("Full time Employee is present")
        else:
            print("Part time employee is present")

    def daily_emp_wage(self):
        if self.attendance == 0:
            daily_wage = 0
        elif self.attendance == 1:
            daily_wage = self.wage_per_hour * self.full_day_hour
        else:
            daily_wage = self.wage_per_hour * self.part_time_hour

        print(f"The daily employee wage is Rs.{daily_wage}")
        return daily_wage

    def monthly_emp_wage(self):
        monthly_wage = 0
        for i in range(self.days_of_month):
            employee_temp = Employee()
            employee_temp.check_attendance()
            monthly_wage += employee_temp.daily_emp_wage()
        print(f"The total monthly wage is Rs.{monthly_wage}.")
        return monthly_wage


print("Welcome to EmployeeWage computation program")
employee = Employee()
employee.monthly_emp_wage()