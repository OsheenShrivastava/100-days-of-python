
print("Welcome to the tip calculator!")
Bill = float(input("What was the total bill? $"))
Tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
People = int(input("How many people to split the bill?"))

# TODO-1 - Calculate Tip Percentage
Tip_as_Percent = Tip/100

# TODO-2 - Calculate Total Tip Amount
Total_Tip_amount = Tip_as_Percent * Bill

# TODO-3 - Calculate Total Bill
Total_Bill = Total_Tip_amount + Bill

# TODO-4 - Calculate Bill Per Person
Bill_per_Person = Total_Bill/People

# TODO-5 - Round the Final Amount to be paid by each person by 2 decimal places
Final_Amount = round(Bill_per_Person, 2)
print(f"Each person should pay: ${Final_Amount}")