#!/usr/bin/python

import sys 
import os
import subprocess

filename = 'haha.txt'

try:
  f = open(filename, 'rU')
  text = f.read()
  f.close()
except IOError:
    ## Control jumps directly to here if any of the above lines throws IOError.
  sys.stderr.write('problem reading:' + filename)
  ## In any case, the code then continues with the line after the try/except
