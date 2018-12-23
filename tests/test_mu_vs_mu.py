import numpy as np
import numpy.testing as npt
import sys 
from surfinpy import mu_vs_mu
from numpy.testing import assert_almost_equal, assert_equal


def test_pressure():
    a = sp.pressure(1, 1)
    expected = 5267.59
    assert_almost_equal(a, expected, decimal=2)


def test_calculate_excess():
    pass


def test_calculete_normalisation():
    pass


def test_calculate_surface_energy():
    X = sp.calculate_surface_energy(1, 2, 3, 4, 5, 6, 7)
    expected = -48
    assert expected == X
