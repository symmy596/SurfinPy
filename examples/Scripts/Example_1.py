from surfinpy import mu_vs_mu

bulk = {'Cation' : 1, 'Anion' : 2, 'Energy' : -780.0, 'F-Units' : 4}

pure =     {'Cation': 24, 'X': 48, 'Y': 0, 'Area': 60.0, 'Energy': -575.0,   'Label': 'Stoich',  'nSpecies': 1}
H2O =      {'Cation': 24, 'X': 48, 'Y': 2, 'Area': 60.0, 'Energy': -612.0,   'Label': '1 Water', 'nSpecies': 1}
H2O_2 =    {'Cation': 24, 'X': 48, 'Y': 4, 'Area': 60.0, 'Energy': -640.0,   'Label': '2 Water', 'nSpecies': 1}
H2O_3 =    {'Cation': 24, 'X': 48, 'Y': 8, 'Area': 60.0, 'Energy': -676.0,   'Label': '3 Water', 'nSpecies': 1}
Vo =       {'Cation': 24, 'X': 46, 'Y': 0, 'Area': 60.0, 'Energy': -558.0,   'Label': 'Vo', 'nSpecies': 1}
H2O_Vo =   {'Cation': 24, 'X': 46, 'Y': 2, 'Area': 60.0, 'Energy': -594.0,  'Label': 'Vo + 1 Water', 'nSpecies': 1}
H2O_Vo_2 = {'Cation': 24, 'X': 46, 'Y': 4, 'Area': 60.0, 'Energy': -624.0,  'Label': 'Vo + 2 Water', 'nSpecies': 1}
H2O_Vo_3 = {'Cation': 24, 'X': 46, 'Y': 6, 'Area': 60.0, 'Energy': -640.0, 'Label': 'Vo + 3 Water', 'nSpecies': 1}
H2O_Vo_4 = {'Cation': 24, 'X': 46, 'Y': 8, 'Area': 60.0, 'Energy': -670.0, 'Label': 'Vo + 4 Water', 'nSpecies': 1}

data = [pure, H2O_2, H2O_Vo, H2O,  H2O_Vo_2, H2O_3, H2O_Vo_3,  H2O_Vo_4, Vo]

deltaX = {'Range': [ -12, -6],  'Label': 'O'}
deltaY = {'Range': [ -19, -12], 'Label': 'H_2O'}

system = mu_vs_mu.calculate(data, bulk, deltaX, deltaY)
system.plot_phase()

Zero_K = mu_vs_mu.calculate(data, bulk, deltaX, deltaY, x_energy=-4.54, y_energy=-14.84)
Zero_K.plot_phase(output="Example_1.png", set_style="seaborn-dark-palette", colourmap="RdYlBu")