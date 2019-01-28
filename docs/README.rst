
..image:: https://github.com/symmy596/SurfinPy/blob/master/logo/Logo.png?raw=true
    :align: center

.. image::  https://readthedocs.org/projects/surfinpy/badge/?version=latest
    :target: https://surfinpy.readthedocs.io/en/latest/
    :alt: Documentation Status

.. image:: https://travis-ci.com/symmy596/SurfinPy.svg?branch=master
    :target: https://travis-ci.com/symmy596/SurfinPy
    :alt: Build Status

This is the documentation for the open-source Python project, `surfinpy`.
A library designed to facilitate the generation of publication ready surface phase diagrams from ab initio calculations.
`surfinpy` is built on existing Python packages that those in the solid state physics/chemistry community should already be familiar with. 
It is hoped that this tool will bring some benfits to the solid state community and facilitate the generation of publication ready phase diagrams (powered by Matplotlib.)

The main features include:

1. **Method to generate 2D surface phase diagrams as a function of chemical potential.**  
   
   - Generate a diagram for two adsorbing species e.g. water and carbon dioxide.  
   - Generate a diagram for an adsorbing species and a surface species e.g. water and oxygen vacancies.  
   - Use experimental data combined with ab initio data to generate a temperature dependent phase diagram.  

2. **Method to generate 2D surface phase diagrams as a function of temperature and pressure.**  
   
   - Use experimental data combined with ab initio data to generate a pvt plot showing the state of a surface.   

3. **Use calculated surface energies to build crystal morphologies.**  
   
   - Use the surface energies produced by `surfinpy` alongside Pymatgen to built particle morphologies.  
   - Evaulate how a particles shape changes with temperature and pressure.   

The code has been developed to analyse VASP calculations however should in theory be compatible with other ab initio codes. 
`surfinpy` was developed during a PhD project and as such the functionality focuses on the research questions encountered during that project, which we should clarify 
are wide ranging. Code contributions aimed at expanding the code to new problems are encouraged.

`surfinpy` is free to use.

Usage
-----

A full list of examples can be found in the examples folder of the git repository, these include both the Python scripts needed to generate each plot, and 
jupyter notebook tutorials which combine the full theory with code examples.

Installation
------------

surfinpy is a Python 3 package and requires a typical scientific Python stack. Use of the tutorials requires Anaconda/Jupyter to be installed.

To build from source:

.. code-block:: bash

    pip install -r requirements.txt

    python setup.py build

    python setup.py install

    python setup.py test

Or alternatively install with pip

.. code-block:: bash

    pip install surfinpy

Documentation
-------------

To build the documentation from scratch 

.. code-block:: bash

    cd docs
    
    make html

License
-------

`surfinpy` is made available under the MIT License.


Detailed requirements
---------------------

`surfinpy` is compatible with Python 3.5+ and relies on a number of open source Python packages, specifically:

- Numpy
- Scipy
- Matplotlib
- Pymatgen

Contributing
------------

Bugs 
~~~~

There may be bugs. If you think you've caught one, please report it on the `Issue Tracker <https://github.com/symmy596/SurfinPy/issues>`_.
This is also the place to propose new ideas for features or ask questions about the design of `surfinpy`. Poor documentation is considered a bug 
so feel free to request improvements.

Code contributions
~~~~~~~~~~~~~~~~~~

We welcome help in improving and extending the package. This is managed through Github pull requests; for external contributions we prefer the
`"fork and pull" <https://guides.github.com/activities/forking/>`__
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
