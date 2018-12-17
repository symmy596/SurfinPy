import numpy as np

class System:
   '''System Information
    This class is designed to store all of the data involved in all 
    calculations. 
    Specifically this includes the DFT data for each "adsorbed" surface, the
    DFT data for the stroichiometric surface and the DFT energies for the adsorbed species. 
    '''
    def __init__(self, data, stoich, adsorbant, bulk=None, SE=None):
        self.data = data
        self.stoich = stoich 
        self.adsorbant = adsorbant
        if bulk:
            self.bulk = bulk
        if SE:
            self.SE = SE
        

def get_labels(ticks, data):
    '''Accesses and returns the labels that correspond to the phases displayed on the phase diagram
    Parameters
    ----------
    ticks : list
        Phases that are displayed
    data  : list 
        list of dictionaries
    Returns
    -------
    labels : list strings
    '''
    # to do 
    # add to utils
    labels = []
    for i in range(0, ticks.size):
        val = ticks[i] - 1
        val = int(val)
        l = data[val]['Label']
        labels.append(l)
    return labels

def transform_numbers(Z, ticks):
    ''' transform numbers - Takes the phase diagram array and converts the numbers to numbers scaled 0, 1, 2, etc in order to make plotting easier
        Parameters
        ----------
            Z : numpy array - surface stabilities
            ticks : list - unique phases appearing in above array
        Returns
        -------
            Z : numpy array - new array
    '''
    # to do 
    # add to utils
    counter = 0
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
    # to do
    # add to utils
    z = np.polyfit(thermochem[:,0], thermochem[:,1], 3)
    shift = (z[0] * (T ** 3)) + (z[1] * (T ** 2)) + (z[2] * T) + z[3]
    return shift

def get_phase_data(S, nsurfaces):
    ''' get_phase_data - Determines which surface composition is most stable
        Parameters
        ----------
            S : 1D numpy array of surface energies
            nsurfaces : int, Total number of surfaces
        Returns
        -------
            X : value
    '''
    # to do 
    # add this function to unitls and combine with find_phase
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
    temperature = data[:,0]
    deltas = data[:,1]
    H = data[:,5]

    DeltaS = (deltas * 0.01036) / 1000
    H = H + H[0]
    H_HT = H * 0.01036
    mu = H_HT - temperature * DeltaS
    data = {'Temperature': temperature, 'Shift': mu}
    return data