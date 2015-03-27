from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope import schema
from zope.component import adapts
from zope.interface import alsoProvides, implements

from company.behavior import MessageFactory as _


class IExternalUrl(model.Schema):
    """
       Marker/Form interface for ExternalUrl
    """

    externalUrl = schema.URI(
        title=_(u'Externam url'),
        required=False,
    )


alsoProvides(IExternalUrl, IFormFieldProvider)

def context_property(name):
    def getter(self):
        return getattr(self.context, name)
    def setter(self, value):
        setattr(self.context, name, value)
    def deleter(self):
        delattr(self.context, name)
    return property(getter, setter, deleter)


class ExternalUrl(object):
    """
       Adapter for ExternalUrl
    """
    implements(IExternalUrl)
    adapts(IDexterityContent)

    def __init__(self,context):
        self.context = context

    # -*- Your behavior property setters & getters here ... -*-
    externalUrl = context_property('externalUrl')
