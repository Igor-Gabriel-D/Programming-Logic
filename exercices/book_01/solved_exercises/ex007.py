# Write a program that receives an employee's base salary, calculates and displays their final salary, knowing that the employee receives a $50 bonus and pays 10% in taxes on their base salary.

base_sal = float(input("Base salary: "))
print(f"Final salary: {base_sal + 50 - (base_sal * 0.1)}")
