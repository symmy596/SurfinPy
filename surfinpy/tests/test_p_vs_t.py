import numpy as np
import numpy.testing as npt
import sys 
from surfinpy import p_vs_t
from surfinpy import utils as ut
import unittest
from numpy.testing import assert_almost_equal, assert_equal

class Testp_vs_t(unittest.TestCase):
    def test_calculate_surface_energy(self):
        pass


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

    #def test_initialise(self):
        #thermochem = ut.read_nist("H2O.txt")
        #a, b, c, d = p_vs_t.initialise(thermochem, -10.0) 
        #assert_almost_equal(d[0],-10.00000010364310, decimals=10)
        #assert_almost_equal(d[1], -10.00000041457220, decimals=10)
        #assert_almost_equal(d[-1], -10.10364305332430, decimals=10)
        #assert_almost_equal(d[-2], -10.10343587086070, decimals=10)



