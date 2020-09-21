import numpy as np
from surfinpy import bulk_mu_vs_t
from surfinpy import utils as ut
from surfinpy import data
import unittest
from numpy.testing import assert_almost_equal
import os

test_data = os.path.join(os.path.dirname(__file__), 'H2O.txt')


class TestReferenceData(unittest.TestCase):

    def test_normalise_phase_energy_1(self):
        bulk = data.ReferenceDataSet(cation = 1, anion = 2, energy = -100.00, funits = 1)
        assert bulk.energy == -100.00
        assert bulk.cation == 1
        assert bulk.anion == 2

    def test_normalise_phase_energy(self):
        phase_1 = data.DataSet(cation = 10, x = 0, y = 0, energy = -90.0, label = "Periclase")
        assert phase_1.cation == 10.0
        assert phase_1.energy == -90.0
        assert phase_1.x == 0
