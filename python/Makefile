# This Makefile should only be used in case  "setup.py"  fails,
# for example, because Python's "distutils" is not available
#
# Modify CFLAGS and LDFLAGS so that they point to the Python
# inlude and extension directories.
#
# If you installed the LWPR library in a non-standard location,
# you also need to include this as well

 CFLAGS+=-I/usr/include/python2.7 -I/usr/lib/python2.7/site-packages/numpy/core/include -fPIC
 LDFLAGS+=-lpython2.7 -lm -llwpr

#CFLAGS+=-I/home/olalekan/anaconda3/include/python3.6m -I/home/olalekan/anaconda3/lib/python3.6/site-packages/numpy/core/include -fPIC
#LDFLAGS+=-lpython3.6m -lm -llwpr 

default:
	gcc -shared -o lwpr.so lwprmodule.c  -Wno-missing-braces $(CFLAGS) $(LDFLAGS)
