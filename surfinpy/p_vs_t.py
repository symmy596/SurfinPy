import numpy as np
from scipy.constants import codata
from surfinpy import utils as ut
from surfinpy import pvt_plot


def calculate_surface_energy(AE, lnP, T, coverage, SE, nsurfaces):
    r"""Calculates the surface energy as a function of pressure and
    temperature for each surface system according to

    .. math::
        \gamma_{adsorbed, T, p} = \gamma_{bare} + (C(E_{ads, T} -
        RTln(\frac{p}{p^o})

    where :math:`\gamma_{adsorbed, T, p}` is the surface energy of the surface
    with adsorbed species at a given temperature and pressure,
    :math:`\gamma_{bare}` is the suface energy of the bare surface,
    C is the coverage of adsorbed species, :math:`E_{ads, T}` is the
    adsorption energy, R is the gas constant, T is the temperature, and
    :math:`\frac{p}{p^o}` is the partial pressure.

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
    """
    R = codata.value('molar gas constant')
    N_A = codata.value('Avogadro constant')
    SEABS = np.array([])
    xnew = ut.build_xgrid(T, lnP)
    ynew = ut.build_ygrid(T, lnP)
    for i in range(0, (nsurfaces - 1)):
        SE_Abs_1 = (SE + (coverage[i] / N_A) * (AE[i] - (ynew * (xnew * R))))
        SEABS = np.append(SEABS, SE_Abs_1)
    surface_energy_array = np.zeros(lnP.size * T.size)
    surface_energy_array = surface_energy_array + SE
    SEABS = np.insert(SEABS, 0, surface_energy_array)
    phase_data = ut.get_phase_data(SEABS, nsurfaces)
    return phase_data


def convert_adsorption_energy_units(AE):
    """Converts the adsorption energy into units of KJ/mol

    Parameters
    ----------
    AE : array like
        array of adsorption energies

    Returns
    -------
    array like
        array of adsorption energies in units of KJ/mol
    """
    return (AE * 96.485 * 1000)


def calculate_adsorption_energy(adsorbed_energy, slab_energy, n_species,
                                adsorbant_t):
    """Calculates the adsorption energy in units of eV

    Parameters
    ----------
    adsorbed_energy : float
        slab energy of slab and adsorbed species from DFT
    slab_energy : float
        bare slab energy from DFT
    n_species : int
        number of adsorbed species at the surface
    adsorbant_t : array like
        dft energy of adsorbing species as a function of temperature

    Returns
    -------
    array like
        adsorption energy as a function of temperature
    """
    return ((adsorbed_energy - (slab_energy + (n_species * adsorbant_t))) /
            n_species)


def adsorption_energy(data, stoich, adsorbant_t):
    '''From the dft data provided - calculate the adsorbation energy of a
    species at the surface.

    Parameters
    ----------
    data : list
        list of dictionaries containing info about each calculation
    stoich : dict
        info about the stoichiometric surface calculation
    adsorbant_t : array like
        dft energy of adsorbing species as a function of temperature

    Returns
    -------
    AE : array like
        Adsorbtion energy of adsorbing species in each calculation
        as a function of temperature
    '''
    AE = np.array([])
    for i in range(0, len(data)):
        AE = np.append(AE, (calculate_adsorption_energy(data[i]["Energy"],
                                                        stoich["Energy"],
                                                        data[i]["Y"],
                                                        adsorbant_t)))
    AE = convert_adsorption_energy_units(AE)
    AE = np.split(AE, len(data))
    return AE


def inititalise(thermochem, adsorbant):
    '''Builds the numpy arrays for each calculation.

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
        log of lnP (hard coded range -13 - 5.0)
    T : array like
        array of temperature values (hard coded range 2 - 1000 K)
    adsrobant_t : array like
        dft values of adsorbant scaled to temperature
    '''
    T = np.arange(2, 1000)
    shift = ut.fit(thermochem[:, 0], thermochem[:, 2], T)
    shift = (T * (shift / 1000)) / 96.485
    adsorbant_t = adsorbant - shift
    logP = np.arange(-13, 5.5, 0.1)
    lnP = np.log(10 ** logP)
    return lnP, logP, T, adsorbant_t


def calculate(stoich, data, SE, adsorbant, thermochem, coverage=None):
    '''Collects input variables and intitialises the calculation.

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
    coverage : array like (default None)
        Numpy array containing the different coverages of adsorbant.
    thermochem : array like
        Numpy array containing thermochemcial data downloaded from NIST_JANAF
        for the adsorbing species.

    Returns
    -------
    system : class object
        plotting object
    '''
    if coverage is None:
        coverage = ut.calculate_coverage(data)
    lnP, logP, T, adsorbant_t = inititalise(thermochem, adsorbant)
    nsurfaces = len(data) + 1
    AE = adsorption_energy(data, stoich, adsorbant_t)
    SE_array = calculate_surface_energy(AE, lnP, T,
                                        coverage, SE,
                                        nsurfaces)
    ticks = np.unique([SE_array])
    SE_array = ut.transform_numbers(SE_array, ticks)
    phase_grid = np.reshape(SE_array, (lnP.size, T.size))
    data.insert(0, stoich)
    y = logP
    x = T
    z = phase_grid
    system = pvt_plot.PVTPlot(x, y, z)
    return system
