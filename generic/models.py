from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.models import Page, Orderable
from wagtail.admin.panels import FieldPanel, MultipleChooserPanel


class GenericPage(Page):
    banner_title = models.CharField(
        max_length=100, 
        default='Welcome to my generic page'
        )
    introduction = models.TextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("introduction"), 
        MultipleChooserPanel(
            "banner_image",
            label="Banner image",
            chooser_field_name="image"
            ),
        ]

class GenericPageBannerImage(Orderable):
    page = ParentalKey(GenericPage,
        on_delete=models.CASCADE, 
        related_name='banner_image',
        )
    image = models.ForeignKey(
        'wagtailimages.Image', 
        null=True,
        blank=False,
        on_delete=models.SET_NULL, 
        related_name='banner_image'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]