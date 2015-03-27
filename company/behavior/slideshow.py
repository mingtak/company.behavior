from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope import schema
from plone.directives import form
from plone.namedfile.field import NamedBlobImage
from zope.component import adapts
from zope.interface import alsoProvides, implements, Invalid

from company.behavior import MessageFactory as _


def checkImage(imageItem):
    """Check image w:h is 3:2
    """
    width, height = imageItem.getImageSize()
    if (float(width)/float(height)) == 1.5:
        return True
    else:
        raise Invalid(_(u"Wrong image size , constraint w:h=3:2"))


class ISlideShow(model.Schema):
    """
       Marker/Form interface for SlideShow
    """
    # Slide show
    form.fieldset(
        'SlideShow',
        label=_(u"Slide show"),
        fields=['image1', 'image1_title', 'image1_description',
                'image2', 'image2_description',
                'image3', 'image3_description',
                'image4', 'image4_description',
                'image5', 'image5_description',],
        description=_(u'Image constraint w:h=3:2'),
    )

    image1 = NamedBlobImage(
        title=_(u'Image 1'),
        required=False,
        constraint=checkImage,
    )

    image2 = NamedBlobImage(
        title=_(u'Image 2'),
        required=False,
        constraint=checkImage,
    )

    image3 = NamedBlobImage(
        title=_(u'Image 3'),
        required=False,
        constraint=checkImage,
    )

    image4 = NamedBlobImage(
        title=_(u'Image 4'),
        required=False,
        constraint=checkImage,
    )

    image5 = NamedBlobImage(
        title=_(u'Image 5'),
        required=False,
        constraint=checkImage,
    )

    image1_title = schema.TextLine(
        title=_(u'Title for slide'),
        description=_(u'Will show in slide image 1'),
        required=False,
    )

    image1_description = schema.TextLine(
        title=_(u'short description for slide 1'),
        required=False,
    )

    image2_description = schema.TextLine(
        title=_(u'short description for slide 2'),
        required=False,
    )

    image3_description = schema.TextLine(
        title=_(u'short description for slide 3'),
        required=False,
    )

    image4_description = schema.TextLine(
        title=_(u'short description for slide 4'),
        required=False,
    )

    image5_description = schema.TextLine(
        title=_(u'short description for slide 5'),
        required=False,
    )


alsoProvides(ISlideShow, IFormFieldProvider)

def context_property(name):
    def getter(self):
        return getattr(self.context, name)
    def setter(self, value):
        setattr(self.context, name, value)
    def deleter(self):
        delattr(self.context, name)
    return property(getter, setter, deleter)


class SlideShow(object):
    """
       Adapter for SlideShow
    """
    implements(ISlideShow)
    adapts(IDexterityContent)

    def __init__(self,context):
        self.context = context

    # -*- Your behavior property setters & getters here ... -*-

    image1 = context_property('image1')
    image2 = context_property('image2')
    image3 = context_property('image3')
    image4 = context_property('image4')
    image5 = context_property('image5')

    image1_title = context_property('image1_title')

    image1_description = context_property('image1_description')
    image2_description = context_property('image2_description')
    image3_description = context_property('image3_description')
    image4_description = context_property('image4_description')
    image5_description = context_property('image5_description')
