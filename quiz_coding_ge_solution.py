from decimal import Decimal, getcontext
from linsys import LinearSystem
from plane import Plane
from vector import Vector


s = LinearSystem([
    Plane(normal_vector=Vector(['5.862','1.178','-10.366']), constant_term='-8.15'),
    Plane(normal_vector=Vector(['-2.931', '-0.589', '5.183']), constant_term='-4.075')
])
r = s.compute_rref()

print "system 1: ", r


s = LinearSystem([
    Plane(normal_vector=Vector(['8.631','5.112','-1.816']), constant_term='-5.113'),
    Plane(normal_vector=Vector(['4.315', '11.132', '-5.27']), constant_term='-6.775'),
    Plane(normal_vector=Vector(['-2.158', '3.01', '-1.727']), constant_term='-0.831')
])
r = s.compute_rref()

print "system 2: ", r


s = LinearSystem([
    Plane(normal_vector=Vector(['5.262','2.739','-9.878']), constant_term='-3.441'),
    Plane(normal_vector=Vector(['5.111', '6.358', '7.638']), constant_term='-2.152'),
    Plane(normal_vector=Vector(['2.016', '-9.924', '-1.3672']), constant_term='-9.278'),
    Plane(normal_vector=Vector(['2.167', '-13.543', '-18.883']), constant_term='-10.567')
])
r = s.compute_rref()

print "system 3: ", r