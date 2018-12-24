import numpy as np
import numpy.testing as npt
import sys
import os
from surfinpy import p_vs_t
from surfinpy import utils as ut
import unittest
from numpy.testing import assert_almost_equal, assert_equal

test_data = os.path.join(os.path.dirname(__file__), 'H2O.txt')


class Testp_vs_t(unittest.TestCase):
    
    
    def setUp(self):
        self.testdata = open(test_data).read()


    def test_calculate_surface_energy(self):
        AE = np.array([-1.0, -2.0])
        lnP = np.arange(1, 10)
        T = np.arange(1, 10)
        coverage = np.array([-10.0*10**18, -20.0*10**18])
        SE = 1.0
        nsurfaces = 2        
        x = p_vs_t.calculate_surface_energy(AE, lnP, T, coverage, SE, nsurfaces)
        assert_almost_equal(x[0], 1.)

    def test_convert_adsorption_energy(self):
        x = p_vs_t.convert_adsorption_energy_units(1)
        expected = 96485
        assert x == expected


    def test_calculate_adsorption_energy(self):
        x = p_vs_t.calculate_adsorption_energy(1, 2, 3, 4)
        expected = -4.3333333
        assert_almost_equal(expected, x, decimal=4)


    def test_adsorption_energy(self):
        stoich = {'M': 24, 'X': 48, 'Y': 0, 'Area': 60.22, 'Energy': -535.660075, 'Label': '0.00 - $Ce^{4+}$'}
        H2O = {'M': 24, 'X': 48, 'Y': 2, 'Area': 60.22, 'Energy': -621.877140,  'Label': '1.66 - $Ce^{4+}$'}
        H2O_2 = {'M': 24, 'X': 48, 'Y': 4, 'Area': 60.22, 'Energy': -670.229520, 'Label': '3.32 - $Ce^{4+}$'}
        data = [H2O, H2O_2]
        x = p_vs_t.adsorption_energy(data, stoich, -10.0)
        expected = [np.array([-3194476.7582625]), np.array([-2281133.22520625])]
        assert_almost_equal(expected, x, decimal=4)

    def test_initialise(self):
        x = ut.read_nist(test_data)
        a, b, c, d = p_vs_t.inititalise(x, -10.0) 
        assert_almost_equal(d[0],-10.000, decimal=3)
        assert_almost_equal(d[1], -10.000, decimal=3)
        assert_almost_equal(d[-1], -10.103, decimal=3)
        assert_almost_equal(d[-2], -10.103, decimal=3)

    def test_calculate(self):
        stoich = {'M': 24, 'X': 48, 'Y': 0, 'Area': 60.22, 'Energy': -530.0, 'Label': '0'}
        H2O = {'M': 24, 'X': 48, 'Y': 2, 'Area': 60.22, 'Energy': -620.0,  'Label': '1'}
        H2O_2 = {'M': 24, 'X': 48, 'Y': 4, 'Area': 60.22, 'Energy': -670.0, 'Label': '2'}
        data = [H2O, H2O_2]
        SE = 1.0
        nsurfaces = 2
        adsorbant = -10.0
        thermochem = ut.read_nist(test_data)
        x, y, z = p_vs_t.calculate(stoich, data, SE, adsorbant, thermochem)
        expectedx = np.arange(2, 1000)
        expectedy = np.arange(-13, 5.5, 0.1)
        expectedz = np.zeros(((expectedy.size), (expectedx.size)))
        assert_almost_equal(x, expectedx)
        assert_almost_equal(y, expectedy)
        assert_almost_equal(z, expectedz)

