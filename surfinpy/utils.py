import yaml
import numpy as np
from scipy.constants import codata
from scipy.interpolate import CubicSpline

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


def build_xgrid(x, y):
    """Builds a 2D grip of values for the x axis.

    Parameters
    ----------
    x : array like
        numpy array
    y : array like
        numpy array

    Returns
    -------
    xnew : array like
        numpy array
    """
    xnew = np.tile(x, y.size)
    xnew = np.reshape(xnew, (y.size, x.size))
    return xnew


def build_ygrid(x, y):
    """Builds a 2D grip of values for the y axis.

    Parameters
    ----------
    x : array like
        numpy array
    y : array like
        numpy array

    Returns
    -------
    xnew : array like
        numpy array
    """
    ynew = np.tile(y, x.size)
    ynew = np.split(ynew, x.size)
    ynew = np.column_stack(ynew)
    return ynew

def build_zgrid(z, y):
    """Builds a 2D grip of values for the x axis.

    Parameters
    ----------
    x : array like
        numpy array
    y : array like
        numpy array

    Returns
    -------
    xnew : array like
        numpy array
    """
    znews = np.tile(z, y.size)
    znews = np.reshape(znews, (z.size, y.size), order='F')
    return znews

def build_entgrid(z, y, ynew):
    znews = np.tile(z, len(y))
    znews = np.reshape(znews, (len(z), len(y)), order='F')
    temp_ent = np.multiply(znews, ynew)
    return temp_ent

def build_freqgrid(z, y):
    """Builds a 2D grip of values for the x axis.

    Parameters
    ----------
    x : array like
        numpy array
    y : array like
        numpy array

    Returns
    -------
    xnew : array like
        numpy array
    """
    znews = np.tile(z, (len(y),1))
    return znews
    
def build_tempgrid(z, y):
    """Builds a 2D grip of values for the x axis.

    Parameters
    ----------
    x : array like
        numpy array
    y : array like
        numpy array

    Returns
    -------
    xnew : array like
        numpy array
    """
    znews = np.tile(z, len(y))
    znews = np.reshape(znews, (len(z), len(y)), order='F')
    return znews

def calculate_coverage(data):
    """Calcualte the coverage of the adsorbing species on each surface.

    Parameters
    ----------
    data : list
        list of dictionaries containing info on each surface calculation

    Returns
    -------
    coverage : array like
        numpy array of coverage values in units of :math:`n/nm^2`
    """
    coverage = np.array([])
    for i in range(0, len(data)):
        coverage = np.append(coverage, (((data[i].y / (
            data[i].area / 100)) / 2) * 10**18))
    return coverage


def get_labels(ticks, data):
    '''Reads the phase diagram data and returns the labels that correspond
    to the phases displayed on the phase diagram.

    Parameters
    ----------
    ticks : list
        Phases that are displayed.
    data  : list
        list of dictionaries.

    Returns
    -------
    labels : list
        list of labels.
    '''
    labels = []
    for i in range(0, ticks.size):
        val = ticks[i] - 1
        val = int(val)
        label = data[val].label
        labels.append(label)
    return labels


def transform_numbers(Z, ticks):
    ''' transform numbers - Takes the phase diagram array and converts
    the numbers to numbers scaled 0, 1, 2, etc in order to make plotting
    easier

    Parameters
    ----------
    Z : array like
        array of integers
    ticks : list
        unique phases

    Returns
    -------
    Z : array like
        Normalised to a continuous set of numbers.
    '''
    y = np.arange(ticks.size)
    for i in range(0, ticks.size):
        for j in range(0, Z.size):
            if Z[j] == ticks[i]:
                Z[j] = y[i]
    return Z


def fit(x, y, t):
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
    z = CubicSpline(x, y, bc_type='clamped')
    shift = z(t)
    return shift


def get_phase_data(S, nsurfaces):
    ''' Determines which surface composition is most stable at a
    given x and y value.

    Parameters
    ----------
    S : array like
        2D array of surface energies
    nsurfaces : int
        Total number of surfaces

    Returns
    -------
    x : array like
        array of ints corresponding to the position of
        the lowest phase
    '''
    S = np.split(S, nsurfaces)
    S = np.column_stack(S)
    x = np.argmin(S, axis=1) + 1
    SE = np.amin(S, axis=1)
    return x, SE


def read_nist(File):
    '''Read a downloaded NIST_JANAF thermochemcial table

    Parameters
    ----------
    File : str
        filename of table

    Returns
    -------
    data : array_like
        table as an array
    '''
    data = np.genfromtxt(File, skip_header=2)
    return data


def calculate_gibbs(t, s, h):
    '''Calculate the gibbs free energy from thermochemcial data
    obtained from the NIST_JANAF database

    Parameters
    ----------
    t : array like
        Temperature range
    s : array like
        delta s values from nist
    h : array like
        selta h values from nist

    Returns
    -------
    g : array like
        gibbs energy as a function of temperature
    '''
    deltas = (s * 0.01036) / 1000
    deltah = h * 0.01036
    g = deltah - t * deltas
    return g


def get_levels(X):
    """Builds the levels used in the contourf plot. This is neccesary to
    ensure that each color correpsonds to a single phase.

    Parameters
    ----------
    X : array like
        2D array of ints corresponding to each phase.

    Returns
    -------
    levels : array like
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

def read_vibdata(vib_file):
    """Description Needed

    Parameters
    ----------
    vib_file : type
        descriotion needed

    Returns
    -------
    vib_prop : type
        description needed
    """
    with open(vib_file, 'r') as file:
        vib_prop = yaml.load(file)
    return vib_prop

def fit_nist(nist_file):
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
    nist_data = read_nist(nist_file)
    h0 = nist_data[0, 4]
    fitted_s = fit(nist_data[:, 0], nist_data[:, 2], np.arange(1, 3000))
    fitted_h = fit(nist_data[:, 0], nist_data[:, 4], np.arange(1, 3000))
    fitted_h = fitted_h - fitted_h[0]
    gibbs = calculate_gibbs(np.arange(1, 3000), fitted_s, fitted_h)
    return gibbs

def temperature_correction_range(nist_file, deltaY):
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
    Y = np.arange(deltaY['Range'][0], deltaY['Range'][1],
                  1, dtype="int")
    Y = Y -1
    gibbs = fit_nist(nist_file)
    return gibbs[Y]