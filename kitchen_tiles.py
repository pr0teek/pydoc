# Bathroom having 12 x 18 tiles (pink tile)
b1_wall = 22 * 7
b1_floor = 6 * 7
# Bathroom having 12 x 24 tiles (brown tile)
b2_wall = 21 * 7
b2_floor = 6 * 6
# Total tiles of bathroom 1st and 2nd
total_b1 = b1_wall + b1_floor
total_b2 = b2_wall + b2_floor
moulding = 2.5 + 2.5
# Grand total
total = total_b1 + total_b2
# cost of work
cost = total * 14
moulding_cost = moulding * 50
total_cost = cost + moulding_cost
# print of tiles
print(f"Total tiles of Bathroom 1st is {total_b1} sqft")
print(f"Total tiles of Bathroom 2nd is {total_b2} sqft")
print(f"Grand total of both Bathroom :- {total} sqft")
print(f" total moulding is {moulding} feet")
print(f"Cost of tiles is {cost} Rs")
print(f"Cost of Moulding is {moulding_cost} Rs")
print(f" Total cost is {total_cost} Rs")
