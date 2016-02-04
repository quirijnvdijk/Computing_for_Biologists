#!/usr/bin/env python
import numpy
import sys

fname = sys.argv[1]
dat = numpy.loadtxt(fname, skiprows=20)
dists = dat[:,1:]
result = numpy.average(dists <= 0.65, axis=0)
norresult = result.astype(numpy.float)/numpy.sum(result)
resnums = numpy.arange(len(result))+1

numpy.savetxt("rescount.xvg", numpy.column_stack((resnums, result)), fmt=["%d", "%.5f"])
numpy.savetxt("norescount.xvg", numpy.column_stack((resnums, norresult)), fmt=["%d", "%.5f"])

