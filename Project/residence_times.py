#!/usr/bin/env python
import numpy
import sys

fname = sys.argv[1]
dat = numpy.loadtxt(fname, skiprows=20)
dists = dat[:,1:]

ncers = dists.shape[1]

inner = dists <= 0.65
outer = dists <= 0.75

contacts = numpy.zeros((len(dists)-1, dists.shape[1]), dtype = numpy.bool)

for ndx, (inn, out) in enumerate(zip(inner[:-1], outer[1:])):
    if ndx:
        contacts[ndx] = out*contacts[ndx-1] + inn
    else:
        contacts[ndx] = out*inner[0] + inn
    
diffs = contacts[1:].astype(numpy.int) - contacts[:-1].astype(numpy.int)

def get_ctimes(cnum):
    dat = diffs[:,cnum]
    inward = list(numpy.where(dat==1)[0])
    outward = list(numpy.where(dat==-1)[0])
    try:
        if outward[0] < inward[0]:
            outward.pop(0)
        if inward[-1] > outward[-1]:
            inward.pop(-1)
        tdiffs = zip(inward, outward)
        return [j-i for i,j in tdiffs]
    except IndexError:
        return []

totaltimes = []
for cer in xrange(ncers):
    ctimes = get_ctimes(cer)
    totaltimes.extend(ctimes)

dt = 200
bw = 5
bins = numpy.arange(0, max(totaltimes)+bw, bw) 
hist, bins = numpy.histogram(totaltimes, bins)
nhist = hist.astype(numpy.float)/numpy.sum(hist)

numpy.savetxt("times.xvg", numpy.column_stack((totaltimes,))*dt, fmt="%d")
numpy.savetxt("time-distribution.xvg", numpy.column_stack((bins[:-1]*dt+dt/2, nhist)), fmt=["%d", "%.5f"])

