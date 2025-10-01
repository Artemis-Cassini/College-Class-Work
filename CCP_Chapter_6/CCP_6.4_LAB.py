import math                     # needed in Step #3

# --------------------------------------------------------------------------------- STEP 1

wall_height = float(input())
wall_width = float(input())
cost_of_one_paint_can = float(input())

wall_area = wall_height * wall_width
print(f"Wall area: {wall_area:.1f} sq ft")

# --------------------------------------------------------------------------------- STEP 2 

paint_needed = wall_area / 350
print(f"Paint needed: {paint_needed:.3f} gallons")

# --------------------------------------------------------------------------------- STEP 3 

cans_needed = math.ceil(paint_needed)
print(f"Cans needed: {cans_needed} can(s)")

# --------------------------------------------------------------------------------- STEP 4

paint_cost = cans_needed * cost_of_one_paint_can
sales_tax = paint_cost * 0.07
total_cost = paint_cost + sales_tax
print(f"Paint cost: ${paint_cost:.2f}")
print(f"Sales tax: ${sales_tax:.2f}")
print(f"Total cost: ${total_cost:.2f}")

# ---------------------------------------------------------------------------------
