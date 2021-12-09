---
title: 'SurfinPy 2.0:  A Phase Diagram Generator for Surfaces and Bulk Phases'
tags:
- Chemistry
- Physicsmar
- Density Functional Theory
- Solid State Chemistry
- Simulation
- materials
authors:
- name: Joshua S. Tse
  orcid: 0000-0002-1320-557X
  affiliation: 1
- name: Marco Molinari
  orcid: 0000-0001-7144-6075
  affiliation: 1
- name: Stephen C. Parker
  orcid: 0000-0003-3804-0975
  affiliation: 2
- name: Adam R. Symington
  orcid: 0000-0001-6059-497X
  affiliation: "2"
affiliations:
- name: Department of Chemistry, University of Huddersfield
  index: 1
- name: Department of Chemistry, University of Bath
  index: 2
date: 08 December 2020
bibliography: paper.bib
---

# Summary

SurfinPy is a python module for generating phase diagrams from Density Functional Theory data. 
The previous code release, reported in Adam R. Symington *et. al.* \cite{Symington2019}, calculated the surface free energy under different external conditions, and used these surface free energies to generate phase diagrams. 
These phase diagrams can and have been used to provide an understanding of surface composition under various environmental conditions, thus providing crucial information for a range of materials science problems \cite{Symington2020c,Symington2020a,Moxon2020}. 
In this new release, the code has been expanded to generate phase diagrams for bulk phases, as well as surface phases. 

This `SurfinPy` release makes the following contributions

1. Introduces a new capability to calculate phase diagrams for bulk phases as a function of the chemical potential (and/or pressure) of two species.
2. Introduces a new capability to calculate phase diagrams for bulk phases as a function of the chemical potential and temperature.
3. Allows the calculation of vibrational entropy and zero point energy for solid phases and introduce these values into the phase diagram generation.
4. A significant update to the original code base in order to improve performance, streamline workflow and improve the plotting options.

The largest contribution to this release is the ability to calculate and plot phase diagrams for bulk phases, which is a substantial expansion of the previous code to include free
energy for bulk phases (and not just surfaces) under various pressures and temperatures.
Similarly, to the surface module, free energies for each phase are calculated under a specific temperature and pressure, which is then used to generate phase diagrams for bulk phases. 
Instead of an absolute value, temperature ranges can now be provided, enabling the ability to plot pressure as a function of temperature (or vice-versa) providing results, which are comparable to experimental data where available.

Another notable addition to this release is the ability to calculate vibrational properties for solid phases from Density Functional Theory calculations. 
This method uses the vibrational modes for each structure to calculate the zero point energy and thus the vibrational entropy. 
These values can then be used to improve the accuracy of the free energy calculation and applies a higher level of theory. An example of bulk phase diagrams is shown in Figure 1.

Finally, eleven tutorials have been developed to highlight the full functionality of this new `SurfinPy` release. These are all available in jupyter notebooks in the repository. 

![An example of a phase diagram as a function of chemical potential.\label{fig:example}](surfinpy.pdf)


# Statement of Need

`SurfinPy` is a package for generating phase diagrams from ab initio data. 
The previous release facilitated research into the change in stability of different surface compositions and the impact that this has on the particle morphology. 
In this new release, we have expanded the code to allow bulk phase relationships to be researched. 
This allows the exploration of the phase stability of solid state systems of different compositions as a function of external conditions. 
We have also added functionality to calculate and incorporate the vibrational entropy and zero point energy. 
This removes the approximation that entropy of solid phases does not contribute to the free energy and improves the accuracy of the methods.

With this release SurfinPy is no longer limited to the surface chemistry, but expands on the chemistry of bulk phases, which makes it ideal for applications to the broad spectrum of research questions across the solid state chemistry and physics.

# Acknowledgements
  
The authors acknowledge support from the EPSRC (EP/K025597/1 and EP/R010366/1), and the Royal Society (Newton Advanced Fellowship NA150190).

# References
