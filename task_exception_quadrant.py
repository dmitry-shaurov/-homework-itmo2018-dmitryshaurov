def get_quadrant_number(x,y):
    if (x > 0) and (y > 0):
        return 1
    elif (x < 0) and (y > 0):
        return 2
    elif (x < 0) and (y < 0):
        return 3
    elif (x > 0 ) and (y < 0):
        return 4
    elif (x == 0) or (y == 0):
        raise ValueError

# a = 0
# b = 0
# print(get_quadrant_number(a,b))
