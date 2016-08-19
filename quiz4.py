from math import degrees
from vector import Vector

pairs = [
    [
        Vector([-7.579, -7.88]),
        Vector([22.737, 23.64])
    ], [
        Vector([-2.029, 9.97, 4.172]),
        Vector([-9.231, -6.639, -7.245])
    ], [
        Vector([-2.328, -7.284, -1.214]),
        Vector([-1.821, 1.072, -2.94])
    ], [
        Vector([2.118, 4.827]),
        Vector([0, 0])
    ]
]

for vectors in pairs:
    print "parallel: "
    print vectors[0].is_parallel_to(vectors[1])
    print "orthogonal: "
    print vectors[0].is_orthogonal_to(vectors[1])
