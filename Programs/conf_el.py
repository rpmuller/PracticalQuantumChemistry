#!/usr/bin/python2
"""\
 conf_el.py Solve the eigenvectors and eigenvalues of the confined
  electron. The problem solved here is described in
  Practical Quantum Chemistry, by Richard P. Muller.
 Copyright (c) 2002, Richard P. Muller. All Rights Reserved.

 Usage: conf_el.py [options]

 Options:
 -h     Print this help message
 -n #   Use # points in the finite approximation

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

# Import the libraries we will use
import sys,getopt
from math import pi, sqrt,sin
from oned_ham import oned_ham

def AnalyticalEnergy(i):
    "Return the ith eigenvalue for the confined electron"
    # The analytical solutions are given by
    return 0.5*i*i*pi*pi

def AnalyticalWFN(x):
    return sqrt(2)*sin(pi*x)

def CompareSolutions(eval,evec):
    "Compare our solutions to the analytical ones"
    n = len(eval)

    # Look at the lowest 3 energies:
    print "Approximate solutions using %d points" % (n-1)
    print "Numeric Analytical"
    for i in range(3):
        print "%5.3f %5.3f" % (eval[i],AnalyticalEnergy(i+1))

    # Compare the lowest eigenvector:
    for xi in range(n):
        x = float(xi)/(n-1)
        print x,evec[0,xi],AnalyticalWFN(x)
    return

def main(n):
    "The program starts here."
    ham = oned_ham(n)
    ham.getHam()
    ham.solve()
    
    CompareSolutions(ham.eval,ham.evec) #Compare solutions to analytical

    #done
    return

if __name__ == '__main__':
    # The program comes here when it is run interactively. There
    #  are 3 steps we need to do:
    
    # 1. Get the command line flags
    opts,args = getopt.getopt(sys.argv[1:],'-hn:')

    # 2. Set defaults and parse the command line flags
    n = 11 # default number of points
    for (key,value) in opts:
        if key == '-h':
            print __doc__
            sys.exit()
        elif key == '-n':
            n = int(value)

    # 3. Call the main program
    main(n)

