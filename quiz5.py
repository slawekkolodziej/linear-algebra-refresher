from vector import Vector

v = Vector([3.039, 1.879])
b = Vector([0.825, 2.036])
print "Projection v on b:"
print v.projection_on(b)

v = Vector([-9.88, -3.264, -8.159])
b = Vector([-2.155, -9.353, -9.473])
print "Orthogonal to b:"
print v.orthogonal_to(b)

v = Vector([3.009, -6.172, 3.692, -2.51])
b = Vector([6.404, -9.144, 2.759, 8.718])
print "V as a sum of vectors:"
print v.projection_on(b)
print v.orthogonal_to(b)