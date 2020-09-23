import numpy as np
import os
from surfinpy import utils as ut
from surfinpy import data
import unittest
from numpy.testing import assert_almost_equal, assert_approx_equal


test_data = os.path.join(os.path.dirname(__file__), 'H2O.txt')


class TestUtils(unittest.TestCase):

    def setUp(self):
        self.testdata = open(test_data).read()

    def test_calculate_coverage(self):
        H20 = data.DataSet(cation = 24, x = 48, y = 2, area = 60.22, 
                                     energy = -570.00, label ="One", nspecies = 1)
        H2O_2 = data.DataSet(cation = 24, x = 48, y = 4, area = 60.22, 
                                     energy = -570.00, label ="Two", nspecies = 1)
        dataset = [H20, H2O_2]
        x = ut.calculate_coverage(dataset)
        expected = np.array([1.66057788*10**18, 3.32115576*10**18])
        assert_approx_equal(expected[0], x[0], significant=8)
        assert_approx_equal(expected[1], x[1], significant=8)

    def test_list_colors(self):
        H20 = data.DataSet(cation = 24, x = 48, y = 2, area = 60.22, color="red",
                                     energy = -570.00, label ="One", nspecies = 1)
        H2O_2 = data.DataSet(cation = 24, x = 48, y = 4, area = 60.22, color="blue",
                                     energy = -570.00, label ="Two", nspecies = 1)
        dataset = [H20, H2O_2]
        ticks = np.array([1, 2])
        labels = ut.list_colors(dataset, ticks)
        expected = ['red', 'blue']
        assert labels == expected

    def test_get_labels(self):
        H20 = data.DataSet(cation = 24, x = 48, y = 2, area = 60.22, 
                                     energy = -570.00, label ="One", nspecies = 1)
        H2O_2 = data.DataSet(cation = 24, x = 48, y = 4, area = 60.22, 
                                     energy = -570.00, label ="Two", nspecies = 1)
        dataset = [H20, H2O_2]
        ticks = np.array([1, 2])
        labels = ut.get_labels(ticks, dataset)
        expected = ['One', 'Two']
        assert labels == expected

    def test_transform_numbers(self):
        Z = np.array([2, 2, 3, 3])
        ticks = np.array([2, 3])
        Z = ut.transform_numbers(Z, ticks)
        expected = np.array([0, 0, 1, 1])
        assert np.array_equal(Z, expected)

    def test_get_phase_data(self):
        X = np.arange(30)
        a, b = ut.get_phase_data(X, 3)
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
        expected = np.array([1., 2., 3., 5.])
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

    def test_fit_nist(self):
        y = ut.fit_nist(test_data)[100]
        assert_almost_equal(y, 5.315630959761595e-06)

    def  test_build_xgrid(self):
        x = ut.build_xgrid(np.arange(10), np.arange(10))
        assert np.array_equal(x[0], np.arange(10))

    def  test_build_ygrid(self):
        x = ut.build_ygrid(np.arange(10), np.arange(10))
        assert np.array_equal(x[0], np.zeros(10))

    def test_build_zgrid(self):
        x = ut.build_ygrid(np.arange(10), np.arange(10))
        assert np.array_equal(x[0], np.zeros(10))

    def test_build_entgrid(self):
        x = ut.build_entgrid(np.arange(10), np.arange(10), np.arange(10))
        assert np.array_equal(x[0], np.zeros(10))
        assert np.array_equal(x[1], np.arange(10))

    def test_build_freqgrid(self):
        x = ut.build_freqgrid(np.arange(10), np.arange(10))
        assert np.array_equal(x[0], np.arange(10))

    def test_build_tempgrid(self):
        x = ut.build_tempgrid(np.arange(10), np.arange(10))
        assert np.array_equal(x[0], np.zeros(10))
