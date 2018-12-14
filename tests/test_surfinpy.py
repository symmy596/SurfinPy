import numpy as np
import numpy.testing as npt
import sys 

sys.path.append('/home/adam/data/adam/progs/Surfpy/')
import surfinpy as sp 
from numpy.testing import assert_almost_equal, assert_equal

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

def test_pressure():
    a = sp.pressure(1, 1)
    expected = 5267.59

    assert_almost_equal(a, expected, decimal=2)

def test_constants():
    data = {'M': 1, 'X': 2, 'Y':3, 'Area': 15.0, 'Energy': -50.0, 'Label': "one"}
    bulk = {'M': 1, 'O': 2, 'Energy' : -100.0, 'F-Units' : 5}
    H, O, B = sp.constants(data, bulk)
    expected_H = 0.1
    expected_O = 0
    expected_B = -1.0

    assert_almost_equal(H, expected_H)
    assert_almost_equal(O, expected_O)
    assert_almost_equal(B, expected_B)

def test_scale():
    X = sp.scale(5, 5)
    expected = 25
    assert X == expected

def test_calculate_surface_energy():
    X = sp.calculate_surface_energy(1, 2, 3, 4, 5, 6, 7)
    expected = -48
    assert expected == X