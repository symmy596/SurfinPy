import numpy as np

from surfinpy import phaseplot
from pylab import *
from scipy.constants import codata

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

def get_labels(ticks, data):
    '''Accesses and returns the labels that correspond to the phases displayed on the phase diagram
       Parameters
       ----------
            ticks : list, Phases that are displayed
            data  : list of dictionaries
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

def pressure(X, T):
    ''' pressure - Calculate the pressure for chemical potential values
        Parameters
        ----------
            X : numpy array - delta mu values
            T : int - temperature
        Returns
        -------
            pressure : numpy array - pressure values
    '''
    # to do 
    # add to utils
    k = codata.value('Boltzmann constant in eV/K')
    pressure = X / (k * T * 2.203)

    return pressure

def constants(data, bulk):
    '''constants - calculate the surface energy irrespective of chemical potential
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
    # to do 
    # get rid of this
    return X * Xscale

def calculate_surface_energy(Uo, Uh, yshiftval, xshiftval, Hexcess, Oexcess, B):
    ''' This function calculates the surface for a given chemical potential of
    oxygen and hydrogen
    Parameters
    ----------
    Uo : 
        Chemical potential of Oxygen
    Ho : 
        Chemical potential of Hydrogen
    yshiftval : 
        shift value for y axis
    xshiftval : 
        shift value for x axis
    Hexcess : 
        Excess Y
    Oexcess : 
        Excess X
    Returns
    -------
    SE  : Surface Energy
    '''
    yshiftval = scale(yshiftval, Hexcess)
    xshiftval = scale(xshiftval, Oexcess)
    C = scale(Oexcess, Uo)
    D = scale(Hexcess, Uh)
    SE = B - C - D - yshiftval - xshiftval

    return SE

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
     # to do 
     # rename this function
     # use the new vectorize stuff in utils
    Xnew = np.tile(X, Y.size)
    Xnew = np.reshape(Xnew, (Y.size, X.size))
    Ynew = np.tile(Y, X.size)
    Ynew = np.split(Ynew, X.size)
    Ynew = np.column_stack(Ynew)

    S = np.array([])
    for k in range(0, nsurfaces):
        Hexcess, Oexcess, B = constants(data[k], bulk)
        SE = calculate_surface_energy(Xnew, Ynew, yshiftval, xshiftval, Hexcess, Oexcess, B)
        S = np.append(S, SE)
    SE_array = get_phase_data(S, nsurfaces)
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
    # to do 
    # fix plots
    data = sorted(data, key=lambda k: (k['Y']))
    nsurfaces = len(data)
    X = np.arange(deltaX['Range'][0], deltaX['Range'][1], 0.025, dtype="float")
    Y = np.arange(deltaY['Range'][0], deltaY['Range'][1], 0.025, dtype="float")
    X = X - xshiftval
    Y = Y - yshiftval
    SE_array = surface_energy_array(data, bulk, X, Y, nsurfaces, xshiftval, yshiftval)
    ticks = np.unique([SE_array])
    SE_array = transform_numbers(SE_array, ticks)
    Z = np.reshape(SE_array, (Y.size, X.size))
    labels = get_labels(ticks, data)          
    if xshiftval == 0 and yshiftval == 0:
        phaseplot.plot_phase(X, Y, Z, ticks, labels, deltaX['Label'],
                             deltaY['Label'], temperature, output)
    elif convert_pressure == False:
        phaseplot.plot_phase(X, Y, Z, ticks, labels, deltaX['Label'], 
                             deltaY['Label'], temperature, output)
    elif convert_pressure == True:
        p1 = pressure(X, temperature)
        p2 = pressure(Y, temperature)
        phaseplot.plot_mu_p(X, Y, Z, p1, p2, ticks, labels, deltaX['Label'], deltaY['Label'], temperature, output)
        phaseplot.plot_pressure(p1, p2, Z, ticks, labels, deltaX['Label'], deltaY['Label'], temperature, output="pressure.png")
