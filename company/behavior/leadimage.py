from five import grok
from plone.indexer import indexer

from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope import schema
from zope.component import adapts
from zope.interface import alsoProvides, implements, Interface
from plone.namedfile.field import NamedBlobImage

from company.behavior import MessageFactory as _


class ILeadImage(model.Schema):
    """
       Marker/Form interface for LeadImage
    """
    image = NamedBlobImage(
        title=_(u'Lead image'),
        required = False,
    )

    # -*- Your Zope schema definitions here ... -*-


alsoProvides(ILeadImage, IFormFieldProvider)

def context_property(name):
    def getter(self):
        return getattr(self.context, name)
    def setter(self, value):
        setattr(self.context, name, value)
    def deleter(self):
        delattr(self.context, name)
    return property(getter, setter, deleter)


class LeadImage(object):
    """
       Adapter for LeadImage
    """
    implements(ILeadImage)
    adapts(IDexterityContent)

    def __init__(self,context):
        self.context = context

    # -*- Your behavior property setters & getters here ... -*-
    image = context_property('image')


@indexer(Interface)
def aspectRatio_indexer(obj):
    if hasattr(obj, 'image'):
        width, height = obj.image.getImageSize()
        return float(width)/float(height)
grok.global_adapter(aspectRatio_indexer, name='aspectRatio')

@indexer(Interface)
def imageSize_indexer(obj):
    if hasattr(obj, 'image'):
        return obj.image.getSize()
grok.global_adapter(imageSize_indexer, name='imageSize')
