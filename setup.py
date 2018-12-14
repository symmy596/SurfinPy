__author__ = "Adam R. Symington"
__copyright__ = "Copyright Adam R.Symington (2018)"
__version__ = "0.2"
__maintainer__ = "Adam R. Symington"
__email__ = "ars44s@bath.ac.uk"
__date__ = "04/09/2018"

from setuptools import setup
import os

module_dir = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    setup(
        name='surfinpy',
        version='0.2',
        description='Surface Phase Diagram Plotting Tools',
        long_description=open(os.path.join(module_dir, 'README.md')).read(),
        url='git@github.com:symmy596/SurfinPy.git',
        author='Adam R. Symington',
        author_email='ars44@bath.ac.uk',
        license='MIT license',
        packages=['surfinpy','tests'],
        zip_safe=False,
        install_requires=['scipy','numpy'],
        classifiers=['Programming Language :: Python',
                     'Development Status :: 5 - Production/Stable',
                     'Intended Audience :: Science/Research',
                     'Operating System :: OS Independent',
                     'Topic :: Scientific/Engineering']
    )