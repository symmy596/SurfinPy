from surfinpy import p_vs_t as pt
import numpy as np
from scipy.constants import codata

def calculate_surface_energy(stoich, data, SE, adsorbant, coverage, thermochem, T, P):
    
    R = codata.value('molar gas constant')
    N_A = codata.value('Avogadro constant')
    P = np.log(10 ** P)
    Tarr = np.arange(2, 1000)
    shift = pt.fit(thermochem, Tarr)
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




