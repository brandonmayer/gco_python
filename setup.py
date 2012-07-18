from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy
import os

gco_directory = "../../tools/gco/"
#gco_directory = "C:/gc0-v3.0/src"
gco_directory = os.path.realpath(gco_directory) 

files = ['GCoptimization.cpp', 'graph.cpp', 'LinkedBlockList.cpp',
    'maxflow.cpp']

files = [os.path.join(gco_directory,f) for f in files]
files.insert(0, "gco_python.pyx")

setup(cmdclass={'build_ext': build_ext},
    ext_modules=[Extension("pygco", files, language="c++",
    include_dirs=[gco_directory, numpy.get_include()], 
    library_dirs=[gco_directory])])
