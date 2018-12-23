#!/bin/bash

cd ../
python setup.py build_ext --inplace
cd docs/
make html
