import numpy as np
from scipy.constants import codata
from surfinpy import utils as ut


def vectorize(AE, lnP, T):
    '''Create 2D arrays of adsorption energy, temperature and pressure values

    Parameters
    ----------
    AE : array like
        adsorption energies at varying temerature
    lnP : array like
        Pressure range
    T : array like
        Temperature range

    Returns
    -------
    xnew : array like
        2D array of temeoerature values
    ynew : array like
        2D array of pressure values
    A : array like
        2D array of adsorption energies
    '''
    A = np.tile(AE, lnP.size)
    A = np.reshape(A, (lnP.size, T.size))
    xnew = np.tile(T, lnP.size)
    xnew = np.reshape(xnew, (lnP.size, T.size))
    ynew = np.tile(lnP, T.size)
    ynew = np.split(ynew, T.size)
    ynew = np.column_stack(ynew)

    return xnew, ynew, A


def calculate_surface_energy(AE, lnP, T, coverage, SE, data, nsurfaces):
    '''Calculate the surface energy as a function of pressure and temperature
    for each surface calculation.

    Parameters
    ----------
    AE : list
        list of adsorption energies
    lnP : array like
        full pressure range
    T : array like
        full temperature range
    coverage : array like
        surface coverage of adsorbing species in each calculation
    SE : float
        surface energy of stoichiomteric surface
    data : list
        list of dictionaries containing info on each surface
    nsurfaces : int
        total number of surface

    Returns
    -------
    SE_array : array like
        array of integers corresponding to lowest surface energies
    '''
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
    SE_array = ut.get_phase_data(SEABS, nsurfaces)
    return SE_array


def calculate_adsorption_energy(data, stoich, thermochem):
    '''From the dft data provided - calculate the adsorbation energy

    Parameters
    ----------
    data : list
        list of dictionaries containing info about each calculation
    stoich : dict
        info about the stoichiometric surface calculation
    termochem : float
        dft energy of adsorbing species

    Returns
    -------
    AE : array like
        Adsorbtion energy of adsorbing species in each calculation
    '''
    AE = np.array([])
    for i in range(0, len(data)):
        adsorption_energy = (data[i]["Energy"] - (stoich["Energy"] + 
                            (data[i]["Y"] * thermochem))) / data[i]["Y"]
        AE = np.append(AE, adsorption_energy)
    AE = AE * 96.485 * 1000
    AE = np.split(AE, len(data))
    return AE


def inititalise(thermochem, adsorbant):
    '''initialise the arrays

    Parameters
    ----------
    thermochem : array like
        array containing NIST_JANAF thermochemical data
    adsorbant : float
        dft energy of adsorbing species

    Returns
    -------
    lnP : array like
        numpy array of pressure values
    logP : array like
        log of lnP
    T : array like
        array of temperature values
    adsrobant : array like 
        dft values of adsorbant scaled to temperature
    '''
    T = np.arange(2, 1000)
    shift = ut.fit(thermochem, T)
    shift = (T * (shift / 1000)) / 96.485
    adsorbant = adsorbant - shift

    logP = np.arange(-13, 5.5, 0.1)
    lnP = np.log(10 ** logP)
    return lnP, logP, T, adsorbant

def calculate(stoich, data, SE, adsorbant, thermochem, coverage=None):
    '''collects input variables and intitialises the calculation.

    Parameters
    ----------
    stoich : dictionary 
        information about the stoichiometric surface
    data : list
        list of dictionaries containing information on the "adsorbed" surfaces
    SE : float
        surface energy of the stoichiomteric surface
    adsorbant : float
        dft energy of adsorbing species
    coverage : array like
        Numpy array containing the different coverages of adsorbant. 
    thermochem : array like
        Numpy array containing thermochemcial data downloaded from NIST_JANAF
        for the adsorbing species. 

    Returns
    -------
    '''
    if Coverage is None:
        coverage = sut.calculate_coverage(data)
    lnP, logP, T, thermochem = inititalise(thermochem, adsorbant)
    nsurfaces = len(data) + 1
    AE = calculate_adsorption_energy(data, stoich, thermochem) 
    SE_array = calculate_surface_energy(AE, lnP, T, coverage, SE, data, nsurfaces)
    ticks = np.unique([SE_array])
    SE_array = ut.transform_numbers(SE_array, ticks)
    phase_grid = np.reshape(SE_array, (lnP.size, T.size))
    data.insert(0, stoich)
    labels = ut.get_labels(ticks, data)
    y = logP
    x = T
    z = phase_grid
    return x, y, z