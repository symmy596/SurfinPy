import numpy as np
import os
from surfinpy import utils as ut
import unittest
from numpy.testing import assert_almost_equal, assert_approx_equal


test_data = os.path.join(os.path.dirname(__file__), 'H2O.txt')


class TestUtils(unittest.TestCase):

    def setUp(self):
        self.testdata = open(test_data).read()

    def test_calculate_coverage(self):
        H2O = {'M': 24, 'X': 48, 'Y': 2, 'Area': 60.22,
               'Energy': -621.877140,  'Label': '1.66 - $Ce^{4+}$'}
        H2O_2 = {'M': 24, 'X': 48, 'Y': 4, 'Area': 60.22,
                 'Energy': -670.229520, 'Label': '3.32 - $Ce^{4+}$'}
        data = [H2O, H2O_2]
        x = ut.calculate_coverage(data)
        expected = np.array([1.66057788*10**18, 3.32115576*10**18])
        assert_approx_equal(expected[0], x[0], significant=8)
        assert_approx_equal(expected[1], x[1], significant=8)

    def test_get_labels(self):
        one = {'M': 1, 'X': 2, 'Y': 3, 'Area': 15.0,
               'Energy': -56.9, 'Label': "one"}
        two = {'M': 1, 'X': 2, 'Y': 3, 'Area': 15.0,
               'Energy': -56.9, 'Label': "two"}
        three = {'M': 1, 'X': 2, 'Y': 3, 'Area': 15.0,
                 'Energy': -56.9, 'Label':  "three"}
        data = [one, two, three]
        ticks = np.array([1, 2, 3])
        labels = ut.get_labels(ticks, data)
        expected = ['one', 'two', 'three']
        assert labels == expected

    def test_transform_numbers(self):
        Z = np.array([2, 2, 3, 3])
        ticks = np.array([2, 3])
        Z = ut.transform_numbers(Z, ticks)
        expected = np.array([0, 0, 1, 1])
        assert np.array_equal(Z, expected)

    def test_get_phase_data(self):
        X = np.arange(30)
        a = ut.get_phase_data(X, 3)
        expected = np.ones(10)
        assert np.array_equal(a, expected)

    def test_read_nist(self):
        x = ut.read_nist(test_data)
        assert x[1, 0] == 100
        assert x[10, 0] == 1000
        assert x[1, 1] == 1

    def test_fit(self):
        data = np.array([[0, 0, 0],
                         [1, 1, 1],
                         [2, 2, 2],
                         [3, 3, 3],
                         [4, 3, 5],
                         [5, 3, 8]])
        y = np.array([1, 2, 3, 4])
        x = ut.fit(data[:, 0], data[:, 2], y)
        expected = np.array([1.0142, 1.9424, 3.0844, 4.94])
        assert_almost_equal(x, expected, decimal=2)

    def test_calculate_gibbs(self):
        y = ut.calculate_gibbs(5, 5, 5)
        assert_almost_equal(y, 0.051541)

    def test_pressure(self):
        a = ut.pressure(1, 1)
        expected = 5267.59
        assert_almost_equal(a, expected, decimal=2)

    def test_get_levels(self):
        X = np.arange(5)
        levels = ut.get_levels(X)
        expected = np.array([-1, 0, 1, 2, 3, 4])
        assert np.array_equal(levels, expected)

    def test_get_ticks(self):
        X = np.arange(5)
        tick = ut.get_ticks(X)
        expected = [-0.5, 0.5, 1.5, 2.5, 3.5]
        assert tick == expected
