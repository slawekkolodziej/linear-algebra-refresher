from vector import Vector
from plane import Plane

def test(p1, p2):
    if p1.is_parallel_to(p2):
        if p1 == p2:
            print 'equal'
        else:
            print 'parallel but not equal'
    else:
        print 'not parallel'

# Example 1
p1 = Plane([-0.412, 3.806, 0.728], -3.46)
p2 = Plane([1.03, -9.515, -1.82], 8.65)

print '1:'
test(p1, p2)

# Example 2
p1 = Plane([2.611, 5.528, 0.283], 4.6)
p2 = Plane([7.715, 8.306, 5.342], 3.76)

print '2:'
test(p1, p2)

# Example 3
p1 = Plane([-7.926, 8.625, -7.212], -7.952)
p2 = Plane([-2.642, 2.875, -2.404], -2.443)

print '3:'
test(p1, p2)
