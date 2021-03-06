'''OpenGL extension SGIX.subsample

This module customises the behaviour of the 
OpenGL.raw.GL.SGIX.subsample to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/SGIX/subsample.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.SGIX.subsample import *
### END AUTOGENERATED SECTION