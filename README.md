# SurfinPy
  
[![Documentation Status](https://readthedocs.org/projects/surfinpy/badge/?version=latest)](https://surfinpy.readthedocs.io/en/latest/)
[![Build Status](https://travis-ci.com/symmy596/SurfinPy.svg?branch=master)](https://travis-ci.com/symmy596/SurfinPy)
<a href='https://coveralls.io/github/symmy596/SurfinPy?branch=master'><img src='https://coveralls.io/repos/github/symmy596/SurfinPy/badge.svg?branch=master' alt='Coverage Status' /></a>
![Version](https://img.shields.io/badge/Version-0.2.2-blue.svg?maxAge=2592000)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/symmy596/Surfinpy/issues)
[![MIT license](http://img.shields.io/badge/license-MIT-brightgreen.svg)](http://opensource.org/licenses/MIT)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)


This is the documentation for the open-source python project, `surfinpy`.
A library designed to facilitate the generation of publication ready surface phase diagrams from ab initio calculations.
surfinpy is built on existing python packages that those in the solid state physics/chemistry community should already be familiar with. 
It is hoped that this tool will bring some benfits to the solid state community and facilitate the generation of publication ready phase diagrams (powered by Matplotlib.)

The main features include:

1. **Method to generate 2D surface phase diagrams as a function of chemical potential.**  
   
   - Generate a diagram for two adsorbing species e.g. water and carbon dioxide.  
   - Generate a diagram for an adsorbing species and a surface species e.g. water and oxygen vacancies.  
   - Use experimental data combined with ab initio data to generate a phase diagram at a desired temperature.  

2. **Method to generate 2D surface phase diagrams as a function of temperature and pressure.**  
   
   - Use experimental data combined with ab inition data to generate a pvt plot of the state of a surface.  

3. **Use calculated surface energies to built crystal morphologies.**  
   
   - Use the surface energies produced by surfinpy and Pymatgen to built particle morphologies.  
   - Evaulate how a particles shape changes with temperature and pressure.   

The code has been developed to analyse VASP calculations however should in theory be compatible with other ab initio codes. 
surfinpy was developed during a PhD project and as such the functionality focuses on the research questions encountered during that project, which we should clarify 
are wide ranging. Code contributions aimed at expanding the code to a wider range of problems are encouraged.

surifnpy is free to use.

## Usage


A full list of examples can be found in the examples folder of the git repository, these include both the python scripts needed to generate each plot, and 
jupyter notebook tutorials which combine the full theory with code examples.

## Installation

surfinpy is a Python 3 package and requires a typical scientific Python stack. Use of the tutorials requires Anaconda/Jupyter to be installed.

To build from source:

    pip install -r requirements.txt

    python setup.py build

    python setup.py install

    python setup.py test


### Documentation

To build the documentation from scratch 
  
    cd docs   
    make html   

### License

surfinpy is made available under the MIT License.


### Detailed requirements

surfinpy is compatible with Python 3.5+ and relies on a number of open source python packages, specifically:

- Numpy
- Scipy
- Matplotlib
- Pymatgen

## Contributing

### Bugs 


There may be bugs. If you think you've caught one, please report it on the [Issue Tracker](https://github.com/symmy596/SurfinPy/issues).
This is also the place to propose new ideas for features or ask questions about the design of surfinpy. Poor documentation is considered a bug 
so feel free to request improvements.

### Code contributions

We welcome help in improving and extending the package. This is managed through Github pull requests; for external contributions we prefer the
["fork and pull"](https://guides.github.com/activities/forking/)__
workflow while core developers use branches in the main repository:

   1. First open an Issue to discuss the proposed contribution. This
      discussion might include how the changes fit Sumo's scope and a
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

