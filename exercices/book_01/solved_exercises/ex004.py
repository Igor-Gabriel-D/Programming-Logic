# Write a program that receives an employee's salary, calculates and displays the new salary, knowing that it has increased by 25%.

salary = float(input("employee salary :"))

print(f"New salary: {salary + (salary * 0.25)}")
