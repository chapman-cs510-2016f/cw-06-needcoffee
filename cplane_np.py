#!/usr/bin/env python3

import abscplane
import numpy as np
import pandas as pd


"""
Implementation for Abstract Base Class AbsComplexPlane
A complex plane is a 2D grid of complex numbers, having
the form (x + y*1j), where 1j is the unit imaginary number,
and one can think of x and y as the coordinates for
the horizontal axis and the vertical axis of the plane, 
respectively.
"""

class ComplexPlane(abscplane.AbsComplexPlane):
    """Create and manipulate a complex plane
    In addition to generating the 2D grid of numbers (x + y*1j),
    the class supports transformations of the plane with
    an arbitrary function f. The attribute self.plane
    stores a 2D grid of numbers f(x + y*1j) such that the
    parameter x ranges from self.xmin to self.xmax with self.xlen
    total points, while the parameter y ranges from self.ymin to
    self.ymax with self.ylen total points. By default, the function
    f is the identity function lamdax:x, which does nothing to
    the bare complex plane.

    Attributes:
        xmax (float) : maximum horizontal axis value
        xmin (float) : minimum horizontal axis value
        xlen (int)   : number of horizontal points
        ymax (float) : maximum vertical axis value
        ymin (float) : minimum vertical axis value
        ylen (int)   : number of vertical points
        plane        : stored complex plane implementation
        f    (func)  : function displayed in the plane
    """
    
    def __init__(self, xmin, xmax, xlen, ymin, ymax, ylen):
        """
            Args:
            xmax (float) : maximum horizontal axis value
            xmin (float) : minimum horizontal axis value
            xlen (int)   : number of horizontal points
            ymax (float) : maximum vertical axis value
            ymin (float) : minimum vertical axis value
            ylen (int)   : number of vertical points
        """
        self.xmin = xmin
        self.xmax = xmax
        self.xlen = xlen 
        self.ymin = ymin
        self.ymax = ymax
        self.ylen = ylen
        self.f = lambda x:x
        
        #plane = []  #need this?
        self.refresh()
    
    def refresh(self):
        """Regenerate complex plane.
        For every point (x + y*1j) in self.plane, replace
        the point with the value self.f(x + y*1j). 
        """
        
        real = np.linspace(self.xmin,self.xmax,self.xlen)
        imaginary = np.linspace(self.ymin,self.ymax,self.ylen)
        x, y= np.meshgrid(real,imaginary)
        z = x+ y*1j
        rl = np.linspace(self.xmin,self.xmax,self.xlen)
        imag = np.linspace(self.ymin,self.ymax,self.ylen)
        self.plane = pd.DataFrame(self.f(z), index=imag, columns=rl)
        
    def zoom(self, xmin, xmax, xlen, ymin, ymax, ylen):
        """Reset self.xmin, self.xmax, and/or self.xlen.
        Also reset self.ymin, self.ymax, and/or self.ylen.
        Zoom into the indicated range of the x- and y-axes.
        Refresh the plane as needed.
        Args:
            xmax (float) : maximum horizontal axis value
            xmin (float) : minimum horizontal axis value
            xlen (int)   : number of horizontal points
            ymax (float) : maximum vertical axis value
            ymin (float) : minimum vertical axis value
            ylen (int)   : number of vertical points
        """

        self.refresh(xmin, xmax, xlen, ymin, ymax, ylen)

    def set_f(self, function):
        """Reset the transformation function f.
        Refreshes the plane after setting attribute 
        f to function.
        Args:
            function (function) : function to apply to 
                points of complex plane.
        """

        self.f = function
        self.refresh() #calls refresh to have function change take effect
        
    def __repr__(self):
        """Represent the complex plane as an even grid 
        of complex numbers
        """

        return str(self.plane)

def julia(c, max=100):
    def f(z):
        n = 1
        mag = abs(z)
        if mag > 2:
            return 1
        while n <= max:
            z = z**2 + c
            mag = abs(z)
            if mag > 2:
                return n
            else:
                n += 1
        return 0
    return f
