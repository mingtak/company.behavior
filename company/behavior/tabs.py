from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope import schema
from plone.directives import form
from plone.app.textfield import RichText
from zope.component import adapts
from zope.interface import invariant, Invalid
from zope.interface import alsoProvides, implements

from company.behavior import MessageFactory as _


class TabsError(Invalid):
    __doc__ = _(u"Tabs and Descriptions are no match.")


class ITabs(model.Schema):
    """
       Marker/Form interface for Tabs
    """

    form.fieldset(
        'Tabs',
        label=_(u"Tabs"),
        fields=['tab1', 'description1', 'tab2', 'description2',
                'tab3', 'description3', 'tab4', 'description4', 'tab5', 'description5'],
        description=_(u"Tabs for product description."),
    )

    tab1 = schema.TextLine(
        title=_(u"Tab 1"),
        description=_(u"Tab1, max_length 8 words."),
        max_length=8,
        required=False,
    )

    description1 = RichText(
        title=_(u"Description 1"),
        description=_(u"Description for Tab 1"),
        required=False,
    )

    tab2 = schema.TextLine(
        title=_(u"Tab 2"),
        description=_(u"Tab2, max_length 8 words."),
        max_length=8,
        required=False,
    )

    description2 = RichText(
        title=_(u"Description 2"),
        description=_(u"Description for Tab 2"),
        required=False,
    )

    tab3 = schema.TextLine(
        title=_(u"Tab 3"),
        description=_(u"Tab3, max_length 8 words."),
        max_length=8,
        required=False,
    )

    description3 = RichText(
        title=_(u"Description 3"),
        description=_(u"Description for Tab 3"),
        required=False,
    )

    tab4 = schema.TextLine(
        title=_(u"Tab 4"),
        description=_(u"Tab4, max_length 8 words."),
        max_length=8,
        required=False,
    )

    description4 = RichText(
        title=_(u"Description 4"),
        description=_(u"Description for Tab 4"),
        required=False,
    )

    tab5 = schema.TextLine(
        title=_(u"Tab 5"),
        description=_(u"Tab5, max_length 8 words."),
        max_length=8,
        required=False,
    )

    description5 = RichText(
        title=_(u"Description 5"),
        description=_(u"Description for Tab 5"),
        required=False,
    )

    @invariant
    def checkTabs(data):
        if (data.tab1 is None) != (data.description1 is None) or \
           (data.tab2 is None) != (data.description2 is None) or \
           (data.tab3 is None) != (data.description3 is None) or \
           (data.tab4 is None) != (data.description4 is None) or \
           (data.tab5 is None) != (data.description5 is None):
            raise TabsError(_(u"The tabs and descriptions are no match."))


alsoProvides(ITabs, IFormFieldProvider)

def context_property(name):
    def getter(self):
        return getattr(self.context, name)
    def setter(self, value):
        setattr(self.context, name, value)
    def deleter(self):
        delattr(self.context, name)
    return property(getter, setter, deleter)


class Tabs(object):
    """
       Adapter for Tabs
    """
    implements(ITabs)
    adapts(IDexterityContent)

    def __init__(self,context):
        self.context = context

    # -*- Your behavior property setters & getters here ... -*-

    tab1 = context_property('tab1')
    tab2 = context_property('tab2')
    tab3 = context_property('tab3')
    tab4 = context_property('tab4')
    tab5 = context_property('tab5')
    description1 = context_property('description1')
    description2 = context_property('description2')
    description3 = context_property('description3')
    description4 = context_property('description4')
    description5 = context_property('description5')

