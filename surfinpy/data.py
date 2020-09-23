import numpy as np
from surfinpy import vibrational_data as vd

class ReferenceDataSet():
    """Object that contains information about the reference DFT calculation
    to be used in the phase diagram calculation. This object is
    used in both the surface and bulk phase diagram methods.

    Parameters
    ----------
    cation : :py:attr:`int`
        Number of cations in reference dataset
    anion :  :py:attr:`int`
        Number of anions in reference dataset
    energy : :py:attr:`float`
        DFT evaluated energy of reference dataset
    funits : :py:attr:`int`
        Number of formula units in reference dataset
    color : :py:attr:`string`
        Desired color of this phase in the phase diagram
    file : :py:attr:`str`):
        yaml file containing vibrational frequencies
    entropy : :py:attr:`bool`
        Is entropy to be considered?
    temp_range : :py:attr:`list`
        Temperature range to calculate vibrational entropy across
    zpe : :py:attr:`bool`
        Is the zero point energy to be considered?
    """
    def __init__(self, cation, anion, energy, funits, color=None,
                 file=None, entropy=False, temp_range=None,
                 zpe=False):
        self.cation = cation
        self.anion = anion
        self.energy = energy
        self.funits = funits
        self.file = file
        self.color = color
        self.entropy = entropy
        self.temp_range = temp_range
        self.zpe = 0
        self.svib = 0
        self.temperature = 0
        self.zpe = zpe
        if self.entropy:
            self.temp_r = np.arange(self.temp_range[0],
                                    self.temp_range[1], 
                                    1, dtype="float")
            self.svib = vd.vib_calc(self.file, self.temp_r)[1]
            self.temperature = self.temp_r[0]

        if self.zpe:
            self.temp_r = np.arange(self.temp_range[0],
                                    self.temp_range[1], 
                                    1, dtype="float")
            self.zpe = vd.vib_calc(self.file, self.temp_r)[0]
            self.temperature = self.temp_r[0]

class DataSet():
    """Object that contains information about a DFT calculation
    to be added to the phase diagram calculation. This object is
    used in both the surface and bulk phase diagram methods.

    Parameters
    ----------
    cation : :py:attr:`int`
        Number of cations in dataset
    x :  :py:attr:`int`
        Number of species x in dataset
    y :  :py:attr:`int`
        Number of species y in dataset
    energy : :py:attr:`float`
        DFT evaluated energy of reference dataset
    label : :py:attr:`str`
        Label of dataset to be used in phase diagram
    color : :py:attr:`string`
        Desired color of this phase in the phase diagram
    funits : :py:attr:`int`
        Number of formula units in dataset
    file : :py:attr:`str`
        yaml file containing vibrational frequencies
    area : :py:attr:`float`
        Surface area - required for surface calculations
    nspecies : :py:attr:`int`
        Number of species that are constituent parts of the surface.
    entropy : :py:attr:`bool`
        Is entropy to be considered?
    temp_range : :py:attr:`list`
        Temperature range to calculate vibrational entropy across
    zpe : :py:attr:`bool`
        Is the zero point energy to be considered?
    """
    def __init__(self, cation, x, y, energy, label, color=None, funits=0, 
                 file=None, area=None, nspecies=None, entropy=False,
                 temp_range=False, zpe=False):
        self.cation = cation
        self.x = x
        self.y = y
        self.energy = energy
        self.label= label
        self.color = color
        self.funits = funits
        self.file = file 
        self.area = area
        self.nspecies = nspecies
        self.entropy = entropy
        self.temp_range = temp_range
        self.zpe = 0
        self.svib = 0
        self.temperature = 0
        if self.entropy:
            self.temp_r = np.arange(self.temp_range[0],
                                    self.temp_range[1], 
                                    1, dtype="float")
            self.svib = vd.vib_calc(self.file, self.temp_r)[1]
            self.temperature = self.temp_r[0]

        if self.zpe:
            self.temp_r = np.arange(self.temp_range[0],
                                    self.temp_range[1], 
                                    1, dtype="float")
            self.zpe = vd.vib_calc(self.file, self.temp_r)[0]
            self.temperature = self.temp_r[0]