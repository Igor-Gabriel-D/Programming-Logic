# Write a program that receives a deposit amount and an interest rate, calculates and displays the interest earned and the total amount after the investment.

deposit = float(input("Deposit: "))
interest_rate = float(input("Interest rate: "))

print(f"Interest earned: {deposit * (interest_rate/100)}")
print(f"Total amount after the investment: {deposit + deposit * (interest_rate/100)}")
