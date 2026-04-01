# Write a program that receives an employee's base salary, calculates and displays the final salary, knowing that the employee receives a 5% bonus on the base salary and pays 7% in taxes on the base salary.

base_sal = float(input("Base salary: "))
final_sal = (base_sal + (base_sal * 0.05) - (base_sal * 0.07))

print(f"Final salary: {final_sal}")
