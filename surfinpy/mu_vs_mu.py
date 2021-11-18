import numpy as np
from surfinpy import plotting
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
    adsorbant : :py:attr:`int`
        Number of species
    slab_cations : :py:attr:`int`
        Number of cations
    area : :py:attr:`float`
        Area of surface
    bulk : :py:attr:`dict`
        Dictonary of bulk properties
    nspecies : :py:attr:`int`
        number of external species
    check : :py:attr:`bool`
        Check if this is an external or constituent species.

    Returns
    -------
    :py:attr:`float`
        Surface excess of given species.
    """
    if check is True and nspecies == 1:
        return ((adsorbant - ((bulk.anion / bulk.cation) *
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
    slab_energy : :py:attr:`float`
        Energy of the slab from DFT
    slab_cations : :py:attr:`int`
        Total number of cations in the slab
    bulk : :py:class:`surfinpy.data.DataSet`
        Bulk properties
    area : :py:attr:`float`
        Surface area

    Returns
    -------
    :py:attr:`float`
        Constant normalising the slab energy to the bulk energy.
    """
    return ((slab_energy - (slab_cations / bulk.cation) * (bulk.energy /
            bulk.funits)) / (2 * area))

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
    deltamux : :py:attr:`array_like`
        Chemical potential of species x
    deltamuy : :py:attr:`array_like`
        Chemical potential of species y
    x_energy : :py:attr:`float`
        DFT energy or temperature corrected DFT energy
    y_energy : :py:attr:`float`
        DFT energy or temperature corrected DFT energy
    xexcess : :py:attr:`float`
        Surface excess of species x
    yexcess : :py:attr:`float`
        Surface excess of species y
    normalised_bulk : :py:attr:`float`
        Slab energy normalised to the bulk value.

    Returns
    -------
    :py:attr:`array_like`
        2D array of surface energies as a function of
        chemical potential of x and y
    """
    return ((normalised_bulk- (deltamux * xexcess) - (deltamuy * yexcess) - (
        x_energy * xexcess)- (y_energy * yexcess)) * 16.021)


def evaluate_phases(data, bulk, x, y, nsurfaces, x_energy, y_energy):
    """Calculates the surface energies of each phase as a function of chemical
    potential of x and y. Then uses this data to evaluate which phase is most
    stable at that x/y chemical potential cross section.

    Parameters
    ----------
    data : :py:attr:`list`
        List containing the :py:class:`surfinpy.data.DataSet` for each phase
    bulk : :py:class:`surfinpy.data.DataSet`
        Data for bulk
    x : :py:attr:`dict`
        X axis chemical potential values
    y : :py:attr:`dict`
        Y axis chemical potential values
    nsurfaces : :py:attr:`int`
        Number of phases
    x_energy : :py:attr:`float`
        DFT 0K energy for species x
    y_energy : :py:attr:`float`
        DFT 0K energy for species y

    Returns
    -------
    phase_data  : :py:attr:`array_like`
        array of ints, with each int corresponding to a phase.
    """
    xnew = ut.build_xgrid(x, y)
    ynew = ut.build_ygrid(x, y)
    S = np.array([])
    for k in range(0, nsurfaces):
        xexcess = calculate_excess(data[k].x, data[k].cation,
                                   data[k].area, bulk,
                                   data[k].nspecies, check=True)
        yexcess = calculate_excess(data[k].y, data[k].cation,
                                   data[k].area, bulk)
        normalised_bulk = calculate_normalisation(data[k].energy,
                                                  data[k].cation, bulk,
                                                  data[k].area)
        SE = calculate_surface_energy(xnew, ynew,
                                      x_energy,
                                      y_energy,
                                      xexcess,
                                      yexcess,
                                      normalised_bulk)
        S = np.append(S, SE)
    phase_data, surface_energy = ut.get_phase_data(S, nsurfaces)
    return phase_data, surface_energy
    
def calculate(data, bulk, deltaX, deltaY, x_energy=0, y_energy=0, increments=0.025):
    """Initialise the surface energy calculation.

    Parameters
    ----------
    data : :py:attr:`list`
        List of :py:class:`surfinpy.data.DataSet` for each phase
    bulk : :py:class:`surfinpy.data.ReferenceDataSet`
        Data for bulk
    deltaX : :py:attr:`dict`
        Range of chemical potential/label for species X 
    DeltaY : :py:attr:`dict`
        Range of chemical potential/label for species Y 
    x_energy : :py:attr:`float`
        DFT energy of adsorbing species
    y_energy : :py:attr:`float`
        DFT energy of adsorbing species

    Returns
    -------
    system : :py:class:`surfinpy.plotting.ChemicalPotentialPlot`
        Plotting object
    """
    nsurfaces = len(data)
    
    X = np.arange(deltaX['Range'][0], deltaX['Range'][1],
                  increments, dtype="float")
    Y = np.arange(deltaY['Range'][0], deltaY['Range'][1],
                  increments, dtype="float")
    X = X - x_energy
    Y = Y - y_energy
    phases, SE = evaluate_phases(data, bulk, X, Y,
                             nsurfaces, x_energy, y_energy)
    ticks = np.unique([phases])
    colors = ut.list_colors(data, ticks)
    phases = ut.transform_numbers(phases, ticks)
    Z = np.reshape(phases, (Y.size, X.size))
    SE = np.reshape(SE, (Y.size, X.size))
    labels = ut.get_labels(ticks, data)
    system = plotting.ChemicalPotentialPlot(X,
                                            Y,
                                            Z,
                                            labels,
                                            ticks,
                                            colors,
                                            deltaX['Label'],
                                            deltaY['Label'])
    return system, SE


