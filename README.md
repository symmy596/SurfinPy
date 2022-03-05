# SurfinPy


<p align="center"> 
<img src="https://github.com/symmy596/SurfinPy/blob/master/logo/Logo.png?raw=true" width="40%"/>
</p>

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.2573646.svg)](https://doi.org/10.5281/zenodo.2573646)
[![status](http://joss.theoj.org/papers/368e55451d3fd6ae4b939e1b8e7843ba/status.svg)](http://joss.theoj.org/papers/368e55451d3fd6ae4b939e1b8e7843ba)
[![DOI](https://joss.theoj.org/papers/10.21105/joss.04014/status.svg)](https://doi.org/10.21105/joss.04014)
[![Documentation Status](https://readthedocs.org/projects/surfinpy/badge/?version=latest)](https://surfinpy.readthedocs.io/en/latest/)
[![Build Status](https://travis-ci.com/symmy596/SurfinPy.svg?branch=master)](https://travis-ci.com/symmy596/SurfinPy)
[![Build status](https://ci.appveyor.com/api/projects/status/nww04m6tp3335jjr?svg=true)](https://ci.appveyor.com/project/symmy596/surfinpy)
[![PyPI version](https://badge.fury.io/py/surfinpy.svg)](https://badge.fury.io/py/surfinpy)
<a href='https://coveralls.io/github/symmy596/SurfinPy?branch=master'><img src='https://coveralls.io/repos/github/symmy596/SurfinPy/badge.svg?branch=master' alt='Coverage Status' /></a>
<a href='https://gitter.im/Surfinpy/Lobby'>
<img src='https://badges.gitter.im/gitterHQ/gitter.png' alt='Gitter chat' /></a>
 
This is the documentation for the open-source Python project - `surfinpy`.
A library designed to facilitate the generation of publication ready phase diagrams from ab initio calculations for both surface and bulk materials.
surfinpy is built on existing Python packages that those in the solid state physics/chemistry community should already be familiar with. 
It is hoped that this tool will bring some benfits to the solid state community and facilitate the generation of publication ready phase diagrams (powered by Matplotlib.)
 
The main features include:

1. **Method to generate surface phase diagrams as a function of chemical potential.**  

   - Generate a diagram as a function of the chemical potential of two adsorbing species e.g. water and carbon dioxide.  
   - Generate a diagram as a function of the chemical potential of one adsorbing species and a surface species e.g. water and oxygen vacancies.  
   - Use experimental data combined with ab initio data to generate a temperature dependent phase diagram.  

2. **Method to generate surface phase diagrams as a function of temperature and pressure.**  

   - Use experimental data combined with ab initio data to generate a pressure vs temperature plot showing the state of a surface as a function of temperature and pressure of one species.

3. **Use calculated surface energies to built crystal morphologies.**  

   - Use the surface energies produced by `surfinpy` alongside Pymatgen to built particle morphologies.  
   - Evaulate how a particles shape changes with temperature and pressure.

4. **Method to generate bulk phase diagrams as a function of chemical potential.**  

   - Generate a diagram as a function of the chemical potential of two species e.g. water and carbon dioxide.  
   - Use experimental data combined with ab initio data to generate a temperature dependent phase diagram.  

5. **Method to generate bulk phase diagrams as a function of temperature and pressure.**  

   - Use experimental data combined with ab initio data to generate a pressure vs temperature plot showing the phase space as a function of temperature and pressure.  

6. **Method to include vibrational properties in a phase diagram**
   
   - Module to calculate the zero point energy and vibrational entropy
   - Encorporate the zero point energy and/or the vibrational entropy into a phase diagram.

The code has been developed to analyse VASP calculations but is compatible with other ab initio codes. 
`surfinpy` was developed across several PhD projects and as such the functionality focuses on the research questions encountered during those projects, which we should clarify 
are wide ranging. Code contributions aimed at expanding the code to new problems are encouraged.

`surfinpy` is free to use.

## Usage

A full list of examples can be found in the examples folder of the git repository, these include jupyter notebook tutorials which combine the full theory with code examples.

## Installation

surfinpy is a Python 3 package and requires a typical scientific Python stack. Use of the tutorials requires Anaconda/Jupyter to be installed.

To build from source:

    pip install -r requirements.txt -e .

Or for jupyter compatable use

    pip install -r requirements.txt -e .[Tutorials]

    python setup.py test


Or alternatively install with pip

    pip install surfinpy


### Documentation

To build the documentation from scratch
  
    cd docs
    make html

Alternativly, documentation can be found [here](https://surfinpy.readthedocs.io/en/latest/).

### License

`surfinpy` is made available under the MIT License.

### Detailed requirements

`surfinpy` is compatible with Python 3.5+ and relies on a number of open source Python packages, specifically:

- Numpy
- Scipy
- Matplotlib
- Pymatgen
- Seaborn
- Pyyaml
- Jupyter (Examples using Jupyter Notebooks, use Tutorials install)


## Contributing

### Contact

If you have questions regarding any aspect of the software then please get in touch with the development team via email Adam Symington (symmy596@gmail.com), Joshua Tse (joshua.s.tse@gmail.com). 
Alternatively you can create an issue on the [Issue Tracker](https://github.com/symmy596/SurfinPy/issues) or you can discuss your questions on our [gitter channel](https://gitter.im/Surfinpy/Lobby).

### Bugs

There may be bugs. If you think you've caught one, please report it on the [Issue Tracker](https://github.com/symmy596/SurfinPy/issues).
This is also the place to propose new ideas for features or ask questions about the design of `surfinpy`. Poor documentation is considered a bug
so feel free to request improvements.

### Code contributions

We welcome help in improving and extending the package. This is managed through Github pull requests; for external contributions we prefer the
["fork and pull"](https://guides.github.com/activities/forking/)__
workflow while core developers use branches in the main repository:

   1. First open an Issue to discuss the proposed contribution. This
      discussion might include how the changes fit surfinpy's scope and a
      general technical approach.
   2. Make your own project fork and implement the changes
      there. Please keep your code style compliant with PEP8.
   3. Open a pull request to merge the changes into the main
      project. A more detailed discussion can take place there before
      the changes are accepted.

For further information please contact Adam Symington - symmy596@gmail.com, Joshua Tse - joshua.s.tse@gmail.com

## Research

- [Strongly Bound Surface Water Affects the Shape Evolution of Cerium Oxide Nanoparticles](https://pubs.acs.org/doi/abs/10.1021/acs.jpcc.9b09046)
- [The energetics of carbonated PuO2 surfaces affects nanoparticle morphology: a DFT+U study](https://pubs.rsc.org/lv/content/articlelanding/2020/cp/d0cp00021c/unauth#!divAbstract)
- [Exploiting cationic vacancies for increased energy densities in dual-ion batteries](https://www.sciencedirect.com/science/article/abs/pii/S2405829719310153)
- [Thermodynamic Evolution of Cerium Oxide Nanoparticle Morphology Using Carbon Dioxide](https://pubs.acs.org/doi/abs/10.1021/acs.jpcc.0c07437)

## Author

* Adam R.Symington
* Joshua Tse (Uniersity of Huddersfield)  

## Acknowledgements
  
* [Prof Stephen C.Parker](http://people.bath.ac.uk/chsscp/) - (Bath University)

