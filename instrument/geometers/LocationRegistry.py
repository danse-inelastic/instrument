#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from ._journal import debug


from .CoordinateSystem import McStasCS
from . import CoordinateSystem


class LocationRegistry(object):

    '''Registry of position and orientation of geometrical
    objects.
    '''

    def __init__(self, coordinate_system = McStasCS):
        """
  - coordinate_system: the coordinate system. The position
    and orientation that are registered are expressed using
    this coordinate system.
    """
        self._coordinate_system = coordinate_system
        self._registry = {}
        return


    def register( self, element, offset, orientation, relative=None):
        if element in self._registry:
            raise RuntimeError("you have already registered %s before" % element)
        
        self._registry[ element ] = relative, offset, orientation
        return


    def registered(self, element):
        return self._registry.get(element) is not None


    def location(self, element):
        return self._registry[ element ]


    def coordinate_system(self): return self._coordinate_system

    pass # end of Geometer


def main():
    return

if __name__ == '__main__': main()
    

# version
__id__ = "$Id$"

# End of file
