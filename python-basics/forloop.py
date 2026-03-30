# Mwenje kiff
# 13/02/2026
# PROGRAM TO SHOW FOR LOOPS
# import math
# for x in range(0,360,30):
#     print(math.cos(x))
#     print(math.sin(x))
#     print(math.tan(x))

# for a in range (10,0,-1):
#     print(a)

#     import math

# # Header for the table
# print(f"{'Degree':>7} | {'Sin':>8} | {'Cos':>8} | {'Tan':>8}")
# print("-" * 40)

# # Loop from -180 to 180 with a step of 30
# for deg in range(-180, 181, 30):
#     # Convert degrees to radians
#     rad = math.radians(deg)
    
#     # Calculate values
#     s = math.sin(rad)
#     c = math.cos(rad)
    
#     # Tangent can be undefined (approaching infinity) at 90 and -90
#     # but since we are stepping by 30, we hit exactly 90 and -90.
#     # We'll use a conditional to handle the very large numbers returned.
#     t = math.tan(rad) if abs(math.cos(rad)) > 1e-10 else "inf"

#     # Formatting numbers to 4 decimal places
#     s_str = f"{s:.4f}"
#     c_str = f"{c:.4f}"
#     t_str = f"{t:.4f}" if isinstance(t, float) else t
    
#     print(f"{deg:>7} | {s_str:>8} | {c_str:>8} | {t_str:>8}")