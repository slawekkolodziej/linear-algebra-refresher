from math import degrees
from vector import Vector

# Dot 1
VEC_1 = Vector([7.887, 4.138])
VEC_2 = Vector([-8.802, 6.776])
print VEC_1.dot(VEC_2)

# Dot 2
VEC_3 = Vector([-5.955, -4.904, -1.874])
VEC_4 = Vector([-4.496, -8.755, 7.103])
print VEC_3.dot(VEC_4)

# Angle 1
VEC_5 = Vector([3.183, -7.627])
VEC_6 = Vector([-2.668, 5.319])
print VEC_5.angle(VEC_6)

# Angle 2
VEC_7 = Vector([7.35, 0.221, 5.188])
VEC_8 = Vector([2.751, 8.259, 3.985])
print degrees(VEC_7.angle(VEC_8))