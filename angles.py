"""http://stackoverflow.com/questions/36000400/calculate-difference-between-two-angles

Answer for a stack overflow question on calculating 
the difference between two angles"""

import math

# calculate and return the distance unit2 
# needs to move to reach unit1
def get_distance(unit1, unit2):
    phi = abs(unit2-unit1) % 360
    sign = 1
    # used to calculate sign
    if not ((unit1-unit2 >= 0 and unit1-unit2 <= 180) or (
            unit1-unit2 <= -180 and unit1-unit2 >= -360)):
        sign = -1
    if phi > 180:
        result = 360-phi
    else:
        result = phi

    return result*sign

# distance unit2 needs to move to reach unit1
print get_distance(90,45)  # output 45 
print get_distance(270, 350) # output -80 
print get_distance(350, 30) # output -40 (unit2 moves -40 degrees)   
print get_distance(30, 350) # output 40  

unit1 = 30
unit2 = 350
# then calculate distance to move by taking 20 from distance
distance_to_move = (get_distance(unit1, unit2) - 20)

print (unit2 + distance_to_move)%360 # new position 10
