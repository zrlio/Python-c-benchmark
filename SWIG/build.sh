#!/bin/bash
swig -c++ -python foo_cpp.i
python3 ./setup.py install
