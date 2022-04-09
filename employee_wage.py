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
        self.daily_wage = 0
        self.max_working_hours = 0;

    def check_attendance(self):
        if self.attendance == 0:
            print("The employee is absent")
        elif self.attendance == 1:
            print("The full time employee is present")
        else:
            print("The part time employee is present")

    def daily_hours(self):
        if self.attendance == 0:
            return 0
        elif self.attendance == 1:
            return self.full_day_hour
        else:
            return self.part_time_hour

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
        self.max_working_hours
        max_working_days = 0
        monthly_wage = 0
        while self.max_working_hours < 100 and max_working_days < 19:
            employee_temp = Employee()
            self.max_working_hours += employee_temp.daily_hours()
            if self.max_working_hours == 104:
                self.max_working_hours = 96
                continue
            max_working_days += 1
            if employee_temp.daily_hours() == 0:
                max_working_days -= 1
            monthly_wage += employee_temp.daily_emp_wage()
        print(f"The total monthly wage is Rs.{monthly_wage}.")
        print(f"The total work days is {max_working_days}.")
        print(f"The total working hours is Rs.{self.max_working_hours}.")
        return monthly_wage

    def get_total_hours(self):
        return self.max_working_hours


print("Welcome to EmployeeWage computation program")
employee = Employee()
employee.monthly_emp_wage()
print(employee.max_working_hours)
