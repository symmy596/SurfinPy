from surfinpy import mu_vs_mu

Oxygen_exp = mu_vs_mu.temperature_correction("O2.txt", 298)
Water_exp = mu_vs_mu.temperature_correction("H2O.txt", 298)
Oxygen_corrected = (-9.08 + -0.86 + Oxygen_exp) / 2 
Water_corrected = -14.84 + 0.55 + Water_exp

bulk = {'Cation' : 1, 'Anion' : 2, 'Energy' : -781.954938, 'F-Units' : 32}

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


system =  mu_vs_mu.calculate(data, bulk, deltaX, deltaY, x_energy=Oxygen_corrected, y_energy=Water_corrected)

system.plot_phase(output="Example_3_1.png", temperature=298)

system.plot_pressure(output="Example_3_2.png", temperature=298)

system.plot_mu_p(output="Example_3_3.png", temperature=298)