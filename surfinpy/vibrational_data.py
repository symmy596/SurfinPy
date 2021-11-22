import yaml
import numpy as np
from surfinpy import utils as ut
from scipy.constants import codata
from scipy.constants import physical_constants

def zpe_calc(vib_prop):
    """Calculates and returns the zero point energy for the system.

    Parameters
    ----------
    vib_prop : :py:attr:`array_like`
        Vibrational Properties read from input yaml file

    Returns
    -------
    zpe : :py:attr:`float`
        Zero Point energy for the system
    """
    hc = np.multiply(physical_constants["speed of light in vacuum"][0],physical_constants["Planck constant"][0])*100
    vib_prop_1 = list(map(lambda x : x * hc, vib_prop['Frequencies']))
    vib_prop_1 = np.multiply(vib_prop_1, 0.5)
    zpe = sum(vib_prop_1)
    zpe = zpe* physical_constants["joule-electron volt relationship"][0]/ vib_prop['F-Units'] 
    
    return zpe


def entropy_calc(freq, temp, vib_prop):
    """Calculates and returns the vibrational entropy for the system.

    Parameters
    ----------
    freq : :py:attr:`array_like`
        Vibrational frequencies for system.
    temp : :py:attr:`array_like`
        Temperature range at which the vibrational entropy is calculated
    vib_prop : :py:attr:`array_like`
        Vibrational Properties read from input yaml file

    Returns
    -------
    svib : :py:attr:`array_like`
        Vibrational entropy for the system calculated using the temperature range provided.
    """
    hc = np.multiply(physical_constants["speed of light in vacuum"][0],physical_constants["Planck constant"][0])*100 #constant
    k =  physical_constants["Boltzmann constant"][0]
    R=physical_constants["molar gas constant"][0]
    jtoev = np.multiply(physical_constants["electron volt-joule relationship"][0],physical_constants["Avogadro constant"][0])
    np.seterr(over='ignore')
    np.seterr(divide='ignore', invalid='ignore')

    Theta = np.multiply(freq,hc)
    Theta = np.divide(Theta, k)
    
    u = np.divide(np.multiply(Theta, R),(np.exp(np.divide(Theta, temp), dtype=np.float64)-1))
    uvib = np.sum(u, axis=1)
    uvib = uvib/vib_prop['F-Units']

    a = np.multiply(np.multiply(temp,R),np.log(np.subtract(1,np.exp(np.divide(np.negative(Theta),temp)))))
    avib = np.sum(a, axis=1)
    avib = avib/vib_prop['F-Units']
    avib = np.divide(avib,jtoev) #constant
    
    s = np.divide(np.subtract(u,a), temp)
    svib = np.sum(s, axis=1, dtype=np.float64)
    svib = svib/vib_prop['F-Units']
    svib = np.divide(svib,jtoev) #constant
    svib = np.nan_to_num(svib)
    return svib, avib

def vib_calc(vib_file, temp_r):
    """Calculates and returns the Zero Point Energy (ZPE) and vibrational entropy for the temperature range provided. 
    
    Parameters
    ----------
    vib_file : :py:attr:`str`):
        yaml file containing vibrational frequencies
    temp_r : :py:attr:`array_like`
        Temperature range at which the vibrational entropy is calculated

    Returns
    -------
    zpe : :py:attr:`float`
        Zero Point energy for the system
    svib : :py:attr:`array_like`
        Vibrational entropy for the system calculated using the temperature range provided.
    """
    vib_prop = ut.read_vibdata(vib_file)
    new_temp = ut.build_tempgrid(temp_r, vib_prop['Frequencies']) 
    freq = ut.build_freqgrid(vib_prop['Frequencies'], temp_r) 
    zpe = 0
    zpe = zpe_calc(vib_prop)
    svib, avib = entropy_calc(freq, new_temp, vib_prop)
    return zpe, svib, avib

def recalculate_vib(dataset, bulk):
    if bulk.entropy:
        bulk.temp_r = np.arange(bulk.temp_range[0],
                                bulk.temp_range[1], 
                                0.01, dtype="float")
        bulk.svib = vib_calc(bulk.file, bulk.temp_r)[1]
        bulk.avib = vib_calc(bulk.file, bulk.temp_r)[2]
        bulk.temperature = bulk.temp_r[0]
    if bulk.zpe:
        bulk.temp_r = np.arange(bulk.temp_range[0],
                                bulk.temp_range[1], 
                                0.01, dtype="float")
        bulk.zpe = vib_calc(bulk.file, bulk.temp_r)[0]
        bulk.temperature = bulk.temp_r[0]

    for phase in dataset:
        if phase.entropy:
            phase.temp_r = np.arange(phase.temp_range[0],
                                    phase.temp_range[1], 
                                    0.01, dtype="float")
            phase.svib = vib_calc(phase.file, phase.temp_r)[1]
            phase.avib = vib_calc(phase.file, phase.temp_r)[2]
            phase.temperature = phase.temp_r[0]

        if phase.zpe:
            phase.temp_r = np.arange(phase.temp_range[0],
                                    phase.temp_range[1], 
                                    0.01, dtype="float")
            phase.zpe = vib_calc(phase.file, phase.temp_r)[0]
            phase.temperature = phase.temp_r[0]