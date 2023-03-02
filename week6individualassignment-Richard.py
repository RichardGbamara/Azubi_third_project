stock_level = int(input("Please enter an initial stock level: "))
month_number = int(input("Please enter the number of months to plan: "))
Sales_quantity_list =  []
current_month = 1
while current_month <= month_number:
    planned_sale_quantity = int(input(f"Please enter the planned sales quantity  for month {current_month}: "))
    Sales_quantity_list.append(planned_sale_quantity)
    current_month += 1
