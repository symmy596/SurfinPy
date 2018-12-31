---
title: 'surfinpy: A Surface Phase Diagram Generator'
tags:
- Chemistry
- Physics
- Density Functional Theory
- Solid State Chemistry
- Simulation
- materials
authors:
- name: Adam R. Symington
  orcid: 0000-0001-6059-497X
  affiliation: "1"
- name: Joshua Tse
  affiliation: 2
- name: Marco Molinari
  orcid: 0000-0001-7144-6075
  affiliation: 2
- name: Stephen C. Parker
  orcid: 0000-0003-3804-0975
  affiliation: 1
affiliations:
- name: Department of Chemistry, University of Bath
  index: 1
- name: Department of Chemistry, University of Huddersfield
  index: 2
date: 24 December 2018
bibliography: paper.bib
---

# Summary

A surface phase diagram is a graphical representation of the different physical states of a surface under different conditions. A large number of problems in materials science concern the relationship between the state of the surface and the surrounding enviromental condtions. Examples include particle morphologies in solid state batteries [Canepa2018]; calculating the desorption temperature of water on surfaces [Molinari2012, Tegner2017]; catalytic reactions [Reuter2003]; or determing the effect of dopants and impurities on the surface stability.  

Computational modelling can be used to generate surface phase diagrams from density functional theory (DFT) data. One common research question is how water adsorption affects the surface of a material. To answer this a series of DFT calculations can be performed with varying concentrations of water on several different surfaces slabs. 
From this data the surface energy of each calculation (phase) as a function of temperature and pressure can be calculated according to the method employed in [Molinari2012]. 
However it is possible to go a step further and calculate the surface energy of each phase across the entire temperature range and then generate the entire pressure vs temperature phase diagram by evaluating which surface phase is more stable. 
A further degree of complexity can be introduced by considering surface defects e.g. vacancies or interstitials, or other adsorbants e.g. carbon dioxide. Using surface defects as an example, it is important to consider the relationship between the defective surface, the stoichiometric surface and the adsorbing water molecules. A surface phase diagram can be contructed as a function of the chemcial potential of the adsorbing spcies (water) and the surface defect (e.g. oxygen if oxygen vacancies are being considered). This is done using the method of [Marmier2004]. 

# `surfinpy`

`surfinpy` is a python module for generating a surface phase diagrams from DFT data. 
It contains two core modules for generating surface phase diagrams using both the methods employed in Molinari *et al.* Marmier *et al.*. These allow fast generation of temperature vs pressure phase diagrams and phase diagrams as a function of chemcial potential of species A and B. The plotting classes take the outputs of the calculation modules and generate phase diagrams using `matplotlib`. 
The `surfinpy` is aimed towards theoretical solid state physicist and chemists who a basic familiarity with Python. The repository contains examples of the core functionality as well as tutorials, implemented in jupyter notebooks to explain the full theory.

# Acknowledgements
  
ARS would like to thank Andrew R. McCluskey for his guidance through this project. This package was written during a PhD funded by AWE and EPSRC (EP/R010366/1). The input
data for the development and testing of this project was generated using ARCHER UK National Supercomputing Service (http://www.archer.ac.uk) via our membership of 
the UK's HEC Ma-terials Chemistry Consortium funded by EPSRC (EP/L000202).

# References