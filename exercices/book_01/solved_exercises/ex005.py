# Write a program that receives an employee's salary and the percentage increase, calculates and displays the increase amount and the new salary.

sal = float(input("employee salary: "))
perc = float(input("percentage increase: "))

new_sal = sal + (sal * (perc/100))

print(f"Increase: {new_sal - sal}")
print(f"New salary: {new_sal}")
