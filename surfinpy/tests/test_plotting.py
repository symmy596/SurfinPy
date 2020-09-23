import numpy as np
from surfinpy import bulk_mu_vs_mu
from surfinpy import bulk_mu_vs_t
from surfinpy import p_vs_t
from surfinpy import utils as ut
from surfinpy import data
import unittest
from numpy.testing import assert_almost_equal
import os

test_data = os.path.join(os.path.dirname(__file__), 'H2O.txt')


class Testbulk_plotting(unittest.TestCase):

    def chemical_potential_1(self):
        bulk = data.ReferenceDataSet(cation = 1, anion = 2, energy = -100.00, funits = 1)
        phase_1 = data.DataSet(cation = 10, x = 0, y = 10, energy = -90.0, label = "Periclase")
        phase_2 = data.DataSet(cation = 10, x = 0, y = 10, energy = -100.0, label = "Periclase")
        ref = {'Range': [ -3, 2],  'Label': 'test'}
        calculated = bulk_mu_vs_mu.calculate([phase_1, phase_2], bulk, ref, ref, -10, -10)
        ax = calculated.plot_phase()
        assert_almost_equal(calculated.x, ax.lines[0].get_xydata().T[0])

    def chemical_potential_2(self):
        bulk = data.ReferenceDataSet(cation = 1, anion = 2, energy = -100.00, funits = 1)
        phase_1 = data.DataSet(cation = 10, x = 0, y = 10, energy = -90.0, label = "Periclase")
        phase_2 = data.DataSet(cation = 10, x = 0, y = 10, energy = -100.0, label = "Periclase")
        ref = {'Range': [ -3, 2],  'Label': 'test'}
        calculated = bulk_mu_vs_mu.calculate([phase_1, phase_2], bulk, ref, ref, -10, -10)
        p1 = ut.pressure(calculated.x, 298)
        ax = calculated.plot_pressure(298)
        assert_almost_equal(p1, ax.lines[0].get_xydata().T[0])
