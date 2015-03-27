from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope import schema
from zope.component import adapts
from zope.interface import alsoProvides, implements, Invalid

from Products.CMFDefault.utils import checkEmailAddress
from Products.CMFDefault.exceptions import EmailAddressInvalid

from company.behavior import MessageFactory as _


def checkEmail(value):
    try:
        checkEmailAddress(value)
    except EmailAddressInvalid:
        raise Invalid(_(u"Invalid email address."))
    return True


class IContactEmail(model.Schema):
    """
       Marker/Form interface for ContactEmail
    """

    contactEmail = schema.TextLine(
        title=_(u'Contact email'),
        required=False,
        constraint=checkEmail,
    )


alsoProvides(IContactEmail, IFormFieldProvider)

def context_property(name):
    def getter(self):
        return getattr(self.context, name)
    def setter(self, value):
        setattr(self.context, name, value)
    def deleter(self):
        delattr(self.context, name)
    return property(getter, setter, deleter)


class ContactEmail(object):
    """
       Adapter for ContactEmail
    """
    implements(IContactEmail)
    adapts(IDexterityContent)

    def __init__(self,context):
        self.context = context

    # -*- Your behavior property setters & getters here ... -*-
    contactEmail = context_property('contactEmail')
