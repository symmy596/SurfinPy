import numpy as np
from surfinpy import chemical_potential_plot
from surfinpy import utils as ut


def calculate_excess(adsorbant, slab_cations, area, bulk,
                     nspecies=1, check=False):
    r"""Calculates the excess of a given species at the surface.
    Depending on the nature of the species, there are two ways to do this.
    If the species is a constituent part of the surface, e.g.
    Oxygen in :math:`TiO_2` then the calculation must account for
    the stoichiometry of that material. Using the :math:`TiO_2` example

    .. math::
        \Gamma_O = \frac{1}{2A} \Bigg( nO_{Slab} - \frac{nO_{Bulk}}
        {nTi_{Bulk}}nTi_{Slab}  \Bigg)

    where :math:`nO_{Slab}` is the number of oxygen in the slab,
    :math:`nO_{Bulk}` is the number of oxygen in the bulk,
    A is the surface area, :math:`nTi_{Bulk}` is the number of Ti in
    the bulk and :math:`nTi_{Slab}` is the number of Ti in the slab. 
    If the species is just an external adsorbant, e.g. water or carbon dioxide
    then one does not need to consider the state of the surface,
    as there was none there to begin with.

    .. math::
        \Gamma_{H_2O} = \frac{nH_2O}{2A}

    where :math:`nH_2O` is the number of water molecules and A is the
    surface area.

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
        return ((adsorbant - ((bulk['Anion'] / bulk['Cation']) *
                 slab_cations)) / (2 * area))
    else:
        return (adsorbant / (area * 2))


def calculate_normalisation(slab_energy, slab_cations, bulk, area):
    r"""Normalises the slab energy relative to the bulk material.
    Thus allowing the different slab calculations to be compared.

    .. math::
        Energy = \frac{1}{2A} \Bigg( E_{MO}^{slab} -
        \frac{nCat_{slab}}{nCat_{Bulk}} E_{MO}^{Bulk} \Bigg)

    where Energy is the slab energy normalised to the
    bulk, :math:`E_{MO}^{slab}` is the DFT slab energy, :math:`nCat_{slab}`
     is the number of slab cations, :math:`nCat_{Bulk}` is the number of bulk
    cations, :math:`E_{MO}^{Bulk}` is the DFT bulk energy A is the surface
    area.

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
    return ((slab_energy - (slab_cations / bulk['Cation']) * (bulk['Energy'] /
            bulk['F-Units'])) / (2 * area))


def calculate_surface_energy(deltamux, deltamuy, x_energy, y_energy,
                             xexcess, yexcess, normalised_bulk):
    r"""Calculates the surface for a given chemical potential of
    species x and species y for a single phase.

    .. math::
        \gamma_{Surf} = \frac{1}{2S} \Bigg( E_{MO}^{slab} -
        \frac{nCat_{Slab}}{nCat_{Bulk}} E_{MO}^{Bulk} \Bigg) -
         \Gamma_O \mu_O - \Gamma_{H_2O} \mu_{H_2O} -
         \Gamma_O  \mu_O (T) - \Gamma_{H_2O} \mu_{H_2O} (T)

    where S is the surface area, :math:`E_{MO}^{slab}` is the DFT energy of
    the stoichiometric slab, :math:`nCat_{Slab}` is the number of cations
    in the slab, :math:`nCat_{Slab}` is the number of cations in the bulk
    unit cell, :math:`E_{MO}^{Bulk}` is the DFT energy of the bulk unit cell,
    :math:`\Gamma_O`  :math:`\Gamma_{H_2O}` is the excess oxygen / water at
    the surface and :math:`\mu_O` :math:`\mu_{H_2O}` is the oxygen /
    water chemcial potential.

    Parameters
    ----------
    deltamux : array like
        Chemical potential of species x
    deltamuy : array like
        Chemical potential of species y
    x_energy : float
        DFT energy or temperature corrected DFT energy
    y_energy : float
        DFT energy or temperature corrected DFT energy
    xexcess : float
        Surface excess of species x
    yexcess : float
        Surface excess of species y
    normalised_bulk : float
        Slab energy normalised to the bulk value.

    Returns
    -------
    array like:
        2D array of surface energies as a function of
        chemical potential of x and y
    """
    return (normalised_bulk - (deltamux * xexcess) - (deltamuy * yexcess) - (
        x_energy * xexcess) - (y_energy * yexcess))


def evaluate_phases(data, bulk, x, y, nsurfaces, x_energy, y_energy):
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
    x_energy : float
        DFT 0K energy for species x
    y_energy : float
        DFT 0K energy for species y

    Returns
    -------
    phase_data  : array like
        array of ints, with each int corresponding to a phase.
    """
    xnew = ut.build_xgrid(x, y)
    ynew = ut.build_ygrid(x, y)
    S = np.array([])
    for k in range(0, nsurfaces):
        xexcess = calculate_excess(data[k]['X'], data[k]['Cation'],
                                   data[k]['Area'], bulk,
                                   data[k]['nSpecies'], check=True)
        yexcess = calculate_excess(data[k]['Y'], data[k]['Cation'],
                                   data[k]['Area'], bulk)
        normalised_bulk = calculate_normalisation(data[k]['Energy'],
                                                  data[k]['Cation'], bulk,
                                                  data[k]['Area'])
        SE = calculate_surface_energy(xnew, ynew,
                                      x_energy,
                                      y_energy,
                                      xexcess,
                                      yexcess,
                                      normalised_bulk)
        S = np.append(S, SE)
    phase_data = ut.get_phase_data(S, nsurfaces)
    return phase_data


def temperature_correction(nist_file, temperature):
    """Use experimental data to correct the DFT free energy of an adsorbing
    species to a specific temperature.

    Parameters
    ----------
    nist_file : array like
        numpy array containing experiemntal data from NIST_JANAF
    temperature : int
        Temperature to correct to

    Returns
    -------
    gibbs : float
        correct free energy
    """
    nist_data = ut.read_nist(nist_file)
    h0 = nist_data[0, 4]
    fitted_s = ut.fit(nist_data[:, 0], nist_data[:, 2], np.arange(1, 1000))
    fitted_h = ut.fit(nist_data[:, 0], nist_data[:, 4], np.arange(1, 1000))
    fitted_h = fitted_h + h0
    gibbs = ut.calculate_gibbs(np.arange(1, 1000), fitted_s, fitted_h)
    return gibbs[(temperature - 1)]


def calculate(data, bulk, deltaX, deltaY, x_energy=0, y_energy=0,
              temperature=0, output="Phase_Diagram.png"):
    """Initialise the surface energy calculation.

    Parameters
    ----------
    data : list
        List of dictionaries for each phase
    bulk : dictionary
        Dictionary containing data for bulk
    deltaX : dictionary
        Range of chemical potential/label for species X 
    DeltaY : dictionary
        Range of chemical potential/label for species Y 
    x_energy : float
        DFT energy of adsorbing species
    y_energy : float
        DFT energy of adsorbing species
    temperature : int
        Temperature
    output : str
        Output file name

    Returns
    -------
    system : class obj
        Plotting object
    """
    data = sorted(data, key=lambda k: (k['Y']))
    nsurfaces = len(data)
    X = np.arange(deltaX['Range'][0], deltaX['Range'][1],
                  0.025, dtype="float")
    Y = np.arange(deltaY['Range'][0], deltaY['Range'][1],
                  0.025, dtype="float")
    X = X - x_energy
    Y = Y - y_energy
    phases = evaluate_phases(data, bulk, X, Y,
                             nsurfaces, x_energy, y_energy)
    ticks = np.unique([phases])
    phases = ut.transform_numbers(phases, ticks)
    Z = np.reshape(phases, (Y.size, X.size))
    labels = ut.get_labels(ticks, data)
    system = chemical_potential_plot.ChemicalPotentialPlot(X,
                                                           Y,
                                                           Z,
                                                           labels,
                                                           ticks,
                                                           deltaX['Label'],
                                                           deltaY['Label'])
    return system
