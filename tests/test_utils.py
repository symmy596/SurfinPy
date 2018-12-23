import numpy as np
import numpy.testing as npt
import sys 
from surfinpy import utils as ut
from numpy.testing import assert_almost_equal, assert_equal


def test_calculate_coverage():
    pass


def test_get_phase_data():
    X = np.arange(30)
    a = sp.get_phase_data(X, 3)
    expected = np.ones(10)
    assert np.array_equal(a, expected)


def test_get_labels():
    one = {'M': 1, 'X': 2, 'Y':3, 'Area': 15.0, 'Energy': -56.9, 'Label': "one"}
    two = {'M': 1, 'X': 2, 'Y':3, 'Area': 15.0, 'Energy': -56.9, 'Label': "two"}
    three = {'M': 1, 'X': 2, 'Y':3, 'Area': 15.0, 'Energy': -56.9, 'Label':  "three"}
    data = [one, two, three]
    ticks = np.array([1, 2, 3])
    labels = sp.get_labels(ticks, data)
    expected = ['one', 'two', 'three']
    assert labels == expected


def test_transform_numbers():
    Z = np.array([2, 2, 3, 3])
    ticks = np.array([2, 3])
    Z = sp.transform_numbers(Z, ticks)
    expected = np.array([0, 0, 1, 1 ])
    assert np.array_equal(Z, expected)


def test_fit():
    pass


def test_get_phase_data():
    pass


def test_read_nist():
    pass


def test_calculate_gibbs():
    pass
