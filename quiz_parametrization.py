from decimal import Decimal, getcontext
from linsys import LinearSystem
from plane import Plane
from vector import Vector


s = LinearSystem([
    Plane(normal_vector=Vector(['0.786','0.786','0.588']), constant_term='-0.714'),
    Plane(normal_vector=Vector(['-0.138', '-0.138', '0.244']), constant_term='0.319')
])

try:
    print s.compute_solution()
except Exception as e:
    print str(e)
