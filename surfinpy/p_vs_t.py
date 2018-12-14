import numpy as np

from surfinpy import mu_vs_mu
from scipy.constants import codata

def fit(thermochem, T):
    # to do
    # add to utils
    z = np.polyfit(thermochem[:,0], thermochem[:,1], 3)
    shift = (z[0] * (T ** 3)) + (z[1] * (T ** 2)) + (z[2] * T) + z[3]
    return shift

def vectorize(AE, lnP, T):
    # to do 
    # a and xnew are the same - write function for this and add to utils
    A = np.tile(AE, lnP.size)
    A = np.reshape(A, (lnP.size, T.size))
    xnew = np.tile(T, lnP.size)
    xnew = np.reshape(xnew, (lnP.size, T.size))
    ynew = np.tile(lnP, T.size)
    ynew = np.split(ynew, T.size)
    ynew = np.column_stack(ynew)

    return xnew, ynew, A

def find_phase(data, SEABS):
    # to do
    # add this function to utils and combine with get_hase_data
    S = np.split(SEABS, (len(data) + 1))
    S = np.column_stack(S)
    SE_array = np.argmin(S, axis=1) + 1
    return SE_array

def calculate_surface_energy(AE, lnP, T, coverage, SE, data):
    
    R = codata.value('molar gas constant')
    N_A = codata.value('Avogadro constant')
    SEABS = np.array([])
    for i in range(0, len(AE)):
        xnew, ynew, A = vectorize(AE[i], lnP, T)
        Y = (ynew * (xnew * R))
        SE_Abs_1 = (SE + (coverage[i] / N_A) * (A - Y))
        SEABS = np.append(SEABS, SE_Abs_1) 
    test = np.zeros(lnP.size * T.size)
    test = test + SE
    SEABS = np.insert(SEABS, 0, test)
    SE_array = find_phase(data, SEABS)
    
    return SE_array

def calculate_adsorption_energy(data, stoich, thermochem):
    
    AE = np.array([])
    for i in range(0, len(data)):
        adsorption_energy = (data[i]["Energy"] - (stoich["Energy"] + (data[i]["Y"] * thermochem))) / data[i]["Y"]
        AE = np.append(AE, adsorption_energy)
    AE = AE * 96.485 * 1000
    AE = np.split(AE, len(data))
    return AE

def inititalise(thermochem, adsorbant):
    T = np.arange(2, 1000)
    shift = fit(thermochem, T)
    shift = (T * (shift / 1000)) / 96.485
    adsorbant = adsorbant - shift

    logP = np.arange(-13, 5.5, 0.1)
    lnP = np.log(10 ** logP)
    return lnP, logP, T, adsorbant

def calculate(stoich, data, SE, adsorbant, coverage, thermochem):
    
    lnP, logP, T, thermochem = inititalise(thermochem, adsorbant)

    AE = calculate_adsorption_energy(data, stoich, thermochem) 
    SE_array = calculate_surface_energy(AE, lnP, T, coverage, SE, data)
    ticks = np.unique([SE_array])
    SE_array = mu_vs_mu.transform_numbers(SE_array, ticks)
    phase_grid = np.reshape(SE_array, (lnP.size, T.size))
    data.insert(0, stoich)
    labels = mu_vs_mu.get_labels(ticks, data)
    y = logP
    x = T
    z = phase_grid

    return x, y, z