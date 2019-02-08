#!/bin/bash
g++ -c -fPIC test.cpp
g++ -shared -o liba.so test.o
pip install cython
python3 setup.py install
