import yaml
import numpy as np
from scipy.constants import codata
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt 

def pressure(chemical_potential, t):
    r"""Converts chemical potential at a specific
    temperature (T) to a pressure value.

    .. math::
        P = \frac{\mu}{k * T}

    where P is the pressure, :math:`\mu` is the chemcial potential, k is the
    Boltzmann constant and T is the temperature.

    Parameters
    ----------
    chemical_potential : :py:attr:`array_like`
        delta mu values
    t : :py:attr:`int`
        temperature

    Returns
    -------
    pressure : :py:attr:`array_like`
        pressure values as a function of chemcial potential
    """
    k = codata.value('Boltzmann constant in eV/K')
    pressure = chemical_potential / (k * t * 2.203)
    return pressure

def calculate_coverage(data):
    """Calcualte the coverage of the adsorbing species on each surface.

    Parameters
    ----------
    data : :py:attr:`list`
        list of dictionaries containing info on each surface calculation

    Returns
    -------
    coverage : :py:attr:`array_like`
        Coverage values in units of :math:`n/nm^2`
    """
    coverage = np.array([])
    for i in range(0, len(data)):
        coverage = np.append(coverage, (((data[i].y / (
            data[i].area / 100)) / 2) * 10**18))
    return coverage

def build_xgrid(x, y):
    """Builds a 2D grip of values for the x axis.

    Parameters
    ----------
    x : :py:attr:`array_like`
        One dimensional numpy array representing one dimension of phase diagram
    y : :py:attr:`array_like`
        One dimensional numpy array representing one dimension of phase diagram

    Returns
    -------
    xnew : :py:attr:`array_like`
        Two dimensional numpy array required for energy calculations
    """
    xnew = np.tile(x, y.size)
    xnew = np.reshape(xnew, (y.size, x.size))
    return xnew

def build_ygrid(x, y):
    """Builds a 2D grip of values for the y axis.

    Parameters
    ----------
    x : :py:attr:`array_like`
        One dimensional numpy array representing one dimension of phase diagram
    y : :py:attr:`array_like`
        One dimensional numpy array representing one dimension of phase diagram

    Returns
    -------
    xnew : :py:attr:`array_like`
        Two dimensional numpy array required for energy calculations
    """
    ynew = np.tile(y, x.size)
    ynew = np.split(ynew, x.size)
    ynew = np.column_stack(ynew)
    return ynew

def build_zgrid(z, y):
    """Builds a 2D grip of values for the x axis.

    Parameters
    ----------
    x : :py:attr:`array_like`
        One dimensional numpy array representing one dimension of phase diagram
    y : :py:attr:`array_like`
        One dimensional numpy array representing one dimension of phase diagram

    Returns
    -------
    xnew : :py:attr:`array_like`
        Two dimensional numpy array required for energy calculations
    """
    znews = np.tile(z, y.size)
    znews = np.reshape(znews, (z.size, y.size), order='F')
    return znews

def build_entgrid(z, y, ynew):
    """Builds a 2D grip of values for the x axis.

    Parameters
    ----------
    x : :py:attr:`array_like`
        One dimensional numpy array representing one dimension of phase diagram
    y : :py:attr:`array_like`
        One dimensional numpy array representing one dimension of phase diagram

    Returns
    -------
    xnew : :py:attr:`array_like`
        Two dimensional numpy array required for energy calculations
    """
    znews = np.tile(z, len(y))
    znews = np.reshape(znews, (len(z), len(y)), order='F')
    temp_ent = np.multiply(znews, ynew)
    return temp_ent

def build_freqgrid(z, y):
    """Builds a 2D grip of values for the x axis.

    Parameters
    ----------
    x : :py:attr:`array_like`
        One dimensional numpy array representing one dimension of phase diagram
    y : :py:attr:`array_like`
        One dimensional numpy array representing one dimension of phase diagram

    Returns
    -------
    xnew : :py:attr:`array_like`
        Two dimensional numpy array required for energy calculations
    """
    znews = np.tile(z, (len(y),1))
    return znews
    
def build_tempgrid(z, y):
    """Builds a 2D grip of values for the x axis.

    Parameters
    ----------
    x : :py:attr:`array_like`
        One dimensional numpy array representing one dimension of phase diagram
    y : :py:attr:`array_like`
        One dimensional numpy array representing one dimension of phase diagram

    Returns
    -------
    xnew : :py:attr:`array_like`
        Two dimensional numpy array required for energy calculations
    """
    znews = np.tile(z, len(y))
    znews = np.reshape(znews, (len(z), len(y)), order='F')
    return znews

def read_vibdata(vib_file):
    """Reads a yaml file containing the
    vribational frequencies from a DFT calculation.

    Parameters
    ----------
    vib_file : (:py:attr:`str`):
        File name

    Returns
    -------
    vib_prop : :py:attr:`dict`
        Dictionary of vibrational freqencies.
    """
    with open(vib_file, 'r') as file:
        vib_prop = yaml.load(file)
    return vib_prop

def read_nist(File):
    '''Read a downloaded NIST_JANAF thermochemcial table

    Parameters
    ----------
    File : :py:attr:`str`
        Filename of NIST_JANAF thermochemcial table

    Returns
    -------
    data : :py:attr:`array_like`
        NIST_JANAF thermochemcial as an array
    '''
    data = np.genfromtxt(File, skip_header=2)
    return data

def cs_fit(x, y, t):
    '''Fit a polynominal function to thermochemical data from NIST_JANAF

    Parameters
    ----------
    x : :py:attr:`array_like`
        x axis for fit
    y : :py:attr:`array_like`
        y axis for fit
    t : :py:attr:`array_like`
        x axis to be fitted

    Returns
    -------
    shift : :py:attr:`array_like`
        data fitted from x and y to t
    '''
    z = CubicSpline(x, y, bc_type='clamped')
    shift = z(t)
    return shift

def poly_fit(x, y, t):
    '''Fit a polynominal function to thermochemical data from NIST_JANAF
    Parameters
    ----------
    x : array like
        x axis for fit
    y : array like
        y axis for fit
    t : array like
        x axis to be fitted
    Returns
    -------
    shift : array like
        data fitted from x and y to t
    '''
    x = np.delete(x, (0), axis=0)
    y = np.delete(y, (0), axis=0)
    z = np.polyfit(x, y, 3)
    f = np.poly1d(z)
    shift = f(t)
    return shift

def calculate_gibbs(t, s, h):
    '''Calculate the gibbs free energy from thermochemcial data
    obtained from the NIST_JANAF database

    Parameters
    ----------
    t : :py:attr:`array_like`
        Temperature range
    s : :py:attr:`array_like`
        delta s values from nist
    h : :py:attr:`array_like`
        selta h values from nist

    Returns
    -------
    g : :py:attr:`array_like`
        gibbs energy as a function of temperature
    '''
    deltas = (s * 0.01036) / 1000
    deltah = h * 0.01036
    g = deltah - t * deltas
    return g

def fit_nist(nist_file, increments=1, method='cs'):
    """Use experimental data to correct the DFT free energy of an adsorbing
    species to a specific temperature.

    Parameters
    ----------
    nist_file : :py:attr:`array_like`
        numpy array containing experiemntal data from NIST_JANAF

    Returns
    -------
    gibbs : :py:attr:`float`
        correct free energy
    """
    nist_data = read_nist(nist_file)
    h0 = nist_data[0, 4]
    if method == 'cs':
        fitted_s = cs_fit(nist_data[:, 0], nist_data[:, 2], np.arange(1, 3000, increments))
        fitted_h = cs_fit(nist_data[:, 0], nist_data[:, 4], np.arange(1, 3000, increments))
    elif method == 'poly':
        fitted_s = poly_fit(nist_data[:, 0], nist_data[:, 2], np.arange(1, 3000, increments))
        fitted_h = poly_fit(nist_data[:, 0], nist_data[:, 4], np.arange(1, 3000, increments))
    fitted_h = fitted_h + h0
    gibbs = calculate_gibbs(np.arange(1, 3000, increments), fitted_s, fitted_h)
    return gibbs

def temperature_correction_range(nist_file, deltaY):
    """Use experimental data to correct the DFT free energy of an adsorbing
    species to a specific temperature.

    Parameters
    ----------
    nist_file : :py:attr:`array_like`
        numpy array containing experiemntal data from NIST_JANAF
    temperature : :py:attr:`int`
        Temperature to correct to

    Returns
    -------
    gibbs : :py:attr:`float`
        correct free energy
    """
    x = fit_nist(nist_file, increments=0.01)
    lower = int(deltaY['Range'][0] / 0.01)
    upper = int(deltaY['Range'][1] / 0.01)
    gibbs = x[lower : upper]
    return gibbs

def get_phase_data(S, nsurfaces):
    ''' Determines which surface composition is most stable at a
    given x and y value.

    Parameters
    ----------
    S : :py:attr:`array_like`
        2D array of surface energies
    nsurfaces : :py:attr:`int`
        Total number of surfaces

    Returns
    -------
    x : :py:attr:`array_like`
        array of ints corresponding to the position of
        the lowest phase
    '''
    S = np.split(S, nsurfaces)
    S = np.column_stack(S)
    surface_energy = np.amin(S, axis=1)
    x = np.argmin(S, axis=1) + 1
    return x, surface_energy

def list_colors(phases, ticks):
    '''Reads the phase diagram data and returns the colors that correspond
    to the phases displayed on the phase diagram.

    Parameters
    ----------
    phases  : :py:attr:`list`
        list of (:py:class:`surfinpy.data.DataSet`): objects.
    ticks : :py:attr:`list`
        Phases that are displayed.

    Returns
    -------
    colors : :py:attr:`list`
        list of colors.
    '''
    colors = []
    if phases[0].color:
        for i in range(0, ticks.size):
            val = ticks[i] - 1
            val = int(val)
            colors.append(phases[val].color)
        return colors
    else:
        return None

def get_labels(ticks, data):
    '''Reads the phase diagram data and returns the labels that correspond
    to the phases displayed on the phase diagram.

    Parameters
    ----------
    ticks : :py:attr:`list`
        Phases that are displayed.
    data  : :py:attr:`list`
        list of (:py:class:`surfinpy.data.DataSet`): objects.

    Returns
    -------
    labels : :py:attr:`list`
        list of labels.
    '''
    labels = []
    for i in range(0, ticks.size):
        val = ticks[i] - 1
        val = int(val)
        label = data[val].label
        labels.append(label)
    return labels

def get_levels(X):
    """Builds the levels used in the contourf plot. This is neccesary to
    ensure that each color correpsonds to a single phase.

    Parameters
    ----------
    X : :py:attr:`array_like`
        2D array of ints corresponding to each phase.

    Returns
    -------
    levels : :py:attr:`array_like`
        numpy array of ints
    """
    a = np.amax(X) + 1
    b = np.amin(X) - 1
    levels = np.arange(b, a, 1)
    return levels

def get_ticks(X):
    """I have no idea what this does
    """
    t = np.arange(X.size)
    t = t - 0.5
    ticky = t.tolist()
    return ticky

def transform_numbers(Z, ticks):
    ''' transform numbers - Takes the phase diagram array and converts
    the numbers to numbers scaled 0, 1, 2, etc in order to make plotting
    easier

    Parameters
    ----------
    Z : :py:attr:`array_like`
        array of integers
    ticks : :py:attr:`list`
        unique phases

    Returns
    -------
    Z : :py:attr:`array_like`
        Normalised to a continuous set of numbers.
    '''
    y = np.arange(ticks.size)
    for i in range(0, ticks.size):
        for j in range(0, Z.size):
            if Z[j] == ticks[i]:
                Z[j] = y[i]
    return Z
