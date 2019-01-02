theory
======

The physical quantity that is used to define the stability of a surface with a given composition is its surface energy $\gamma$ (J $m^{-2}$). 
At its core, surfinpy is a code that calculates the surface energy of different slabs and uses these surface energies to build a phase diagram.
In this exmplantion of theory we will use the example of water adsorbing onto a surface of $TiO_2$ containing oxygen vacancies.
In such an example there are two variables, water concentration and oxygen vacancy concentration. We are able to calculate the surface energy according to 

\begin{align}
\gamma_{Surf} & = \frac{1}{2A} \Bigg( E_{TiO_2}^{slab} - \frac{nTi_{slab}}{nTi_{Bulk}} E_{TiO_2}^{Bulk} \Bigg) - \Gamma_O \mu_O - \Gamma_{H_2O} \mu_{H_2O} ,
\end{align}

where A is the surface area, $E_{TiO_2}^{slab}$ is the DFT energy of the slab, $nTi_{Slab}$ is the number of cations in the slab, 
$nTi_{Bulk}$ is the number of cations in the bulk unit cell, $E_{TiO_2}^{Bulk}$ is the DFT energy of the bulk unit cell and

\begin{align}
\Gamma_O & = \frac{1}{2A} \Bigg( nO_{Slab} - \frac{nO_{Bulk}}{nTi_{Bulk}}nTi_{Slab}  \Bigg) ,
\end{align}

\begin{align}
\Gamma_{H_2O} & = \frac{nH_2O}{2A} ,
\end{align}

where $nO_{Slab}$ is the number of anions in the slab, $nO_{Bulk}$ is the number of anions in the bulk and $nH_2O$ is the number of adsorbing water molecules. 
$\Gamma_O$ / $\Gamma_{H_2O}$ is the excess oxygen / water at the surface and $\mu_O$ / $\mu_{H_2O}$ is the oxygen / water chemcial potential. 
Clearly $\Gamma$ and $\mu$ will only matter when the surface is non stoichiometric. 
