import numpy as np
from surfinpy import p_vs_t as pt
from surfinpy import wulff  
from surfinpy import utils as ut
from pymatgen.core.surface import SlabGenerator, generate_all_slabs, Structure, Lattice
from pymatgen.analysis.wulff import WulffShape

adsorbant = -14.22
thermochem = ut.read_nist('H2O.txt')

SE = 1.44
stoich =      {'M': 24, 'X': 48, 'Y': 0, 'Area': 60.22, 'Energy': -575.66, 'Label': 'Stoich'}
Adsorbant_1 = {'M': 24, 'X': 48, 'Y': 2, 'Area': 60.22, 'Energy': -609.23, 'Label': '1 Species'}
data = [Adsorbant_1]
Surface_100_1 = wulff.calculate_surface_energy(stoich, data, SE, adsorbant, thermochem, 298, 0)

SE = 1.06
stoich =      {'M': 24, 'X': 48, 'Y': 0, 'Area': 85.12, 'Energy': -672.95, 'Label': 'Stoich'}
Adsorbant_1 = {'M': 24, 'X': 48, 'Y': 2, 'Area': 85.12, 'Energy': -705.0, 'Label': '1 Species'}
data = [Adsorbant_1]
Surface_110_1 = wulff.calculate_surface_energy(stoich, data, SE, adsorbant, thermochem, 298, 0)

SE = 0.76
stoich =      {'M': 24, 'X': 48, 'Y': 0, 'Area': 77.14, 'Energy': -579.61, 'Label': 'Stoich'}
Adsorbant_1 = {'M': 24, 'X': 48, 'Y': 2, 'Area': 77.14, 'Energy': -609.24, 'Label': '1 Species'}
data = [Adsorbant_1]
Surface_111_1 = wulff.calculate_surface_energy(stoich, data, SE, adsorbant, thermochem, 298, 0)

#Declare the lattic paramter
lattice = Lattice.cubic(5.411)
ceo = Structure(lattice,["Ce", "O"],
               [[0,0,0], [0.25,0.25,0.25]])
surface_energies_ceo = {(1,1,1): np.amin(Surface_111_1), (1,1,0): np.amin(Surface_110_1), (1,0,0): np.amin(Surface_100_1)}

miller_list = surface_energies_ceo.keys()
e_surf_list = surface_energies_ceo.values()

# We can now construct a Wulff shape with an accuracy up to a max Miller index of 3
wulffshape = WulffShape(ceo.lattice, miller_list, e_surf_list)

# Let's get some useful information from our wulffshape object
print("shape factor: %.3f, anisotropy: \
%.3f, weighted surface energy: %.3f J/m^2" %(wulffshape.shape_factor, 
                                       wulffshape.anisotropy,
                                       wulffshape.weighted_surface_energy))


# If we want to see what our Wulff shape looks like
wulffshape.show(color_set="RdBu", direction=(1.00, 0.25, 0.25))