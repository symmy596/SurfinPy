import numpy as np
import numpy.testing as npt
import sys 
from surfinpy import utils as ut
from numpy.testing import assert_almost_equal, assert_equal


def test_calculate_coverage():
    H2O = {'M': 24, 'X': 48, 'Y': 2, 'Area': 60.22, 'Energy': -621.877140,  'Label': '1.66 - $Ce^{4+}$'}
    H2O_2 = {'M': 24, 'X': 48, 'Y': 4, 'Area': 60.22, 'Energy': -670.229520, 'Label': '3.32 - $Ce^{4+}$'}
    data = [H2O, H2O_2]
    x = ut.calculate_coverage(data)
    expected = np.array([1.66057788*10**18, 3.32115576*10**18])
    assert_almost_equal(expected[0], x[0], decimal=0)
    assert_almost_equal(expected[1], x[1], decimal=0)

def test_get_phase_data():
    X = np.arange(30)
    a = ut.get_phase_data(X, 3)
    expected = np.ones(10)
    assert np.array_equal(a, expected)


def test_get_labels():
    one = {'M': 1, 'X': 2, 'Y':3, 'Area': 15.0, 'Energy': -56.9, 'Label': "one"}
    two = {'M': 1, 'X': 2, 'Y':3, 'Area': 15.0, 'Energy': -56.9, 'Label': "two"}
    three = {'M': 1, 'X': 2, 'Y':3, 'Area': 15.0, 'Energy': -56.9, 'Label':  "three"}
    data = [one, two, three]
    ticks = np.array([1, 2, 3])
    labels = ut.get_labels(ticks, data)
    expected = ['one', 'two', 'three']
    assert labels == expected


def test_transform_numbers():
    Z = np.array([2, 2, 3, 3])
    ticks = np.array([2, 3])
    Z = ut.transform_numbers(Z, ticks)
    expected = np.array([0, 0, 1, 1 ])
    assert np.array_equal(Z, expected)


def test_fit():
    pass


def test_read_nist():
    pass


def test_calculate_gibbs():
    pass
