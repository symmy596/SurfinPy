import numpy as np

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
    temperature = data[:,0]
    deltas = data[:,1]
    H = data[:,5]

    DeltaS = (deltas * 0.01036) / 1000
    H = H + H[0]
    H_HT = H * 0.01036
    mu = H_HT - temperature * DeltaS
    data = {'Temperature': temperature, 'Shift': mu}
    return data