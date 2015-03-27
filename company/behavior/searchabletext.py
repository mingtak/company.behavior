from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope import schema
from plone.app.textfield import RichText
from zope.component import adapts
from zope.interface import alsoProvides, implements
from collective import dexteritytextindexer

from company.behavior import MessageFactory as _


class ISearchableText(model.Schema):
    """
       Marker/Form interface for SearchableText
    """
    dexteritytextindexer.searchable('text')
    text = RichText(
        title=_(u'Detail text'),
        required=False,
    )


alsoProvides(ISearchableText, IFormFieldProvider)

def context_property(name):
    def getter(self):
        return getattr(self.context, name)
    def setter(self, value):
        setattr(self.context, name, value)
    def deleter(self):
        delattr(self.context, name)
    return property(getter, setter, deleter)


class SearchableText(object):
    """
       Adapter for SearchableText
    """
    implements(ISearchableText)
    adapts(IDexterityContent)

    def __init__(self,context):
        self.context = context

    # -*- Your behavior property setters & getters here ... -*-
    text = context_property('text')
