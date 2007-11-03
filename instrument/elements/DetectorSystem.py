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


from ElementContainer import ElementContainer

import journal
debug = journal.debug("instrument.elements")


class DetectorSystem( ElementContainer ):
    
    """Container for detector pack objects"""

    allowed_item_types = [
        'DetectorArray',
        'DetectorPack',
        'Detector',
        'Copy',
        ]

    def __init__( self, name, shape = None, **attributes):
        ElementContainer.__init__(
            self, name, shape=shape, **attributes)
        return


    def identify( self, visitor):
        return visitor.onDetectorSystem( self)


    pass # end of DetectorSystem


# version
__id__ = "$Id: DetectorSystem.py 1232 2007-08-29 15:18:03Z linjiao $"

# End of file
