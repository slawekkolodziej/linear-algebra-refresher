from decimal import Decimal, getcontext
from linsys import LinearSystem
from plane import Plane
from vector import Vector


try:
    s = LinearSystem([
        Plane(normal_vector=Vector(['0.786','0.786','0.588']), constant_term='-0.714'),
        Plane(normal_vector=Vector(['-0.138', '-0.138', '0.244']), constant_term='0.319')
    ])
    print s.compute_solution()
except Exception as e:
    print str(e)


try:
    s = LinearSystem([
        Plane(normal_vector=Vector(['8.631', '5.112', '-1.816']), constant_term='-5.113'),
        Plane(normal_vector=Vector(['4.315', '11.132', '-5.27']), constant_term='-6.775'),
        Plane(normal_vector=Vector(['-2.158', '3.01', '-1.727']), constant_term='-0.831')
    ])
    print s.compute_solution()
except Exception as e:
    print str(e)


try:
    s = LinearSystem([
        Plane(normal_vector=Vector(['0.935', '1.76', '-9.365']), constant_term='-9.955'),
        Plane(normal_vector=Vector(['0.187', '0.352', '-1.873']), constant_term='-1.991'),
        Plane(normal_vector=Vector(['0.374', '0.704', '-3.746']), constant_term='-3.982'),
        Plane(normal_vector=Vector(['-0.561', '-1.056', '5.619']), constant_term='5.973')
    ])
    print s.compute_solution()
except Exception as e:
    print str(e)
