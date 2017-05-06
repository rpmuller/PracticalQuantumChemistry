#!/usr/bin/python2
"""\
 oned_ham.py Solve a general one-dimensional potential using a
  discrete set of points and a finite difference approximation.

 Copyright (c) 2002, Richard P. Muller. All Rights Reserved.

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307,
USA.
"""

import copy
from math import sqrt
from Numeric import zeros, dot, argsort, Float
from LinearAlgebra import eigenvectors

BIGVAL=100.0

class oned_ham:
    def __init__(self,npoints=11,xmin=0.,xmax=1.,vfunc=None):
        self.npoints = npoints
        self.xmin = xmin
        self.xmax = xmax
        self.vfunc = vfunc
        self.delta = (xmax-xmin)/(npoints-1)
        self.H = None
        self.eval = None
        self.evec = None
        return

    def x(self,i):
        return self.xmin + self.delta*i
        

    def getHam(self):
        self.H = getT(self.npoints)
        #for i in range(self.npoints): print i,self.H[i,i]
        if not self.vfunc:
            self.H[0,0] = self.H[self.npoints-1,self.npoints-1] =\
                           BIGVAL/(self.delta*self.delta)
        else:
            for i in range(self.npoints):
                x = self.x(i)
                self.H[i,i] = self.H[i,i] + self.vfunc(x)
        return

    def solve(self):
        self.eval,self.evec = eigenvectors(self.H)
        self.eval,self.evec = evsort(self.eval,self.evec)
        self.renormalize()
        return

    def renormalize(self):
        n = len(self.eval)
        h = 1./(n-1) #Grid spacing
        for i in range(n):
            maxval = max(self.evec[i])
            if maxval < 0: self.evec[i] = -self.evec[i]
            area = 0
            for j in range(n-1):
                area = area + 0.5*h*(self.evec[i,j]*self.evec[i,j]+
                                     self.evec[i,j+1]*self.evec[i,j+1])
            self.evec[i] = self.evec[i]/sqrt(area)
        return            
        
def getT(n):
    "Create an nxn KE Hamiltonian for the problem"
    T = zeros((n,n),Float) # get a zero matrix
    delta = 1./(n-1)
    for i in range(n):
        T[i,i] = 1/(delta*delta)
        if i:T[i-1,i] = T[i,i-1] = -0.5/(delta*delta)
    #for i in range(n): print i,T[i,i]
    return T

def evsort(eval,evec):
    """Since NumPy returns the eigenvectors/eigenvalues unsorted,
       perform a sort on them together, based on the eigenvalues."""

    n = len(eval)
    rows,cols = evec.shape
    newvec = copy.copy(evec)
    newval = copy.copy(eval)
    if n != rows:
        print "Help! eval and evec are different sizes!"
        sys.exit()

    index = argsort(eval)
    for i in index:
        newval[i] = eval[index[i]]
        newvec[i,:] = evec[index[i],:]

    return newval,newvec

if __name__ == '__main__':
    ham = oned_ham()
    ham.getHam()
    ham.solve()

