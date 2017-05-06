#!/usr/bin/python2
"""\
 coulomb.py Solve the eigenvectors and eigenvalues of the coulomb
  potential. The problem solved here is described in
  Practical Quantum Chemistry, by Richard P. Muller.
 Copyright (c) 2002, Richard P. Muller. All Rights Reserved.

 Usage: coulomb.py [options]

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

def OutputSolutions(ham):
    eval = ham.eval
    evec = ham.evec
    "Display solutions"
    n = len(eval)

    file = open('coulomb.dat','w')
    # Look at the lowest 3 energies:
    file.write("#Approximate solutions using %d points\n#" % (n-1))
    print "Energies:"
    for i in range(3):
        file.write(" %5.3f" % eval[i]) 
        print eval[i]
    file.write("\n")

    # Print the lowest eigenvectors:
    for i in range(n):
        x = ham.x(i)
        file.write("%5.3f %5.3f %5.3f %5.3f %5.3f \n" %\
                   (x,-10/abs(x),5*evec[0,i]-80,5*evec[1,i]-34,
                    5*evec[2,i]-19))
    return

def main(n):
    "The program starts here."
    # RPM: danger: there is a problem here with npts>21. Fix!!
    ham = oned_ham(n,-3.,3.,lambda x: -50/abs(x))
    ham.getHam()
    #print "Diagonal elements"
    #for i in range(ham.npoints): print i,ham.H[i,i]
    ham.solve()
    
    OutputSolutions(ham)

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

