# SurfinPy

<p align="center"> 
<img src="https://github.com/symmy596/SurfinPy/blob/master/logo/Logo.png?raw=true" width="40%"/>
</p>

[![Documentation Status](https://readthedocs.org/projects/surfinpy/badge/?version=latest)](https://surfinpy.readthedocs.io/en/latest/)
[![Build Status](https://travis-ci.com/symmy596/SurfinPy.svg?branch=master)](https://travis-ci.com/symmy596/SurfinPy)
<a href='https://coveralls.io/github/symmy596/SurfinPy?branch=master'><img src='https://coveralls.io/repos/github/symmy596/SurfinPy/badge.svg?branch=master' alt='Coverage Status' /></a>

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.2549518.svg)](https://doi.org/10.5281/zenodo.2549518)
![Version](https://img.shields.io/badge/Version-1.0-blue.svg?maxAge=2592000)
[![PyPI version](https://badge.fury.io/py/surfinpy.svg)](https://badge.fury.io/py/surfinpy)
<a href='https://gitter.im/Surfinpy/Lobby'>
<img src='https://badges.gitter.im/gitterHQ/gitter.png' alt='Gitter chat' /></a>

This is the documentation for the open-source Python project - `surfinpy`.
A library designed to facilitate the generation of publication ready surface phase diagrams from ab initio calculations.
surfinpy is built on existing Python packages that those in the solid state physics/chemistry community should already be familiar with. 
It is hoped that this tool will bring some benfits to the solid state community and facilitate the generation of publication ready phase diagrams (powered by Matplotlib.)

The main features include:

1. **Method to generate 2D surface phase diagrams as a function of chemical potential.**  

   - Generate a diagram for two adsorbing species e.g. water and carbon dioxide.  
   - Generate a diagram for an adsorbing species and a surface species e.g. water and oxygen vacancies.  
   - Use experimental data combined with ab initio data to generate a temperature dependent phase diagram.  

2. **Method to generate 2D surface phase diagrams as a function of temperature and pressure.**  

   - Use experimental data combined with ab initio data to generate a pvt plot showing the state of a surface.  

3. **Use calculated surface energies to built crystal morphologies.**  

   - Use the surface energies produced by `surfinpy` alongside Pymatgen to built particle morphologies.  
   - Evaulate how a particles shape changes with temperature and pressure.

The code has been developed to analyse VASP calculations however should in theory be compatible with other ab initio codes.
`surfinpy` was developed during a PhD project and as such the functionality focuses on the research questions encountered during that project, which we should clarify
are wide ranging. Code contributions aimed at expanding the code to new of problems are encouraged.

`surfinpy` is free to use.

## Usage

A full list of examples can be found in the examples folder of the git repository, these include both the Python scripts needed to generate each plot, and 
jupyter notebook tutorials which combine the full theory with code examples.

## Installation

surfinpy is a Python 3 package and requires a typical scientific Python stack. Use of the tutorials requires Anaconda/Jupyter to be installed.

To build from source:

    pip install -r requirements.txt

    python setup.py build

    python setup.py install

    python setup.py test

Or alternatively install with pip

    pip install surfinpy


### Documentation

To build the documentation from scratch
  
    cd docs
    make html

### License

`surfinpy` is made available under the MIT License.

### Detailed requirements

`surfinpy` is compatible with Python 3.5+ and relies on a number of open source Python packages, specifically:

- Numpy
- Scipy
- Matplotlib
- Pymatgen

## Contributing

### Contact

If you have questions regarding any aspect of the software then please get in touch with the developer Adam Symington via email - ars44@bath.ac.uk. 
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

For further information please contact Adam Symington, ars44@bath.ac.uk

## Author

* Adam R.Symington
  
## Acknowledgements
  
* [Prof Stephen C.Parker](http://people.bath.ac.uk/chsscp/) - (Bath University)
* Joshua Tse (Huddersfield Uniersity)
