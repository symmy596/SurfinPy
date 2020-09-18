import numpy as np
from surfinpy import chemical_potential_plot
from surfinpy import utils as ut
from surfinpy import vibrational_data as vd
from scipy.interpolate import CubicSpline
import sys

def normalise_phase_energy(phase, bulk):
    r"""
    Description Needed

    Parameters
    ----------
    phase :  type
        Description Needed
    bulk :  type
        Description Needed

    Returns
    -------
    float:
        Normalised phase energy
    """
    return ((phase.energy + (phase.zpe * phase.funits) - phase.temperature * phase.svib * phase.funits) - (phase.cation / bulk.cation)
            * ((bulk.energy / bulk.funits) - phase.temperature * phase.svib))

def calculate_bulk_energy(deltamux, deltamuy, x_energy, y_energy,
                             phase, normalised_bulk):
    r"""Description Needed

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
    phase : surfinpy.data.DataSet object
        Calculation 
    normalised_bulk : float
        bulk energy normalised to the bulk value.

    Returns
    -------
    array like:
        2D array of free energies as a function of
        chemical potential of x and y
    """

    return (
        normalised_bulk - deltamux* phase.x - deltamuy* phase.y - (
        x_energy * phase.x) - (y_energy * phase.y))

def evaluate_phases(data, bulk, x, y, nphases, x_energy, y_energy, 
                    Entropy_true=False, ZPE_true=False, temp_range=0, 
                    temperature = 0):
    """Calculates the free energies of each phase as a function of chemical
    potential of x and y. Then uses this data to evaluate which phase is most
    stable at that x/y chemical potential cross section.

    Parameters
    ----------
    data : list
        list of surfinpy.data.DataSet objects
    bulk : surfinpy.data.ReferenceDataSet object
        bulk
    x : dictionary
        X axis chemical potential values
    y : dictionary
        Y axis chemical potential values
    nphases : int
        Number of phases
    x_energy : float
        DFT 0K energy for species x
    y_energy : float
        DFT 0K energy for species y
    Entropy_true : bool
        Description Needed
    ZPE_true : bool
        Description Needed
    temp_range : int
        Description Needed
    temperature : int
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

def calculate(data, bulk, deltaX, deltaY, x_energy, y_energy, Entropy_true=False, ZPE_true=False, temp_range=0,
              temperature=0):
    """Initialise the surface energy calculation.

    Parameters
    ----------
    data : list
        List of surfinpy.data.DataSet object for each phase
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
    nphases = len(data)
    X = np.arange(deltaX['Range'][0], deltaX['Range'][1],
                  0.005, dtype="float")
    Y = np.arange(deltaY['Range'][0], deltaY['Range'][1],
                  0.005, dtype="float")  

    phases, SE = evaluate_phases(data, bulk, X, Y,
                                 nphases, x_energy, y_energy, 
                                 Entropy_true, ZPE_true, temp_range, 
                                 temperature)

    ticks = np.unique([phases])
    phases = ut.transform_numbers(phases, ticks)
    Z = np.reshape(phases, (Y.size, X.size))
    SE = np.reshape(SE, (Y.size, X.size))
    labels = ut.get_labels(ticks, data)
    system = chemical_potential_plot.ChemicalPotentialPlot(X,
                                                           Y,
                                                           Z,
                                                           labels,
                                                           ticks,
                                                           deltaX['Label'],
                                                           deltaY['Label'])
    return system
