import p_vs_t as pt
import utils as ut
import numpy as np
from scipy.constants import codata

def calculate_surface_energy(stoich, data, SE, adsorbant, thermochem, T, P, coverage=None):
    if coverage is None:
        coverage = ut.calculate_coverage(data)
    R = codata.value('molar gas constant')
    N_A = codata.value('Avogadro constant')
    P = np.log(10 ** P)
    Tarr = np.arange(2, 1000)
    shift = ut.fit(thermochem, Tarr)
    shift = (Tarr * (shift / 1000)) / 96.485
    for i in range(0, shift.size):
        if Tarr[i] == T:
            X = shift[i]
    adsorbant = adsorbant - X
    
    AE = pt.calculate_adsorption_energy(data, stoich, adsorbant)
    Y = P * (T * R)
    SEs = np.array([SE])
    for i in range(0, len(data)):
        S = SE + (coverage[i] / N_A) * (AE[i] - Y)
        SEs = np.append(SEs, S)
    return SEs



