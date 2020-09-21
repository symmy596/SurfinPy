import numpy as np
import os
from surfinpy import vibrational_data as vd
from surfinpy import utils as ut
import unittest
from numpy.testing import assert_almost_equal, assert_approx_equal

test_data = os.path.join(os.path.dirname(__file__), 'test.yaml')


class TestVibrationalData(unittest.TestCase):

    def test_zpe_calc(self):    
        vib_prop = ut.read_vibdata(test_data)
        x = vd.zpe_calc(vib_prop)
        assert x == 0.0017049071357836591

    def test_entropy_calc(self):
        vib_prop = ut.read_vibdata(test_data)
        new_temp = ut.build_tempgrid(np.arange(10), vib_prop['Frequencies']) 
        freq = ut.build_freqgrid(vib_prop['Frequencies'], np.arange(10)) 
        svib = vd.entropy_calc(freq, new_temp, vib_prop)
        assert svib[1] == 5.77204564238144e-05

    def test_vib_calc(self):
        x = vd.vib_calc(test_data, np.arange(10))
        assert x[0] == 0.0017049071357836591