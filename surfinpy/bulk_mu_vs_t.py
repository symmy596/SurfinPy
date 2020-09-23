import numpy as np
from surfinpy import plotting
from surfinpy import utils as ut
from surfinpy import vibrational_data as vd

def normalise_phase_energy(phase, bulk):
    r"""
    Description Needed

    Parameters
    ----------
    phase : (:py:class:`surfinpy.data.DataSet`):
        surfinpy dataset object.
    bulk : (:py:class:`surfinpy.data.ReferenceDataSet`):
        surfinpy ReferenceDataSet object.

    Returns
    -------
    float:
        Constant normalising the slab energy to the bulk energy.
    """
    return ((phase.energy + (phase.zpe * phase.funits)) - (phase.cation / bulk.cation) * ((bulk.energy /
            bulk.funits)+ bulk.zpe))

def calculate_bulk_energy(deltamux, ynew,  
                          x_energy,
                          z_energy, deltamuy,
                          phase,
                          bulk,
                          normalised_bulk,
                          exp_xnew, exp_znew, new_bulk_svib, new_data_svib): 
    """Description needed

    Parameters
    ----------
    deltamux : (:py:attr:`array_like`):
        Chemical potential of species x
    ynew : (:py:attr:`array_like`):
        description needed
    x_energy : (:py:attr:`float`):
        DFT energy or temperature corrected DFT energy
    y_energy : (:py:attr:`float`):
        DFT energy or temperature corrected DFT energy
    deltamuy : (:py:attr:`array_like`):
        Chemical potential of species y
    phase : (:py:class:`surfinpy.data.DataSet`):
        DFT calculation
    bulk : (:py:class:`surfinpy.data.ReferenceDataSet`):
        DFT calculation        
    normalised_bulk : (:py:attr:`float`):
        Bulk energy normalised to the bulk value.
    exp_new :  (:py:attr:`array_like`):
        description needed
    exp_znew :  (:py:attr:`array_like`):
        description needed
    new_bulk_svib :  (:py:attr:`float`):
        description needed
    new_data_svib :  (:py:attr:`float`):
        description needed
    
    Returns
    -------
     (:py:attr:`array_like`):
        description needed
    """
    return (
        normalised_bulk - deltamux * phase.x - deltamuy * phase.y - (
        (x_energy + exp_xnew) * phase.x) - ((z_energy + exp_znew) * phase.y)-
        (new_data_svib * phase.funits - ((phase.cation/ (bulk.cation) * new_bulk_svib))))

def evaluate_phases(data, bulk, x, y,
                    nphases, x_energy, y_energy,
                    mu_z, exp_x, exp_z):
    """Calculates the surface energies of each phase as a function of chemical
    potential of x and y. Then uses this data to evaluate which phase is most
    stable at that x/y chemical potential cross section.

    Parameters
    ----------
    data : (:py:attr:`list`):
        List containing the (:py:class:`surfinpy.data.DataSet`): objects for each phase
    bulk : (:py:class:`surfinpy.data.ReferenceDataSet`):
        Reference dataset
    x : (:py:attr:`dict`):
        X axis chemical potential values
    y : (:py:attr:`dict`):
        Y axis chemical potential values
    nphases : (:py:attr:`int`):
        Number of phases
    x_energy : (:py:attr:`float`):
        DFT 0K energy for species x
    y_energy : (:py:attr:`float`):
        DFT 0K energy for species y
    mu_z :  (:py:attr:`float`):
        Description Needed
    exp_x : (:py:attr:`float`):
        Description Needed
    exp_z : (:py:attr:`float`):
        Description Needed

    Returns
    -------
    phase_data  : (:py:attr:`array_like`):
        array of ints, with each int corresponding to a phase.
    """
    xnew = ut.build_xgrid(x, y)
    ynew = ut.build_ygrid(x, y)
    znew = (xnew * 0 ) + mu_z
    exp_xnew = ut.build_zgrid(exp_x, x)
    exp_znew = ut.build_zgrid(exp_z, x)
    S = np.array([])
    new_data_svib = 0
    if bulk.entropy:
        new_data_svib = ut.build_entgrid(bulk.svib, x, ynew)            

    for k in range(0, nphases):
        normalised_bulk = normalise_phase_energy(data[k],
                                                  bulk)

        SE = calculate_bulk_energy(xnew, ynew, 
                                   x_energy,
                                   y_energy, znew,
                                   data[k],
                                   bulk,
                                   normalised_bulk,
                                   exp_xnew, exp_znew, new_data_svib, new_data_svib)

        S = np.append(S, SE)

    phase_data, SE = ut.get_phase_data(S, nphases)
    return phase_data, SE

def calculate(data, bulk, deltaX, deltaY, x_energy, y_energy, mu_z, exp_x, exp_y):
    """Description needed

    Parameters
    ----------
    data : (:py:attr:`list`):
        List containing the (:py:class:`surfinpy.data.DataSet`): objects for each phase
    bulk : (:py:class:`surfinpy.data.ReferenceDataSet`):
        Reference dataset
    x : (:py:attr:`dict`):
        X axis chemical potential values
    y : (:py:attr:`dict`):
        Y axis chemical potential values
    nphases : (:py:attr:`int`):
        Number of phases
    x_energy : (:py:attr:`float`):
        DFT 0K energy for species x
    y_energy : (:py:attr:`float`):
        DFT 0K energy for species y
    mu_z :  (:py:attr:`float`):
        Description Needed
    exp_x : (:py:attr:`float`):
        Description Needed
    exp_y : (:py:attr:`float`):
        Description Needed

    Returns
    -------
    system : type
        Description Needed
    """
    nphases = len(data)

    X = np.arange(deltaX['Range'][0], deltaX['Range'][1],
                  0.025, dtype="float")
    Y = np.arange(deltaY['Range'][0], deltaY['Range'][1],
                  0.01, dtype="float")

    phases, SE = evaluate_phases(data, bulk, X, Y,
                                 nphases, x_energy,
                                 y_energy, mu_z,
                                 exp_x, exp_y,
                                 )
    ticks = np.unique([phases])
    colors = ut.list_colors(data, ticks)
    phases = ut.transform_numbers(phases, ticks)
    Z = np.reshape(phases, (Y.size, X.size))
    SE = np.reshape(SE, (Y.size, X.size))
    labels = ut.get_labels(ticks, data)
    system = plotting.MuTPlot(X,
                             Y,
                             Z,
                             labels,
                             ticks,
                             colors,
                             deltaX['Label'],
                             deltaY['Label'])

    return system
