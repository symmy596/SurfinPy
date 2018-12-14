import numpy as np

from surfinpy import phaseplot
from surfinpy import p_vs_t
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
    SE = np.split(S, nsurfaces)
    SE = np.column_stack(SE)
    print(SE.shape, SE[:,0].size)
    S = np.amin(SE, axis=1)
    return S

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
    B = (data['Energy'] - (data['M'] / bulk['M']) * (bulk['Energy'] / bulk['F-Units'])) / (2 * data['Area'])
    
    return Hexcess, B

def scale(X, Xscale):
    
    return X * Xscale

def calculate_surface_energy(chemical_potential, adsorbant, Hexcess, B):
    ''' This function calculates the surface for a given chemical potential of
        oxygen and hydrogen
        Parameters
        ----------
            Uo   : Chemical potential of Oxygen
            Ho   : Chemical potential of Hydrogen
            yshiftval : shift value for y axis
            xshiftval : shift value for x axis
            Hexcess : Excess Y
            Oexcess : Excess X
            Returns
        -------
            SE  : Surface Energy
    '''
    #xshiftval = scale(adsorbant, Hexcess)
    D = scale(Hexcess, chemical_potential)
    SE = B - D #- xshiftval

    return SE

def surface_energy_array(data, bulk, chemical_potential, nsurfaces, adsorbant):
    ''' This function calculates and returns a 2D numpy array of surface energes
        for a range of chemical potential values
        Parameters
        ----------
            data      : List containing the dictionary data for each phase
            bulk      : dictionary containing data for bulk
            O         : X axis chemical potential values
            H         : Y axis chemical potential values
            nsurfaces : Number of phases
            xshiftval : shift value for x axis
            yshiftval : shift value for y axis
        Returns
        -------
            SE_array  : array of surface energies matching chemcial potential values
     '''

    S = np.array([])
    for k in range(0, nsurfaces):
        Hexcess, B = constants(data[k], bulk)
        SE = calculate_surface_energy(chemical_potential, adsorbant, Hexcess, B)
        S = np.append(S, SE)

    SE_array = get_phase_data(S, nsurfaces)

    return SE_array

def calculate(data, bulk, deltaY, adsorbant_dft, thermochem, output=None):
    '''Function that runs the calcualtion
       Parameters
       ----------
        data      : List containing the dictionary data for each phase
        bulk      : dictionary containing data for bulk
        O         : X axis chemical potential values
        H         : Y axis chemical potential values
        nsurfaces : Number of phases
    '''

    if output is None:
        output = "Phase.png"
    
    X = np.arange(deltaY['Range'][0], deltaY['Range'][1], 0.025, dtype="float")
    T = np.arange(2, 1002)

    shift = p_vs_t.fit(thermochem, T)
    shift = (T * (shift / 1000)) / 96.485
    adsorbant = adsorbant_dft - shift
    

    nsurfaces = len(data)

    SE_array = surface_energy_array(data, bulk, X, nsurfaces, adsorbant_dft)

    return SE_array, X, T
