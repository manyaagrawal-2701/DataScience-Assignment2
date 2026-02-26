# List of coordinates
points = [(1, 2), (-3, 4), (-2, -5), (6, -7), (3, 4), (-1, -9)]

# Dictionary to count quadrants
quad_count = {"Q1": 0, "Q2": 0, "Q3": 0, "Q4": 0}

# Loop with tuple unpacking
for (x, y) in points:
    
    if x > 0 and y > 0:
        quad_count["Q1"] += 1
        
    elif x < 0 and y > 0:
        quad_count["Q2"] += 1
        
    elif x < 0 and y < 0:
        quad_count["Q3"] += 1
        
    elif x > 0 and y < 0:
        quad_count["Q4"] += 1

print(quad_count)