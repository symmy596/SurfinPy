__author__ = "Adam R. Symington"
__copyright__ = "Copyright Adam R.Symington (2019)"
__version__ = "1.0.1"
__maintainer__ = "Adam R. Symington"
__email__ = "ars44s@bath.ac.uk"
__date__ = "25/01/2019"

from setuptools import setup
import os

module_dir = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    setup(
        name='surfinpy',
        version='1.0.1',
        description='Surface Phase Diagram Plotting Tools',
        long_description=open(os.path.join(module_dir, 'README.md')).read(),
        long_description_content_type='text/markdown', 
        url='https://github.com/symmy596/SurfinPy',
        author='Adam R. Symington',
        author_email='ars44@bath.ac.uk',
        license='MIT license',
        packages=['surfinpy'],
        zip_safe=False,
        install_requires=['scipy', 'numpy', 'jupyter', 'pymatgen', 'numpy', 'matplotlib', 'coverage', 'coveralls'],
        classifiers=['Programming Language :: Python',
                     'Development Status :: 5 - Production/Stable',
                     'Intended Audience :: Science/Research',
                     'Operating System :: OS Independent',
                     'Topic :: Scientific/Engineering']
    )
