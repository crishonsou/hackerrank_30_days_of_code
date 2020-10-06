meal_cost = float(input())
tip_percent = int(input())
tax_percent = int(input())

def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost * (tip_percent / 100)
    tax = meal_cost * (tax_percent / 100)
    total_cost = meal_cost + tip + tax
    print(round(total_cost))

solve(12, 20, 8)
