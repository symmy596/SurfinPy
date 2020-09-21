import numpy as np
from surfinpy import plotting
from surfinpy import utils as ut
from surfinpy import vibrational_data as vd
from scipy.interpolate import CubicSpline
import sys

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
    (:py:attr:`float`):
        Normalised phase energy
    """
    return ((phase.energy + (phase.zpe * phase.funits) - phase.temperature * phase.svib * phase.funits) - (phase.cation / bulk.cation)
            * ((bulk.energy / bulk.funits) - phase.temperature * phase.svib))

def calculate_bulk_energy(deltamux, deltamuy, x_energy, y_energy,
                             phase, normalised_bulk):
    r"""Description Needed

    Parameters
    ----------
    deltamux : (:py:attr:`array_like`):
        Chemical potential of species x
    deltamuy : (:py:attr:`array_like`):
        Chemical potential of species y
    x_energy : (:py:attr:`float`):
        DFT energy or temperature corrected DFT energy
    y_energy : (:py:attr:`float`):
        DFT energy or temperature corrected DFT energy
    phase : (:py:class:`surfinpy.data.DataSet`):
        DFT calculation 
    normalised_bulk : (:py:attr:`float`):
        Bulk energy normalised to the bulk value.

    Returns
    -------
    (:py:attr:`array_like`):
        2D array of free energies as a function of
        chemical potential of x and y
    """

    return (
        normalised_bulk - deltamux* phase.x - deltamuy* phase.y - (
        x_energy * phase.x) - (y_energy * phase.y))

def evaluate_phases(data, bulk, x, y, nphases, x_energy, y_energy):
    """Calculates the free energies of each phase as a function of chemical
    potential of x and y. Then uses this data to evaluate which phase is most
    stable at that x/y chemical potential cross section.

    Parameters
    ----------
    data : (:py:attr:`list`):
        List of (:py:class:`surfinpy.data.DataSet`): objects
    bulk : (:py:class:`surfinpy.data.ReferenceDataSet`): object
        Reference dataset
    x : (:py:attr:`dict`):
        X axis chemical potential values
    y : (:py:attr:`dict`):
        Y axis chemical potential values
    nphases : (:py:attr:`int`):
        Number of phases
    x_energy : (:py:attr:`float`):
        DFT 0 K energy for species x
    y_energy : (:py:attr:`float`):
        DFT 0 K energy for species y
    Entropy_true : (:py:attr:`bool`):
        Description Needed
    ZPE_true : (:py:attr:`bool`):
        Description Needed
    temp_range : (:py:attr:`int`):
        Description Needed
    temperature : (:py:attr:`int`):
        Description Needed

    Returns
    -------
    phase_data  : array like
        array of ints, with each int corresponding to a phase.
    """
    xnew = ut.build_xgrid(x, y)
    ynew = ut.build_ygrid(x, y)
    S = np.array([])
    for k in range(0, nphases):
        normalised_bulk = normalise_phase_energy(data[k], bulk)
        SE = calculate_bulk_energy(xnew, ynew, 
                                      x_energy,
                                      y_energy,
                                      data[k],
                                      normalised_bulk)
        S = np.append(S, SE)

    phase_data, SE = ut.get_phase_data(S, nphases)
    return phase_data, SE

def calculate(data, bulk, deltaX, deltaY, x_energy, y_energy):
    """Initialise the surface energy calculation.

    Parameters
    ----------
    data : list
        List of (:py:class:`surfinpy.data.DataSet`): object for each phase
    bulk : (:py:class:`surfinpy.data.ReferenceDataSet`):
        Reference dataset
    deltaX : (:py:attr:`dict`):
        Range of chemical potential/label for species X 
    DeltaY : (:py:attr:`dict`):
        Range of chemical potential/label for species Y 
    x_energy : (:py:attr:`float`):
        DFT energy of adsorbing species
    y_energy : (:py:attr:`float`):
        DFT energy of adsorbing species

    Returns
    -------
    system : (:py:class:`surfinpy.plotting.chemical_potential`):
        Plotting object
    """
    nphases = len(data)
    X = np.arange(deltaX['Range'][0], deltaX['Range'][1],
                  0.005, dtype="float")
    Y = np.arange(deltaY['Range'][0], deltaY['Range'][1],
                  0.005, dtype="float")  

    phases, SE = evaluate_phases(data, bulk, X, Y,
                                 nphases, x_energy, y_energy)

    ticks = np.unique([phases])
    phases = ut.transform_numbers(phases, ticks)
    Z = np.reshape(phases, (Y.size, X.size))
    SE = np.reshape(SE, (Y.size, X.size))
    labels = ut.get_labels(ticks, data)
    system = plotting.ChemicalPotentialPlot(X,
                                            Y,
                                            Z,
                                            labels,
                                            ticks,
                                            deltaX['Label'],
                                            deltaY['Label'])
    return system
