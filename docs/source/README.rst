
.. image:: Figures/Logo.png
    :align: center
    :alt: Project Logo

.. image::  https://readthedocs.org/projects/surfinpy/badge/?version=latest
    :target: https://surfinpy.readthedocs.io/en/latest/
    :alt: Documentation Status

.. image:: https://travis-ci.com/symmy596/SurfinPy.svg?branch=master
    :target: https://travis-ci.com/symmy596/SurfinPy
    :alt: Build Status

This is the documentation for the open-source Python project, `SurfinPy`.
A library designed to facilitate the generation of publication ready phase diagrams from ab initio calculations.
`surfinpy` is built on existing Python packages that those in the solid state physics/chemistry community should already be familiar with. 
This tool will bring some benfits to the solid state community and facilitate the generation of publication ready phase diagrams (powered by Matplotlib).

The main features include:

1. **Method to generate surface phase diagrams as a function of chemical potential.**  

   - Generate a diagram as a function of the chemical potential of two adsorbing species e.g. water and carbon dioxide.  
   - Generate a diagram as a function of the chemical potential of one adsorbing species and a surface species e.g. water and oxygen vacancies.  
   - Use experimental data combined with ab initio data to generate a temperature dependent phase diagram.  

2. **Method to generate surface phase diagrams as a function of temperature and pressure.**  

   - Use experimental data combined with ab initio data to generate a pressure vs temperature plot showing the state (e.g. composition) of a surface as a function of temperature and pressure of one species.

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

The code has been developed to be used with any ab initio code as it only requires a list of energies and vibrational frequencies.  
`surfinpy` was developed across several PhD projects and as such the functionality focuses on the research questions encountered during those projects, which we should clarify 
are wide ranging. Code contributions aimed at expanding the code to new problems are encouraged.

`surfinpy` is free to use.

Usage
-----

A full list of examples can be found in the examples folder of the git repository, these include jupyter notebook tutorials which combine the full theory with code examples.

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

Contact
~~~~~~~

If you have questions regarding any aspect of the software then please get in touch with the developer Adam Symington via email - ars44@bath.ac.uk. 
Alternatively you can create an issue on the `Issue Tracker <https://github.com/symmy596/SurfinPy/issues>`_ or you can discuss your questions on our `gitter channel <https://gitter.im/Surfinpy/Lobby>`_.

Bugs 
~~~~

There may be bugs. If you think you have caught one, please report it on the `Issue Tracker <https://github.com/symmy596/SurfinPy/issues>`_.
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


Research
--------

- `Strongly Bound Surface Water Affects the Shape Evolution of Cerium Oxide Nanoparticles <https://pubs.acs.org/doi/abs/10.1021/acs.jpcc.9b09046>`__
- `The energetics of carbonated PuO\ :sub:`2`\  surfaces affects nanoparticle morphology: a DFT+U study <https://pubs.rsc.org/lv/content/articlelanding/2020/cp/d0cp00021c/unauth#!divAbstract>`__
- `Exploiting cationic vacancies for increased energy densities in dual-ion batteries <https://www.sciencedirect.com/science/article/abs/pii/S2405829719310153>`__
- `Thermodynamic Evolution of Cerium Oxide Nanoparticle Morphology Using Carbon Dioxide <https://pubs.acs.org/doi/abs/10.1021/acs.jpcc.0c07437>`__ 