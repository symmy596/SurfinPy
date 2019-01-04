from surfinpy import utils as ut
from surfinpy import p_vs_t

adsorbant = -14.00
SE = 1.40

stoich = {'Cation': 24, 'X': 48, 'Y': 0, 'Area': 60.22, 'Energy': -575.00, 'Label': 'Bare'}
H2O =    {'Cation': 24, 'X': 48, 'Y': 2, 'Area': 60.22, 'Energy': -605.00, 'Label': '1 Water'}
H2O_2 =  {'Cation': 24, 'X': 48, 'Y': 8, 'Area': 60.22, 'Energy': -695.00, 'Label': '2 Water'}
data = [H2O, H2O_2]

coverage = ut.calculate_coverage(data)

thermochem = ut.read_nist("H2O.txt")

system = p_vs_t.calculate(stoich, data, SE, adsorbant, thermochem, coverage)
system.plot(output="Example_4.png",)