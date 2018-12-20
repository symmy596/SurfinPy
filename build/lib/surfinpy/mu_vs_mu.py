import numpy as np
from scipy.constants import codata
from surfinpy import phaseplot
from surfinpy import utils as ut


def pressure(chemical_potential, t):
    r"""Converts a given chemical potential at a specific 
    temperature (T) to a pressure value.
    .. math::
        P = \frac{&mu}{k * T}

    Parameters
    ----------
    chemical_potential : array like
        delta mu values
    t : int
        temperature

    Returns
    -------
    pressure : array like
        pressure values
    """
    k = codata.value('Boltzmann constant in eV/K')
    pressure = X / (k * T * 2.203)

    return pressure

def calculate_excess(adsorbant, slab_cations, area, bulk, nspecies=1, check=False):
    if check is True and nspecies == 1:   
        return ((adsorbant - ((bulk['O'] / bulk['M']) * slab_cations)) / (2 * area))
    else:
        return (adsorbant / (area * 2))


def calculate_normalisation(slab_energy, slab_cations, bulk, area):
    return ((slab_energy - (slab_cations / bulk['M']) * (bulk['Energy'] / bulk['F-Units'])) / (2 * area))


def constants(data, bulk):
    '''***** NOW DEPRACATED ******
    Calculates and returns the constants used in the calculation
    of 

    Parameters
    ----------
    data : list of dictionaries containg info on each surface
    bulk : bulk dictionary

    Returns
    -------
    Hexcess : Excess for the Y species
    Oexcess : Excess for the X species
    '''
    Hexcess = data['Y'] / (data['Area'] * 2)
    Oexcess = (data['X'] - ((bulk['O'] / bulk['M']) * data['M'])) / (2 * data['Area'])
    B = (data['Energy'] - (data['M'] / bulk['M']) * (bulk['Energy'] / bulk['F-Units'])) / (2 * data['Area'])
    return Hexcess, Oexcess, B


def scale(X, Xscale):
    return X * Xscale


def calculate_surface_energy(deltamux, deltamuy, xshiftval, yshiftval,
                             xexcess, yexcess, normalised_bulk):
    ''' This function calculates the surface for a given chemical potential of
    oxygen and hydrogen

    Parameters
    ----------
    Uo : array like
    Chemical potential of Oxygen
    Ho : array like
    Chemical potential of Hydrogen
    yshiftval : float
    shift value for y axis
    xshiftval : float
    shift value for x axis
    Hexcess : float
    Excess Y
    Oexcess : float
    Excess X

    Returns
    -------
    SE  : Surface Energy
    '''
    return (normalised_bulk - (deltamux * xexcess) - (deltamuy * yexcess) - (xshiftval * xexcess) - (yshiftval * yexcess))


def surface_energy_array(data, bulk, X, Y, nsurfaces, xshiftval, yshiftval):
    ''' This function calculates and returns a 2D numpy array of surface energes
    for a range of chemical potential values

    Parameters
    ----------
    data : list
        List containing the dictionary data for each phase
    bulk : dictionary
        dictionary containing data for bulk
    X : dictionary
        X axis chemical potential values
    Y : dictionary
        Y axis chemical potential values
    nsurfaces : int
        Number of phases
    xshiftval : float
        shift value for x axis
    yshiftval : float
        shift value for y axis

    Returns
    -------
    SE_array  : array like
        array of surface energies matching chemcial potential values
     '''
    Xnew = np.tile(X, Y.size)
    Xnew = np.reshape(Xnew, (Y.size, X.size))
    Ynew = np.tile(Y, X.size)
    Ynew = np.split(Ynew, X.size)
    Ynew = np.column_stack(Ynew)
    S = np.array([])
    for k in range(0, nsurfaces):
        xexcess = calculate_excess(data[k]['X'], data[k]['M'], data[k]['Area'], bulk,  data[k]['nSpecies'], check=True)
        yexcess = calculate_excess(data[k]['Y'], data[k]['M'], data[k]['Area'], bulk)
        normalised_bulk = calculate_normalisation(data[k]['Energy'], data[k]['M'], bulk, data[k]['Area'])
        Hexcess, Oexcess, B = constants(data[k], bulk)
        SE = calculate_surface_energy(Xnew, Ynew,
                                      xshiftval,
                                      yshiftval,
                                      xexcess,
                                      yexcess,
                                      normalised_bulk)
        S = np.append(S, SE)
    SE_array = ut.get_phase_data(S, nsurfaces)
    return SE_array


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
    None
    '''
    data = sorted(data, key=lambda k: (k['Y']))
    nsurfaces = len(data)
    X = np.arange(deltaX['Range'][0], deltaX['Range'][1], 0.025, dtype="float")
    Y = np.arange(deltaY['Range'][0], deltaY['Range'][1], 0.025, dtype="float")
    X = X - xshiftval
    Y = Y - yshiftval
    phases = surface_energy_array(data, bulk, X, Y,
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
