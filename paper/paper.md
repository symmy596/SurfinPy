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

SurfinPy is a python module for generating phase diagrams from data derived from ab initio and/or classical techniques.

The previous code release, reported in Adam R. Symington *et. al.* , calculated the surface free energy under different external conditions, and used surface free energy values to generate phase diagrams. 
Phase diagrams have been used to provide an understanding of surface composition under various environmental conditions, thus providing crucial information for a range of materials science problems '[@Symington2020c;@Symington2020a;@Moxon2020]'. 
In this second release, the code has been expanded to generate phase diagrams for bulk phases, as well as surface phases. 

This `SurfinPy` release increases the capability of the previous release implementing the following major contributions

1.	The calculation of phase diagrams for bulk phases.
2. A significant update to the original code base in order to improve performance both in terms of capability and speedup, stream-line workflow and improve the plotting options.

The largest contribution to this release is the ability to calculate free energy of bulk phases (and not just surface phases) under various pressures and temperatures and plot phase diagrams for bulk phases as a function  of the chemical potential (and/or pressure) of two species, and as a function  of the chemical potential and temperature. 
Similarly to the surface module, in the bulk module, free energies of different phases are calculated under specific temperatures and pressures, which are then used to generate phase diagrams for bulk phases. 
Instead of an absolute value, temperature ranges can now be provided, enabling the ability to plot pressure as a function of temperature (or vice-versa) providing results, which are comparable to experimental data where available.

Another notable addition to this release is the ability to calculate vibrational properties for solid bulk phases. 
The vibrational modes for each solid bulk phase are used to calculate the zero point energy and thus the vibrational entropy. 
The code allows for the inclusion of these values into the generation of phase diagrams. 
This removes the approximation that entropy of solid phases does not contribute to the free energy and may improve the accuracy of the methodology.

![An example of a phase diagram as a function of chemical potential.\label{fig:example}](surfinpy.pdf)
Finally, eleven tutorials have been developed to highlight the full functionality of this new SurfinPy release. These are all available in jupyter notebooks in the repository.

# Statement of Need

`SurfinPy` is a python module for generating phase diagrams from *ab initio* and/or classical data.

With this release SurfinPy is no longer limited to the surface composition and chemistry and particle morphology, but expands on the chemistry of bulk phases, which make it ideal for applications to the broad spectrum of research questions around solid state chemistry and physics. 
This allows the exploration of the phase stability of solid state systems (bulk and surface phases) of different compositions as a function of external conditions. 

Other codes capable to produce phase diagrams *e.g.* pymatgen `[ONG2013314]` and ASE `[Hjorth_Larsen_2017]` are available.  However, our code is self-contained allowing for the generating both bulk and surface phase diagrams, while offering easier and enhanced plotting capability to compare phases as a function of chemical potential of different species and temperature.  Additionally, unlike other codes detailed tutorials are available, offering a more tailored and focused experience compared to other codes.

# Acknowledgements
  
The authors acknowledge support from the EPSRC (EP/K025597/1 and EP/R010366/1), and the Royal Society (Newton Advanced Fellowship NA150190).

# References
