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
  affiliation: 2
  orcid: 0000-0001-6059-497X
affiliations:
- name: Department of Chemistry, University of Huddersfield
  index: 1
- name: Department of Chemistry, University of Bath
  index: 2
date: 08 December 2020
bibliography: paper.bib
---

# Summary

`SurfinPy` is a Python module for generating phase diagrams from data derived from *ab initio* and/or classical methodologies.

The previous code release, reported by @Symington2019, calculated the surface free energy values under different external conditions, and used these values to generate phase diagrams. 
Surface phase diagrams have been used to provide an understanding of surface composition under various environmental conditions, thus giving crucial information for a range of surface science problems [@Symington2020c;@Symington2020a;@Moxon2020]. 

In this second `SurfinPy` release, the capability of the code has been expanded to generate phase diagrams for bulk phases, as well as surface phases. The code now has the ability to calculate free energy values of bulk phases under specific values of pressure and temperature, and use these to plot phase diagrams for bulk phases as a function  of the chemical potential (and/or pressure) (\autoref{fig:example}) of two species, and as a function  of the chemical potential and temperature. 
Instead of an absolute value, temperature ranges can now be provided, enabling the ability to plot pressure as a function of temperature (or vice-versa), giving results that are comparable to experimental data where available.
Another notable addition to this release is the ability to calculate vibrational properties for bulk phases. 
The vibrational modes for bulk phases are used to calculate the zero point energy and thus the vibrational entropy. 
The code allows for the inclusion of these values into the generation of phase diagrams, which removes the approximation that entropy of bulk phases has little contribution to the free energy, and may improve the accuracy of the methodology.

A significant update to the original code has also been made to improve performance in terms of speedup, streamline workflow and enhanced plotting options.
Finally, eleven tutorials have been developed to highlight the full functionality of this new SurfinPy release. These are all available in Jupyter notebooks in the repository.

![An example of a phase diagram as a function of chemical potential.\label{fig:example}](surfinpy.pdf)



# Statement of Need

`SurfinPy` is a Python module for generating phase diagrams from *ab initio* and/or classical data.

With this release SurfinPy is no longer limited to the surface chemistry and particle morphology, but expands on the chemistry of bulk phases, which makes it ideal for applications to the broad spectrum of research questions in materials science, and solid-state chemistry and physics. 
This allows for the exploration of the phase stability of solid-state systems (bulk and surface phases) of different compositions as a function of external conditions. 

Other codes capable to produce phase diagrams, e.g., pymatgen [@ONG2013314] and ASE [@Hjorth_Larsen_2017] are available.  However, our code is self-contained allowing for the generation of both bulk and surface phase diagrams, while offering easier and enhanced plotting capability to compare phases as a function of chemical potential of different species and temperatures.  Additionally, unlike other codes detailed tutorials are available, offering a more tailored and focused experience compared to other codes.

# Acknowledgements
  
The authors acknowledge support from the EPSRC (EP/K025597/1 and EP/R010366/1), and the Royal Society (Newton Advanced Fellowship NA150190).

# References
