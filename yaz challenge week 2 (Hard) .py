def profit(per_unit_price, per_unit_cost):
    total_cost = 0
    unit_sold = 0
    while(unit_sold * per_unit_price <= total_cost):
        unit_sold += 1
        total_cost = unit_sold * per_unit_cost
    return unit_sold
try:
    per_unit_cost = float(input("Please enter per unit cost: "))
    per_unit_price = float(input("Please enter per unit price: "))
    min_units_for_profit = profit(per_unit_cost, per_unit_price)
    print(f"Company makes profit at least sell {min_units_for_profit} ")
except ValueError:
    print("You should enter valied number!")
