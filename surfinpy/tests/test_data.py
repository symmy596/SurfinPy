import numpy as np
from surfinpy import bulk_mu_vs_t
from surfinpy import utils as ut
from surfinpy import data
import unittest
from numpy.testing import assert_almost_equal
import os

test_data = os.path.join(os.path.dirname(__file__), 'test.yaml')


class TestReferenceData(unittest.TestCase):

    def test_reference_data_1(self):
        bulk = data.ReferenceDataSet(cation = 1, anion = 2, energy = -90.00, funits = 1)
        assert bulk.energy == -90.00
        assert bulk.cation == 1
        assert bulk.anion == 2

    def test_reference_data_2(self):
        bulk = data.ReferenceDataSet(cation = 1, anion = 2, energy = -90.00, entropy = True, file = test_data, funits = 10, temp_range=[100, 120])
        assert_almost_equal(bulk.svib[0], 1.6076787893E-03)

    def test_dataset_1(self):
        phase_1 = data.DataSet(cation = 10, x = 0, y = 0, energy = -90.0, label = "Periclase")
        assert phase_1.cation == 10.0
        assert phase_1.energy == -90.0
        assert phase_1.x == 0

    def test_dataset_2(self):
        phase_1 = data.DataSet(cation = 10, x = 0, y = 0, energy = -90.0, label = "Periclase", entropy = True, file = test_data, funits = 10, temp_range=[100, 120])
        assert_almost_equal(phase_1.svib[0], 1.6076787893E-03)