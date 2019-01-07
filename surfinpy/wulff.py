from surfinpy import p_vs_t as pt
from surfinpy import utils as ut
import numpy as np
from scipy.constants import codata


def temperature_correction(T, thermochem, adsorbant):
    """Make the energy of the adsorbing species a temperature
    dependent term by scaling it with experimental data.

    Parameters
    ----------
    T : int
        Temperature to scale the energy to
    thermochem : array like
        nist_janaf table
    adsorbant : float
        DFT energy of adsorbant

    Returns
    -------
    adsorbant : float
        Scaled energy of adsorbant
    """
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
    """Calculate the surface energy at a specific temperature
    and pressure.

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
    T : float
        Temperature to calculate surface energy
    P : float
        Pressure to calculate the surface energy
    coverage : array like (default None)
        Coverage of adsorbed specied on the surface.

    Returns
    -------
    SEs : array like
        surface energies for each surface at T/P
    """
    if coverage is None:
        coverage = ut.calculate_coverage(data)
    R = codata.value('molar gas constant')
    N_A = codata.value('Avogadro constant')
    lnP = np.log(10 ** P)
    adsorbant = temperature_correction(T, thermochem, adsorbant)
    AE = pt.adsorption_energy(data, stoich, adsorbant)
    SEs = np.array([SE])
    for i in range(0, len(data)):
        S = SE + (coverage[i] / N_A) * (AE[i] - (lnP * (T * R)))
        SEs = np.append(SEs, S)
    return SEs
