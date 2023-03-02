# declaring and initializing variables
tax_rate = 7/100
tip_rate = 18/100

#asking for user input
userInput = float(input("Please can you enter the price of the food: "))
# computation of tip, sale tax and grand total
tip = userInput * tip_rate
sale_tax = userInput * tax_rate
grand_total = tip + sale_tax + userInput

# display results
print("The tip price is: $", tip)
print("The sale tax is: $", round(sale_tax,2))
print("The grand total is: $",grand_total)