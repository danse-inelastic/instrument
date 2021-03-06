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

from pyre.geometry.pml.parser.Document import Document as base

class Document (base):

    tags = [
        "Axis", "Vector", "Angle",
        
        'Block',
        'Cylinder',
        'HollowCylinder',
        'Pyramid', 'Cone',
        'RectTube',
        'Sphere',
        'SphereShell',
        
        'Rotation', 'Translation', 'Dilation',
        'Union', 'Intersection', 'Difference',
        ]

    pass # end of Document


# version
__id__ = "$Id$"


# End of file 
