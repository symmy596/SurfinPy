Theory
======

Before using this code you will need to generate the relevant data. `surfinpy` is a python module to generate surface phase diagrams from DFT calculation data. 
`surfinpy` has the capability to generate phase diagrams as a function of chemical potential of two species e.g. water and carbon dioxide. In such an example 
the user would require calculations with varying concentrations of water, carbon dioxide and water/carbon dioxide on a surface. Assuming that you have generating enough
data and reliable data then you are ready to use `surfinpy`.

Chemical potential
------------------

The physical quantity that is used to define the stability of a surface with a given composition is its surface energy :math:`\gamma` (J :math:`m^{-2}`). 
At its core, surfinpy is a code that calculates the surface energy of different slabs and uses these surface energies to build a phase diagram.
In this exmplantion of theory we will use the example of water adsorbing onto a surface of :math:`TiO_2` containing oxygen vacancies.
In such an example there are two variables, water concentration and oxygen vacancy concentration. We are able to calculate the surface energy according to 

.. math::
    \gamma_{Surf} = \frac{1}{2A} \Bigg( E_{TiO_2}^{slab} - \frac{nTi_{slab}}{nTi_{Bulk}} E_{TiO_2}^{Bulk} \Bigg) - \Gamma_O \mu_O - \Gamma_{H_2O} \mu_{H_2O} ,

where A is the surface area, :math:`E_{TiO_2}^{slab}` is the DFT energy of the slab, :math:`nTi_{Slab}` is the number of cations in the slab, 
:math:`nTi_{Bulk}` is the number of cations in the bulk unit cell, :math:`E_{TiO_2}^{Bulk}` is the DFT energy of the bulk unit cell and

.. math::
    \Gamma_O = \frac{1}{2A} \Bigg( nO_{Slab} - \frac{nO_{Bulk}}{nTi_{Bulk}}nTi_{Slab}  \Bigg) ,

.. math::
    \Gamma_{H_2O} = \frac{nH_2O}{2A} ,

where :math:`nO_{Slab}` is the number of anions in the slab, :math:`nO_{Bulk}` is the number of anions in the bulk and :math:`nH_2O` is the number of adsorbing water molecules. 
:math:`\Gamma_O` / :math:`\Gamma_{H_2O}` is the excess oxygen / water at the surface and :math:`\mu_O` / :math:`\mu_{H_2O}` is the oxygen / water chemcial potential. 
Clearly :math:`\Gamma` and :math:`mu` will only matter when the surface is non stoichiometric. 

The resultant phase diagram is at 0K. It is possible to use experimental data from the NIST_JANAF database to make the chemical potential a temperature dependent
term and thus generate a phase diagram at a temperature (T). This is done according to

.. math::
    \gamma_{Surf} = \frac{1}{2A} \Bigg( E_{TiO_2}^{slab} - \frac{nTi_{Slab}}{nTi_{Bulk}} E_{TiO_2}^{Bulk} \Bigg) - \Gamma_O \mu_O - \Gamma_{H_2O} \mu_{H_2O} - n_O \mu_O (T) - n_{H_2O} \mu_{H_2O} (T) 

where 

.. math::
    \mu_O (T)  = \frac{1}{2} \mu_O (T) (0 K , DFT) +  \frac{1}{2} \mu_O (T) (0 K , EXP) +  \frac{1}{2} \Delta G_{O_2} ( \Delta T, Exp),

:math:`\mu_O` (T) (0 K , DFT) is the 0K free energy of an isolated oxygen molecule evaluated with DFT, :math:`\mu_O` (T) (0 K , EXP) is the 0 K experimental 
Gibbs energy for oxygen gas and $\Delta$ :math:`G_{O_2}` ( :math:`\Delta` T, Exp) is the Gibbs energy defined at temperature T as

.. math::
    \Delta G_{O_2} ( \Delta T, Exp)  = \frac{1}{2} [H(T, {O_2}) -  H(0 K, {O_2})] -  \frac{1}{2} T[S(T, {O_2}])

finally, chemical potential can be converted to pressure values according to

.. math::
    P = \frac{\mu_O}{k_B T}

where P is the pressure, :math:`\mu` is the chemical potential of oxygen, :math:`k_B` is the Boltzmnann constant and T is the temperature. 

Pressure vs temperature
-----------------------

`Surfinpy` has the functionality to generate phase diagrams as a function of pressure vs temperature based upon the methodology used in Molinari et al. 
(J. Phys. Chem. C  116, 12, 7073-7082) according to

.. math::
    \gamma_{adsorbed, T, P} = \gamma_{bare} + ( C ( E_{ads, T} - RTln(\frac{p}{p^o})

where :math:`\gamma_{adsorbed, T, p}` is the surface energy of the surface with adsorbed species at temperature (T) and pressure (P), 
:math:`\gamma_{bare}` is the suface energy of the bare surface, C is the coverage of adsorbed species, :math:`E_{ads}` is the adsorption energy, 

.. math::
    E_{ads, T} =  E_{slab, adsorbant} - (E_{slab, bare} + n_{H_2O} E_{H_2O, T}) / n_{H_2O}

where :math:`E_{slab, adsorbant}` is the energy of the surface and the adsorbed species, :math:`n_{H_2O}` is he number of adsorbed species, 

.. math::
    E_{H_2O, (T)} = E_{H_2O, (g)} - TS_{(T)}

where :math:`S_{(T)}` is the experimental entropy of gaseous water in the standard state.