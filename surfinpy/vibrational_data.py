import yaml
import numpy as np
from surfinpy import utils as ut
from scipy.constants import codata

#Use scipy.constants for all constants

def zpe_calc(vib_prop):
    """Description

    Parameters
    ----------
    vib_prop : type
        description

    Returns
    -------
    zpe :
        description
    """
    hc = 9.93247898996E-24 #constant
    vib_prop_1 = list(map(lambda x : x * hc, vib_prop['Frequencies']))
    zpe = sum(vib_prop_1)
    zpe = zpe / 1.6021E-19 / vib_prop['F-Units'] #constant
    return zpe

#Is avid needed?
def entropy_calc(freq, temp, vib_prop):
    """Description

    Parameters
    ----------
    freq : type
        description
    temp : type
        description
    vib_prop : type
        description

    Returns
    -------
    svib :
        description
    """
    hc = 1.99E-25 *100.0E0 #constant
    k = 1.38064852E-23#constant
    R=8.314#constant
    np.seterr(over='ignore')

    Theta = np.multiply(freq,hc)
    Theta = np.divide(Theta, k)

    u = np.multiply(Theta, R)/(np.exp(np.divide(Theta, temp), dtype=np.float64)-1)
    uvib = np.sum(u, axis=1)
    uvib = uvib/vib_prop['F-Units']

    a = np.multiply(Theta, R)*np.log(1-np.exp(np.negative(np.divide(Theta, temp)), dtype=np.float64))
    avib = np.sum(a, axis=1)
    avid = avib/vib_prop['F-Units']

    s = np.divide(np.subtract(u,a), temp)
    svib = np.sum(s, axis=1, dtype=np.float64)
    svib = svib/vib_prop['F-Units']
    svib = np.divide(svib,96485) #constant
    
    return svib

def vib_calc(vib_file, temp_r):
    """Description Needed

    Parameters
    ----------
    vib_file : type
        description
    temp_r : type
        description
    zpe_true : type
        description
    ent_true : type
        description

    Returns
    -------
    zpe :
        description
    svib : 
        description
    """
    vib_prop = ut.read_vibdata(vib_file)
    new_temp = ut.build_tempgrid(temp_r, vib_prop['Frequencies']) 
    freq = ut.build_freqgrid(vib_prop['Frequencies'], temp_r) 
    zpe = 0
    zpe = zpe_calc(vib_prop)
    svib = entropy_calc(freq, new_temp, vib_prop)
    return zpe, svib

def recalculate_vib(dataset, bulk):
    if bulk.entropy:
        bulk.temp_r = np.arange(bulk.temp_range[0],
                                bulk.temp_range[1], 
                                0.01, dtype="float")
        bulk.svib = vib_calc(bulk.file, bulk.temp_r)[1]
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
            phase.temperature = phase.temp_r[0]

        if phase.zpe:
            phase.temp_r = np.arange(phase.temp_range[0],
                                    phase.temp_range[1], 
                                    0.01, dtype="float")
            phase.zpe = vib_calc(phase.file, phase.temp_r)[0]
            phase.temperature = phase.temp_r[0]