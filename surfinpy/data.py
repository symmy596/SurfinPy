import numpy as np
from surfinpy import vibrational_data as vd

class ReferenceDataSet():
    """Description Needed

    Parameters
    ----------
    cation : type
        Description Needed
    anion :  type
        Description Needed
    energy : type
        Description Needed
    funits : type
        Description Needed
    file : type
        Description Needed
    entropy : type
        Description Needed
    temp_range : type
        Description Needed
    zpe : type
        Description Needed
    """
    def __init__(self, cation, anion, energy, funits, file=None,
                 entropy=False, temp_range=None, zpe=False):
        self.cation = cation
        self.anion = anion
        self.energy = energy
        self.funits = funits
        self.file = file
        self.entropy = entropy
        self.temp_range = temp_range
        self.zpe = 0
        self.svib = 0
        self.temperature = 0
        self.zpe = zpe
        if self.entropy:
            self.temp_r = np.arange(self.temp_range[0],
                                    self.temp_range[1], 
                                    1, dtype="int")
            self.svib = vd.vib_calc(self.file, self.temp_r)[1]
            self.temperature = self.temp_r[0]

        if self.zpe:
            self.temp_r = np.arange(self.temp_range[0],
                                    self.temp_range[1], 
                                    1, dtype="int")
            self.zpe = vd.vib_calc(self.file, self.temp_r)[0]
            self.temperature = self.temp_r[0]

class DataSet():
    """Description Needed

    Parameters
    ----------
    cation : type
        Description Needed
    x :  type
        Description Needed
    y : type
        Description Needed
    energy : type
        Description Needed
    label : type
        Description Needed
    funits : type
        Description Needed
    file : type
        Description Needed
    area : type
        Description Needed
    nspecies : type
        Description Needed
    entropy : type
        Description Needed
    temp_range : type
        Description Needed
    """
    def __init__(self, cation, x, y, energy, label, funits=0, 
                 file=None, area=None, nspecies=None, entropy=False,
                 temp_range=False, zpe=False):
        self.cation = cation
        self.x = x
        self.y = y
        self.energy = energy
        self.label= label
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
                                    1, dtype="int")
            self.svib = vd.vib_calc(self.file, self.temp_r)[1]
            self.temperature = self.temp_r[0]

        if self.zpe:
            self.temp_r = np.arange(self.temp_range[0],
                                    self.temp_range[1], 
                                    1, dtype="int")
            self.zpe = vd.vib_calc(self.file, self.temp_r)[0]
            self.temperature = self.temp_r[0]