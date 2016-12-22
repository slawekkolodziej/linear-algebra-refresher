from decimal import Decimal, getcontext
from copy import deepcopy

from vector import Vector
from plane import Plane, MyDecimal

getcontext().prec = 30


class LinearSystem(object):

    ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG = 'All planes in the system should live in the same dimension'
    NO_SOLUTIONS_MSG = 'No solutions'
    INF_SOLUTIONS_MSG = 'Infinitely many solutions'

    def __init__(self, planes):
        try:
            d = planes[0].dimension
            for p in planes:
                assert p.dimension == d

            self.planes = planes
            self.dimension = d

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)


    def swap_rows(self, row1, row2):
        self[row1], self[row2] = self[row2], self[row1]


    def multiply_coefficient_and_row(self, coefficient, row):
        self[row] = self[row] * coefficient


    def add_multiple_times_row_to_row(self, coefficient, row_to_add, row_to_be_added_to):
        new_plane = self[row_to_add] * coefficient
        target_plane = self[row_to_be_added_to]

        self[row_to_be_added_to] = target_plane + new_plane


    # def indices_of_first_nonzero_terms_in_each_row(self):
    #     num_equations = len(self)
    #     num_variables = self.dimension

    #     indices = [-1] * num_equations

    #     for i, p in enumerate(self.planes):
    #         try:
    #             indices[i] = p.first_nonzero_index(p.normal_vector)
    #         except Exception as e:
    #             if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
    #                 continue
    #             else:
    #                 raise e

    #     return indices


    def compute_triangular_form(self):
        system = deepcopy(self)
        num_variables = system.dimension
        j = 0

        for i, plane in enumerate(system.planes):
            while j < num_variables:
                c = MyDecimal(plane.normal_vector[j])
                if c.is_near_zero() and system.swap_with_row_below_for_nonzero_coefficient(i, j) == False:
                    j += 1
                    continue

                system.clear_equaions_below(i, j)
                j += 1
                break

        return system


    def compute_rref(self):
        tf = self.compute_triangular_form()
        tf.planes.reverse()

        num_variables = tf.dimension

        for i, plane in enumerate(tf.planes):
            try:
                j = Plane.first_nonzero_index(plane.normal_vector)
            except Exception as e:
                if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
                    continue
                else:
                    raise e

            coefficient = Decimal(1.0) / plane.normal_vector[j]
            tf.multiply_coefficient_and_row(coefficient, i)
            tf.clear_equaions_below(i, j)

        tf.planes.reverse()

        return tf


    def swap_with_row_below_for_nonzero_coefficient(self, row_index, variable_index):
        k = row_index + 1

        while k < len(self.planes):
            if self.planes[k].normal_vector[variable_index] != 0:
                self.swap_rows(row_index, k)
                return True

        return False


    def clear_equaions_below(self, row_index, variable_index):
        number_of_equations = len(self.planes)
        coefficient = self.planes[row_index].normal_vector[variable_index]

        for n in range(row_index + 1, number_of_equations):
            plane = self.planes[n]
            if plane.normal_vector[variable_index] != 0:
                equation = plane.normal_vector[variable_index] / (coefficient * Decimal(-1.0))
                self.add_multiple_times_row_to_row(equation, row_index, n)


    def __len__(self):
        return len(self.planes)


    def __getitem__(self, i):
        return self.planes[i]


    def __setitem__(self, i, x):
        try:
            assert x.dimension == self.dimension
            self.planes[i] = x

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)


    def __str__(self):
        ret = 'Linear System:\n'
        temp = ['Equation {}: {}'.format(i+1,p) for i,p in enumerate(self.planes)]
        ret += '\n'.join(temp)
        return ret
