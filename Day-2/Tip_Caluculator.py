print("Welcome to the tip caluculator.")
total = float(input("What was the total bill? $ "))
percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
total += total*percent/100
people = int(input("How many people to split the bill? "))
value = round(total/7,2)
print(f"Each person should pay: ${value}")