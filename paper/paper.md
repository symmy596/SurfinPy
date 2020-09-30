---
title: 'surfinpy 2.0:'
tags:
- Chemistry
- Physics
- Density Functional Theory
- Solid State Chemistry
- Simulation
- materials
authors:
- name: Joshua Tse
  orcid: 0000-0002-1320-557X
  affiliation: 2
- name: Marco Molinari
  orcid: 0000-0001-7144-6075
  affiliation: 2
- name: Stephen C. Parker
  orcid: 0000-0003-3804-0975
  affiliation: 1
- name: Adam R. Symington
  orcid: 0000-0001-6059-497X
  affiliation: "1"
affiliations:
- name: Department of Chemistry, University of Bath
  index: 1
- name: Department of Chemistry, University of Huddersfield
  index: 2
date: 30 September 2020
bibliography: paper.bib
---

# Summary

SurfinPy is a python module for generating phase diagrams from DFT data. 
The previous code release, reported in Adam R. Symington *et. al.* \cite{Symington2019}, calculated the free energy for surfaces under different external conditions, used these surface free energies to generate a phase diagram. 
These phase diagrams can and have been used to provide an understanding of surface composition under various environmental conditions, thus providing crucial information for a range of materials science problems \cite{Symington2020c,Moxon2020}. 
In this new release,the code has been expanded to generate phase diagrams for bulk phases, as well as surface phases. 

This `surfinpy` release makes the following contributions

1. Introduces the new capability to calculate phase diagrams for bulk phases as a function of the chemical potential (and/or pressure) of two species.
2. Introduces the new capability to calculate phase diagrams for bulk phases as a function of the chemical potential and temperature.
3. Allows the calculation of vibrational entropy and zero point energy for solid phases and introduce these values in to the phase diagram generation.
4. A significant update to the original code base to improve performance, streamline workflow and improve the plotting options.

The largest contribution to this release is the ability to calculate and plot phase diagrams for bulk phases. 
This expands the current code base to calculate the free energy for bulk phases under various pressures and temperatures. 
Similarly, to the surface module free energies for each phase are calculated under a specific temperature and pressure which is then used to generate phase diagrams for bulk phases. 
Temperature ranges can now be provided instead of an absolute value, enabling the ability to plot temperature as a function of pressure providing results which are easily comparable to experiment.

Another noteable addition to this release is the ability to calculate vibrational properties for solid phases from density functional perturbation theory calculations. 
This method uses the vibrational modes for each structure to calculate zero point energy and vibrational entropy. 
These values can then be used to improve the accuracy of the free energy calculation and applies a higher level of theory.

Finally, eleven tutorials have been developed to highlight the full functionality of this new `surfinpy` release. These are all available in jupyter notebooks in the repository. 

![An example phase diagram as a function of chemical potential.\label{fig:example}](surfinpy.pdf)


# Statement of Need

`surfinpy` is a package for generating phase diagrams from ab initio data. 
The previous release facilitated research into the change in stability of different surface stoichiometries and the impact that this has on the particle morphology. 
In this new release we have expanded the code to allow bulk phase relationships to be researched. 
This allows the exploration of the phase stability of solid state systems as a function of external conditions. 
We have also added functionality to calculate and encorporate the vibrational entropy and zero point energy. 
This removes the approximation that solid phases don't contribute to the free energy and improves the accuracy of the methods.

With this release `surfinpy` is no longer limited to the surface chemistry and is now applicable to research questions across the solid state chemistry/physics field. 

# Acknowledgements
  
Joshs acknowledgements, Marcos acknowledgements, A.R.S acknowledeges AWE and EPSRC (EP/R010366/1) for funding.

# References