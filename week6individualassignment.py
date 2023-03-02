Sales_quantity_list =  []
stock_level = int(input("Please enter an initial stock level: "))
month_number = int(input("Please enter the number of months to plan: "))
current_month = 1
Sales_quantity_list.append(stock_level)
while current_month <= month_number:
    planned_sale_quantity = int(input(f"Please enter the planned sales quantity  for month {current_month}: "))
    Sales_quantity_list.append(planned_sale_quantity)
    current_month += 1

# index = 0
print(Sales_quantity_list)
q = 0
for m in range(len(Sales_quantity_list)-1):
    stock = (q+Sales_quantity_list[m+1]) - Sales_quantity_list[m]
    print(stock)
    if stock < 0:
        production = 0
        # stock = stock + Sales_quantity_list[m]
        print(f"Production quantity month {m+1} is {production}")
        q = Sales_quantity_list[m+1]
    elif stock > 0:
      production = stock
      print(f"Production quantity month {m+1} is {production}")
      q = Sales_quantity_list[m+1]
    else:
      production = Sales_quantity_list[m]
      print(f"Production quantity month {m+1} is {production}")
      q = Sales_quantity_list[m+1]

       
