import numpy as np
import numpy.testing as npt
import os
from surfinpy import wulff
from surfinpy import utils as ut
from surfinpy import data
import unittest
from numpy.testing import assert_almost_equal, assert_equal

test_data = os.path.join(os.path.dirname(__file__), 'H2O.txt')


class TestWulff(unittest.TestCase):

    def test_temperature_correction(self):
        x = ut.read_nist(test_data)
        adsorbant = wulff.temperature_correction(100, x, -10.0)
        assert_almost_equal( adsorbant, -10.0010467948, decimal=3)


    def test_wulff_calculate(self):
        stoich = data.DataSet(cation = 20, x = 50, y = 0, area = 60.00, 
                                     energy = -500.00, label ="One")
        H2O = data.DataSet(cation = 20, x = 50, y = 2, area = 60.00, 
                                     energy = -600.00, label ="Two")
        dataset = [H2O]
        x = ut.read_nist(test_data)
        y = wulff.calculate_surface_energy(stoich, dataset, 1.0, -10.0, x, 100, 2)
        assert_almost_equal(y[0], 1.0)
        assert_almost_equal(y[1], -9.6914, decimal=4)


