"""http://stackoverflow.com/questions/36000400/calculate-difference-between-two-angles

Answer for a stack overflow question on calculating 
the difference between two angles"""

import math

# calculate and return the distance unit2 
# needs to move to reach unit1
def get_distance(unit1, unit2):
    phi = (unit2-unit1) % 360
    sign = -1
    # used to calculate sign
    if not ((phi >= 0 and phi <= 180) or (
            phi <= -180 and phi >= -360)):
        sign = 1
    if phi > 180:
        result = 360-phi
    else:
        result = phi
    return (result*sign), sign

def get_sign(unit1, unit2):
    return not (unit1-unit2 >= 0 and unit1-unit2 <= 180) or (
            unit1-unit2 <= -180 and unit1-unit2 >= -360)

def new_position(unit1, unit2, variance = 20):
    distance_to_move, sign = get_distance(unit1, unit2)
    variance*=sign
    # %360 to keep it whithin the circle
    return (unit2+distance_to_move-variance)%360

# distance unit2 needs to move to reach unit1
assert (get_distance(90,45) == (45, 1))
assert (get_distance(270, 350) == (-80, -1))
assert (get_distance(350, 30) == (-40, -1))   
assert (get_distance(30, 350) == (40, 1))
assert (get_distance(50, 360*4) == (50, 1))
assert (get_distance(360*4, 50) == (-50, -1))
print "----------"
assert (new_position(90,45) == 70)
assert (new_position(270, 350) == 290) 
assert (new_position(350, 30) == 10)
assert (new_position(30, 350) == 10)
assert (new_position(50, 360*4) == 30)
assert (new_position(360*4, 50) == 20)

print (get_distance(1, 360*4))
print (get_distance(360*4, 1))
