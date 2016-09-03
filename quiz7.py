from vector import Vector
from line import Line

def test(l1, l2):
    if l1.is_parallel_to(l2):
        if l1 == l2:
            print 'equal'
        else:
            print 'parallel but not equal'
    else:
        print 'intersects at:', l1.intersection_point(l2)

# Example 1
l1 = Line([4.046, 2.836], 1.21)
l2 = Line([10.115, 7.09], 3.025)

print '1:'
test(l1, l2)

# Example 2
l1 = Line([7.204, 3.182], 8.68)
l2 = Line([8.172, 4.114], 9.883)

print '2:'
test(l1, l2)

# Example 3
l1 = Line([1.182, 5.562], 6.744)
l2 = Line([1.182, 5.562], 9.525)

print '3:'
test(l1, l2)


# x = (d * k1 - b * k2) / (a * d - b * c)
# y = (-c * k1 + a * k2) / (a * d - b * c)
