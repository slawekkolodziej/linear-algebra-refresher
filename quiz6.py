from vector import Vector

v = Vector([8.462, 7.893, -8.187])
w = Vector([6.984, -5.975, 4.778])
print "Cross product v x w:"
print v.cross_product(w)

v = Vector([-8.987, -9.838, 5.031])
w = Vector([-4.268, -1.861, -8.866])
print "Area of parallelogram spanned by v and w:"
print v.area_of_parallelogram(w)

v = Vector([1.5, 9.547, 3.691])
w = Vector([-6.007, 0.124, 5.772])
print "Area of triangle spanned by v and w:"
print v.area_of_triangle(w)