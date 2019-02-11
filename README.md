# Python -> C
Python -> C/C++ function call overhead benchmark. This repository allows you to run benchmarks on 6 different approaches:

* boost
* ctypes
* cython
* extension modules
* extension modules with manual unpacking
* SWIG

## Build & Run

For each approach you will find a subdirectory.
We recommend using virtual environments to run the benchmarks. Create a virtual environment in the directory
of the benchmark, e.g.:
```
$ cd cython
$ virtualenv --python=python3 venv
```
In the same directory, build the benchmark with:
```
$ ./build.sh
```
Or
```
$ python3 ./setup.py install
```
if the directory does not have a `build.sh` script.

To run the benchmark:
```
$ python3 ../bench/bench.py
```
