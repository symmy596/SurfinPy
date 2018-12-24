import numpy as np


def build_xgrid(x, y):
    xnew = np.tile(x, y.size)
    xnew = np.reshape(xnew, (y.size, x.size))
    return xnew

def build_ygrid(x, y):
    ynew = np.tile(y, x.size)
    ynew = np.split(ynew, x.size)
    ynew = np.column_stack(ynew)
    return ynew

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
        coverage = np.append(coverage, (((data[i]['Y'] / (
            data[i]['Area'] / 100)) / 2) * 10**18))
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
        label = data[val]['Label']
        labels.append(label)
    return labels


def transform_numbers(Z, ticks):
    ''' transform numbers - Takes the phase diagram array and converts
    the numbers to numbers scaled 0, 1, 2, etc in order to make plotting easier
    
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


def fit(thermochem, T):
    '''Fit a polynominal function to thermochemical data from NIST_JANAF

    Parameters
    ----------
    thermochem : array like
        NIST_JANAF thermochemical table in numpy array format
    T : array like
        full temperature range

    Returns
    -------
    shift : array like
        Entropy of adsorption species shifted to temeperature T
    '''
    thermochem =  np.delete(thermochem, (0), axis=0)
    z = np.polyfit(thermochem[:, 0], thermochem[:, 2], 3)
    f = np.poly1d(z)
    shift = f(T)
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
    return x


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


def calculate_gibbs(data):
    '''Calculate the gibbs free energy from thermochemcial data
    obtained from the NIST_JANAF database

    Parameters
    ----------
    data : array like
        Full file downloaded from NIST_JANAF database

    Returns
    -------
    data : dictionary
        gibbs energy as a function of temperature
    '''
    #There may be a bug here - deltas is column 2?
    temperature = data[:, 0]
    deltas = data[:, 1]
    H = data[:, 5]
    DeltaS = (deltas * 0.01036) / 1000
    H = H + H[0]
    H_HT = H * 0.01036
    mu = H_HT - temperature * DeltaS
    data = {'Temperature': temperature, 'Shift': mu}
    return data
