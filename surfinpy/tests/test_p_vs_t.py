import numpy as np
import os
from surfinpy import p_vs_t
from surfinpy import utils as ut
from surfinpy.data import DataSet
import unittest
from numpy.testing import assert_almost_equal

test_data = os.path.join(os.path.dirname(__file__), 'H2O.txt')


class Testp_vs_t(unittest.TestCase):

#  Is this needed ?
#    def setUp(self):
#        self.testdata = open(test_data).read()

    def test_calculate_surface_energy(self):
        AE = np.array([-1.0, -2.0])
        lnP = np.arange(1, 10)
        T = np.arange(1, 10)
        coverage = np.array([-10.0*10**18, -20.0*10**18])
        SE = 1.0
        nsurfaces = 2
        x = p_vs_t.calculate_surface_energy(AE, lnP, T, coverage,
                                            SE, nsurfaces)
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
        stoich = DataSet(cation = 24, x = 48, y = 0, area = 60.22, 
                                     energy = -535.660075, label = "Stoich")
        H2O = DataSet(cation = 24, x = 48, y = 2, area = 60.22, 
                                     energy = -621.877140, label = "Stoich")
        H2O_2 = DataSet(cation = 24, x = 48, y = 4, area = 60.22, 
                                     energy = -670.229520, label = "Stoich")
        data = [H2O, H2O_2]
        x = p_vs_t.adsorption_energy(data, stoich, -10.0)
        expected = [np.array([-3194476.7582625]),
                    np.array([-2281133.22520625])]
        assert_almost_equal(expected, x, decimal=4)

    def test_initialise(self):
        x = ut.read_nist(test_data)
        a, b, c, d = p_vs_t.inititalise(x, -10.0, 1000, -13, 5.5)
        assert_almost_equal(d[0], -10.000, decimal=3)
        assert_almost_equal(d[1], -10.000, decimal=3)
        assert_almost_equal(d[-1], -10.103, decimal=3)
        assert_almost_equal(d[-2], -10.103, decimal=3)

    def test_calculate(self):
        stoich = DataSet(cation = 24, x = 48, y = 0, area = 60.22, 
                                     energy = -530.0, label = "Stoich")
        H2O = DataSet(cation = 24, x = 48, y = 2, area = 60.22, 
                                     energy = -620.0, label = "Stoich")
        H2O_2 = DataSet(cation = 24, x = 48, y = 4, area = 60.22, 
                                     energy = -677.0, label = "Stoich")

        data = [H2O, H2O_2]
        SE = 1.0
        adsorbant = -10.0
        thermochem = ut.read_nist(test_data)
        system = p_vs_t.calculate(stoich, data, SE, adsorbant, thermochem)
        expectedx = np.arange(2, 1000)
        expectedy = np.arange(-13, 5.5, 0.1)
        expectedz = np.zeros(((expectedy.size), (expectedx.size)))
        assert_almost_equal(system.x, expectedx)
        assert_almost_equal(system.y, expectedy)
        assert_almost_equal(system.z, expectedz)
