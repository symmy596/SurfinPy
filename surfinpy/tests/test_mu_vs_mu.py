import numpy as np
from surfinpy import mu_vs_mu
from surfinpy import utils as ut
from surfinpy import data
import unittest
from numpy.testing import assert_almost_equal
import os

test_data = os.path.join(os.path.dirname(__file__), 'H2O.txt')


class Testmu_vs_mu(unittest.TestCase):

    def test_calculate_excess(self):
        bulk = data.ReferenceDataSet(cation = 1, anion = 2, energy = -100.00, funits = 1)
        x1 = mu_vs_mu.calculate_excess(1, 2, 3, bulk)
        x2 = mu_vs_mu.calculate_excess(2, 2, 3, bulk, nspecies=1, check=True)
        expected1 = 0.16666666666
        expected2 = -0.3333333333
        assert_almost_equal(expected1, x1, decimal=4)
        assert_almost_equal(expected2, x2, decimal=4)

    def test_calculete_normalisation(self):
        bulk = data.ReferenceDataSet(cation = 1, anion = 2, energy = -100.00, funits = 1)
        x = mu_vs_mu.calculate_normalisation(1, 2, bulk, 3)
        expected = 33.5
        assert_almost_equal(expected, x, decimal=4)

    def test_calculate_surface_energy(self):
        x = mu_vs_mu.calculate_surface_energy(1, 2, 3, 4, 5, 6, 7) / 16.021
        expected = -49
        assert x == expected

    def test_evaluate_phases(self):
        xshiftval = 0
        yshiftval = 0
        deltaX = {'Range': [0, 10], 'Label': 'O'}
        deltaY = {'Range': [0, 10], 'Label': 'H_2O'}
        bulk = data.ReferenceDataSet(cation = 1, anion = 2, energy = -100.00, funits = 1)
        pure = data.DataSet(cation = 24, x = 48, y = 0, area = 60.22, 
                                     energy = -575.00, label = "Stoich", nspecies = 1)
        H2O = data.DataSet(cation = 24, x = 48, y = 2, area = 60.22, 
                                     energy = -600.00, label = "One", nspecies = 1)
        dataset = [pure, H2O]
        nsurfaces = len(dataset)
        X = np.arange(deltaX['Range'][0], deltaX['Range'][1], 0.025,
                      dtype="float")
        Y = np.arange(deltaY['Range'][0], deltaY['Range'][1], 0.025,
                      dtype="float")
        X = X - xshiftval
        Y = Y - yshiftval
        phase, SE = mu_vs_mu.evaluate_phases(dataset, bulk, X, Y,
                                         nsurfaces, xshiftval, yshiftval)
        expected_phase = np.zeros(X.size * Y.size)
        expected_phase = expected_phase + 2
        assert_almost_equal(phase, expected_phase)
