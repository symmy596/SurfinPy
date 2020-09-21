import numpy as np
from surfinpy import bulk_mu_vs_mu
from surfinpy import utils as ut
from surfinpy import data
import unittest
from numpy.testing import assert_almost_equal
import os

test_data = os.path.join(os.path.dirname(__file__), 'H2O.txt')


class Testbulk_mu_vs_mu(unittest.TestCase):

    def test_normalise_phase_energy(self):
        bulk = data.ReferenceDataSet(cation = 1, anion = 2, energy = -100.00, funits = 1)
        phase_1 = data.DataSet(cation = 10, x = 0, y = 0, energy = -90.0, label = "Periclase")
        calculated = bulk_mu_vs_mu.normalise_phase_energy(phase_1, bulk)
        assert calculated == 910.0

    def test_calculate_bulk_energy(self):
        bulk = data.ReferenceDataSet(cation = 1, anion = 2, energy = -100.00, funits = 1)
        phase_1 = data.DataSet(cation = 10, x = 0, y = 0, energy = -90.0, label = "Periclase")
        calculated = bulk_mu_vs_mu.calculate_bulk_energy(10, 10, 10, 10, phase_1, 10)
        assert calculated == 10.0

    def test_evaluate_phases(self):        
        bulk = data.ReferenceDataSet(cation = 1, anion = 2, energy = -100.00, funits = 1)
        phase_1 = data.DataSet(cation = 10, x = 0, y = 0, energy = -90.0, label = "Periclase")
        calculated = bulk_mu_vs_mu.evaluate_phases([phase_1], bulk, np.arange(0, 10, 1), np.arange(0, 10, 1), 1, 10, 10)[0]
        assert calculated[0] == 1

    def test_calculate(self):
        bulk = data.ReferenceDataSet(cation = 1, anion = 2, energy = -100.00, funits = 1)
        phase_1 = data.DataSet(cation = 10, x = 0, y = 10, energy = -90.0, label = "Periclase")
        phase_2 = data.DataSet(cation = 10, x = 0, y = 10, energy = -100.0, label = "Periclase")
        ref = {'Range': [ -3, 2],  'Label': 'test'}
        calculated = bulk_mu_vs_mu.calculate([phase_1, phase_2], bulk, ref, ref, -10, -10)
        assert calculated.z[0, 0] == 0