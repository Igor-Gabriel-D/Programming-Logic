# Write a program that receives three grades and their respective weights, calculates and displays the weighted mean.

grade1 = float(input("First grade: "))
grade2 = float(input("Second grade: "))
grade3 = float(input("Third grade: "))

weight1 = float(input("First weight: "))
weight2 = float(input("Second weight: ")) 
weight3 = float(input("Third weight: "))

mean = (grade1*weight1 + grade2*weight2 + grade3*weight3) / (weight1 + weight2 + weight3)

print(f"Weighted mean: {mean}")
