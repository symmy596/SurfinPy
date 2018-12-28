from surfinpy import p_vs_t as pt
from surfinpy import utils as ut
import numpy as np
from scipy.constants import codata


def temperature_correction(T, thermochem, adsorbant):
    temperature_range = np.arange(2, 1000)
    shift = ut.fit(thermochem[:, 0], thermochem[:, 2], temperature_range)
    shift = (T * (shift[(T - 1)] / 1000)) / 96.485
    adsorbant = adsorbant - shift
    return adsorbant


def calculate_surface_energy(stoich,
                             data,
                             SE,
                             adsorbant,
                             thermochem,
                             T,
                             P,
                             coverage=None):
    if coverage is None:
        coverage = ut.calculate_coverage(data)
    R = codata.value('molar gas constant')
    N_A = codata.value('Avogadro constant')
    lnP = np.log(10 ** P)
    AE = pt.adsorption_energy(data, stoich, adsorbant)
    adsorbant = temperature_correction(T, thermochem, adsorbant)
    SEs = np.array([SE])
    for i in range(0, len(data)):
        S = SE + (coverage[i] / N_A) * (AE[i] - (lnP * (T * R)))
        SEs = np.append(SEs, S)
    return SEs
