import numpy as np
from scipy.constants import codata
from surfinpy import phaseplot
from surfinpy import utils as ut


def pressure(chemical_potential, t):
    r"""Converts chemical potential at a specific 
    temperature (T) to a pressure value.

    .. math::
        P = \frac{\mu}{k * T}

    where P is the pressure, :math:`\mu` is the chemcial potential, k is the
    Boltzmann constant and T is the temperature.

    Parameters
    ----------
    chemical_potential : array like
        delta mu values
    t : int
        temperature

    Returns
    -------
    pressure : array like
        pressure values as a function of chemcial potential
    """
    k = codata.value('Boltzmann constant in eV/K')
    pressure = chemical_potential / (k * t * 2.203)
    return pressure


def calculate_excess(adsorbant, slab_cations, area, bulk, nspecies=1, check=False):
    r"""calculates the excess of a given species at the surface. Depending on the nature
    of the species, there are two ways to do this. If the species is a constituent part
    of the surface, e.g. Oxygen in :math:`TiO_2` then the calculation must account for 
    the stoichiometry of that material. 
    Using the :math:`TiO_2` example

    .. math::
        \Gamma = \frac{N_O - \frac{1}{2}N_{Ti}}{2S}

    where :math:`N_O` is the number of oxygen in the slab, N_Ti is the number of 
    titanium in the slab, S is the surface area and the 1/2 refers to the 2 oxygen to 1 titanium 
    stoichiometry of :math:`TiO_2`. 
    If the species is just an external adsorbant, e.g. water or carbon dioxide then one does not 
    need to consider the state of the surface, as there was none there to begin with. 

    .. math::
        \Gamma = \frac{N_{Water}}{2S}

    where :math:`N_{Water}` is the number of water molecules and S is the surface area.

    Parameters
    ----------
    adsorbant : int
        Number of species
    slab_cations : int
        Number of cations
    area : float
        Area of surface
    bulk : dic
        Dictonary of bulk properties
    nspecies : int (optional)
        number of external species
    check : bool (optional)
        Check if this is an external or constituent species. 

    Returns
    -------
    float: 
        Surface excess of given species. 
    """
    if check is True and nspecies == 1:   
        return ((adsorbant - ((bulk['O'] / bulk['M']) * slab_cations)) / (2 * area))
    else:
        return (adsorbant / (area * 2))


def calculate_normalisation(slab_energy, slab_cations, bulk, area):
    r"""Normalises the slab energy relative to the bulk material. Thus allowing the
    different slab calculations to be compared.

    .. math::
        Normalised_{Constant} = \frac{E_{Slab} - \frac{N_{Cat}}{Bulk_{Cat}} * 
        \frac{E_{Bulk}}{N_{Units}}}{2S}

    where :math:`Normalised_{Constant}' is the slab energy normalised to the bulk, 
    :math:`E_{slab}` is the DFT slab energy, :math:`N_{Cat}' is the number of slab
    cations, :math:`Bulk_{Cat}` is the number of bulk cations, :math:`E_{Bulk}` is 
    the DFT bulk energy, :math:`N_{Units}` is the number of bulk formula units and S
    is the surface area. 

    Parameters
    ----------
    slab_energy : float
        Energy of the slab from DFT
    slab_cations : int
        Total number of cations in the slab
    bulk : dictionary
        Dictionary of bulk properties
    area : float
        Surface area

    Returns
    -------
    float:
        Constant normalising the slab energy to the bulk energy.
    """
    return ((slab_energy - (slab_cations / bulk['M']) * (bulk['Energy'] / bulk['F-Units'])) / (2 * area))


def calculate_surface_energy(deltamux, deltamuy, xshiftval, yshiftval,
                             xexcess, yexcess, normalised_bulk):
    r"""This function calculates the surface for a given chemical potential of
    species x and species y which in this example is oxygen and water, according to

    .. math::
        \gamma_{Surf} = \frac{1}{2S} \Bigg( E_{MO}^{slab} - \frac{N_M}{x} E_{MO}^{Bulk} \Bigg) -
         \Delta \Gamma_O \mu_O - \Delta \Gamma_{H_2O} \mu_{H_2O} - \Delta n_O \mu_O (T) -
         \Delta n_{H_2O} \mu_{H_2O} (T)

    where S is the surface area, :math:`E_{MO}^{slab}` is the DFT energy of the stoichiometric slab,
    :math:`N_M` is the number of cations in the structure,
    x is the number of cations in the bulk unit cell, :math:`E_{MO}^{Bulk}` is the DFT energy of the bulk unit cell,
    :math:`\Gamma_O`  :math:`\Gamma_{H_2O}` is the excess oxygen / water at the surface and :math:`\mu_O` 
    :math:`\mu_{H_2O}` is the oxygen / water chemcial potential.

    Parameters
    ----------
    deltamux : array like
        Chemical potential of species x
    deltamuy : array like
        Chemical potential of species y
    xshiftval : float
        shift value for the x axis - corresponding to the 0K DFT energy or temperature corrected DFT energy
    yshiftval : float
        shift value for the y axis - corresponding to the 0K DFT energy or temperature corrected DFT energy
    xexcess : float
        Surface excess of species x
    yexcess : float
        Surface excess of species y
    normalised_bulk : float
        Slab energy normalised to the bulk value.

    Returns
    -------
    array like:
        2D array of surface energies as a function of chemical potential of x and y
    """
    return (normalised_bulk - (deltamux * xexcess) - (deltamuy * yexcess) - (
        xshiftval * xexcess) - (yshiftval * yexcess))


def evaluate_phases(data, bulk, x, y, nsurfaces, xshiftval, yshiftval):
    """Calculates the surface energies of each phase as a function of chemical
    potential of x and y. Then uses this data to evaluate which phase is most
    stable at that x/y chemical potential cross section.

    Parameters
    ----------
    data : list
        List containing the dictionaries for each phase
    bulk : dictionary
        dictionary containing data for bulk
    x : dictionary
        X axis chemical potential values
    y : dictionary
        Y axis chemical potential values
    nsurfaces : int
        Number of phases
    xshiftval : float
        DFT 0K energy for species x
    yshiftval : float
        DFT 0K energy for species y

    Returns
    -------
    phase_data  : array like
        array of ints, with each int corresponding to a phase.
    """
    Xnew = np.tile(x, y.size)
    Xnew = np.reshape(Xnew, (y.size, x.size))
    Ynew = np.tile(y, x.size)
    Ynew = np.split(Ynew, x.size)
    Ynew = np.column_stack(Ynew)
    S = np.array([])
    for k in range(0, nsurfaces):
        xexcess = calculate_excess(data[k]['X'], data[k]['M'],
                                   data[k]['Area'], bulk,
                                   data[k]['nSpecies'], check=True)
        yexcess = calculate_excess(data[k]['Y'], data[k]['M'], data[k]['Area'], bulk)
        normalised_bulk = calculate_normalisation(data[k]['Energy'],
                                                  data[k]['M'], bulk,
                                                  data[k]['Area'])
        SE = calculate_surface_energy(Xnew, Ynew,
                                      xshiftval,
                                      yshiftval,
                                      xexcess,
                                      yexcess,
                                      normalised_bulk)
        S = np.append(S, SE)
    phase_data = ut.get_phase_data(S, nsurfaces)
    return phase_data


def calculate(data, bulk, deltaX, deltaY, xshiftval=0, yshiftval=0,
              temperature=0, convert_pressure=False, output="Phase.png"):
    '''Initialise the surface energy calculation.

    Parameters
    ----------
    data : list
        List containing the dictionary data for each phase
    bulk : dictionary
        Dctionary containing data for bulk
    deltaX : dictionary
        X axis chemical potential values
    DeltaY : dictionary
        Y axis chemical potential values
    xshiftval : float
        DFT energy of adsorbing species
    yshiftval : float
        DFT energy of adsorbing species
    temperature : int
        Temperature
    convert_pressure : bool
        Parameter to turn on conversion of chemical potential to pressure
    output : str
        Output file name

    Returns
    -------
    '''
    data = sorted(data, key=lambda k: (k['Y']))
    nsurfaces = len(data)
    X = np.arange(deltaX['Range'][0], deltaX['Range'][1], 0.025, dtype="float")
    Y = np.arange(deltaY['Range'][0], deltaY['Range'][1], 0.025, dtype="float")
    X = X - xshiftval
    Y = Y - yshiftval
    phases = evaluate_phases(data, bulk, X, Y,
                                  nsurfaces, xshiftval, yshiftval)
    ticks = np.unique([phases])
    phases = ut.transform_numbers(phases, ticks)
    Z = np.reshape(phases, (Y.size, X.size))
    labels = ut.get_labels(ticks, data)
    if xshiftval == 0 and yshiftval == 0:
        phaseplot.plot_phase(X, Y, Z, ticks, labels, deltaX['Label'],
                             deltaY['Label'], temperature, output)
    elif convert_pressure is False:
        phaseplot.plot_phase(X, Y, Z, ticks, labels, deltaX['Label'],
                             deltaY['Label'], temperature, output)
    elif convert_pressure is True:
        p1 = pressure(X, temperature)
        p2 = pressure(Y, temperature)
        phaseplot.plot_mu_p(X, Y, Z, p1, p2, ticks, labels, deltaX['Label'],
                            deltaY['Label'], temperature, output)
        phaseplot.plot_pressure(p1, p2, Z, ticks, labels,
                                deltaX['Label'], deltaY['Label'], temperature,
                                output="pressure.png")
