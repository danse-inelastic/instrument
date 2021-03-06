#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                 Jiao Lin   
#                      California Institute of Technology
#                      (C)   2007    All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from pyre.geometry.pml.parser.Cylinder import Cylinder as base
import instrument.geometry.shapes as shapes

class Cylinder( base ):

    def notify(self, parent):
        cylinder = shapes.cylinder(
            radius=self._radius, height=self._height)
        parent.onCylinder(cylinder)
        return


# version
__id__ = "$Id: Geometer.py,v 1.1.1.1 2005/03/08 16:13:43 linjiao Exp $"

# End of file 
