#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                Jiao Lin
#                      California Institute of Technology
#                      (C)    2007   All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from instrument.geometry.pml.Renderer import Renderer as base


class Renderer(base):


    def render(self, instrument):
        document = self.weave(instrument)
        return document


    # handlers

    def onInstrument(self, instrument):
        self.instrument = instrument
        
        self._rep += ['', '<!DOCTYPE instrument>', '']

        self._preElement( instrument )
        self._expandElementContainer( instrument )
        ig = instrument.geometer
        self.onInstrumentGeometer( ig )
        self._postElement( instrument )
        return

    
    def onInstrumentElementContainer(self, elementContainer):
        self._preElement( elementContainer )
        self._expandElementContainer( elementContainer )
        self._postElement( elementContainer )
        return
    

    onDetectorSystem = onDetectorArray = onDetectorPack = onDetector \
                       = onInstrumentElementContainer


    def onInstrumentElement(self, element):
        self._preElement( element )
        shape = element.shape()
        if shape: self.onShape( shape )
        self._postElement(element)
        return

    
    def onCopy(self, element):
        t = element.__class__.__name__
        self._write(
            '<%s %s />' % (t, attribs_str( element.attributes ) ) )
        return


    def _expandElementContainer(self, elementContainer):
        shape = elementContainer.shape()
        if shape : self.onShape( shape )
        
        for element in elementContainer.elements():
            element.identify(self)
            continue
        
        instrument_geometer = self.instrument.geometer
        lgeometer = instrument_geometer._getLocalGeometer( elementContainer )
        self.onLocalGeometer( lgeometer )
        return


    def _preElement(self, element):
        self._write('')
        t = element.__class__.__name__
        self._write(
            '<%s %s>' % (t, attribs_str( element.attributes ) ) )
        
        self._indent()
        return


    def _postElement(self, element):
        t = element.__class__.__name__
        
        self._outdent()
        
        self._write( '</%s>' % t )
        self._write('')
        return


    onPixel = onModerator = onMonitor = onGuide = onInstrumentElement

    #sample probably will become a composite
    #for now, treat it as a single element.
    onSample = onInstrumentElement


    def onLocalGeometer(self, geometer ):
        cs = geometer.registry_coordinate_system()
        self._write('<LocalGeometer registry-coordinate-system="%s">'%
                    cs.name)
        
        target = geometer.target

        self._indent()
        for element in target:
            position = tuple(geometer.position( element ) )
            #the following two lines are necessary because pyre.units
            #__str__ method does not explicitly print out unit of
            #pseudo-units like angle and solid-angle.
            orientation = geometer.orientation( element )
            orientation /= geometer.angle_unit
            #just to make it safer, convert to tuple
            orientation = tuple( orientation )
            self._write(
                '<Register name="%s" position="%s" orientation="%s"/>' % (
                element.name, position, orientation )
                )
            continue
        self._outdent()

        self._write('</LocalGeometer>')
        return


    def onInstrumentGeometer( self, geometer ):
        
        cs = geometer.registry_coordinate_system()

        t = geometer.__class__.__name__
        postfix = 'Geometer' 
        assert t.endswith( postfix )
        t = t[:-len( postfix )].lower()
        
        self._write(
            '<InstrumentGeometer registry-coordinate-system="%s" '\
            'type="%s" />' % (
            cs.name, t)
            )
        return


    def onShape(self, shape):
        self._write('<Shape>')
        shape.identify(self)
        self._write('</Shape>')
        return
    

    def _renderDocument(self, document):
        return document.identify(self)


    pass # end of Renderer


def attribs_str( attributes ):
    return ' '.join(
        ['%s="%s"' % (k, attributes.get(k)) for k in attributes ] )
        


# version
__id__ = "$Id: Renderer.py,v 1.1.1.1 2005/03/08 16:13:43 aivazis Exp $"

# End of file 
