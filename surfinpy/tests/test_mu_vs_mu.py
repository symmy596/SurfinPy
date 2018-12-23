import numpy as np
import numpy.testing as npt
import sys 
from surfinpy import mu_vs_mu
import unittest
from numpy.testing import assert_almost_equal, assert_equal

class Testmu_vs_mu(unittest.TestCase):
    def test_pressure(self):
        a = mu_vs_mu.pressure(1, 1)
        expected = 5267.59
        assert_almost_equal(a, expected, decimal=2)


    def test_calculate_excess(self):
        bulk = {'M' : 1, 'O' : 2, 'Energy' : -100.00, 'F-Units' : 1}
        x1 = mu_vs_mu.calculate_excess(1, 2, 3, bulk)
        x2 = mu_vs_mu.calculate_excess(2, 2, 3, bulk, nspecies=1, check=True)
        expected1 = 0.16666666666
        expected2 = -0.3333333333
        assert_almost_equal(expected1, x1, decimal=4)
        assert_almost_equal(expected2, x2, decimal=4)


    def test_calculete_normalisation(self):
        bulk = {'M' : 1, 'O' : 2, 'Energy' : -100.00, 'F-Units' : 1}
        x = mu_vs_mu.calculate_normalisation(1, 2, bulk, 3)
        expected = 33.5
        assert_almost_equal(expected, x, decimal=4)


    def test_calculate_surface_energy(self):
        x = mu_vs_mu.calculate_surface_energy(1, 2, 3, 4, 5, 6, 7)
        expected = -49
        assert x == expected
