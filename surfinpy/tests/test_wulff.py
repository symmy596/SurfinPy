import numpy as np
import numpy.testing as npt
import os
from surfinpy import wulff
from surfinpy import utils as ut
import unittest
from numpy.testing import assert_almost_equal, assert_equal

test_data = os.path.join(os.path.dirname(__file__), 'H2O.txt')


class TestWulff(unittest.TestCase):

    def test_temperature_correction(self):
        x = ut.read_nist(test_data)
        adsorbant = wulff.temperature_correction(100, x, -10.0)
        assert_almost_equal( adsorbant, -10.0010467948)


    def test_wulff_calculate(self):
        stoich = {'M': 20, 'X': 50, 'Y': 0, 'Area': 60.00, 'Energy': -500.0, 'Label': '0.00 - $Ce^{4+}$'}
        H2O = {'M': 20, 'X': 50, 'Y': 2, 'Area': 60.00, 'Energy': -600.0,  'Label': '1.66 - $Ce^{4+}$'}
        data = [H2O]
        x = ut.read_nist(test_data)
        y = wulff.calculate_surface_energy(stoich, data, 1.0, -10.0, x, 100, 2)
        assert_almost_equal(y[0], 1.0)
        assert_almost_equal(y[1], -9.6917, decimal=4)


