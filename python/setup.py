from distutils.core import setup, Extension
from distutils.sysconfig import get_python_lib
import os
from scipy._build_utils import numpy_nodepr_api

module = Extension('lwpr',
                    include_dirs = ['../include',
                       os.path.join(get_python_lib(),'numpy','core','include')],
                    libraries = ['../build/lwpr'],
                    sources = ['lwprmodule.c'],
                    **numpy_nodepr_api)

setup (name = 'LWPR Module',
       version = '1.1',
       description = 'Python wrapper around LWPR library',
       ext_modules = [module])
