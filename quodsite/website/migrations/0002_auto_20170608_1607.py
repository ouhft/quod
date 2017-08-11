# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-08 16:07
from __future__ import unicode_literals

from django.db import migrations
import quodsite.website.models
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks
import wagtail.wagtailsnippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multipage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('text', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('publications_list', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailsnippets.blocks.SnippetChooserBlock(quodsite.website.models.Publication, label='publication'))), ('qa_list', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('question', wagtail.wagtailcore.blocks.RichTextBlock()), ('answer', wagtail.wagtailcore.blocks.RichTextBlock())), label='entry'))))),
        ),
    ]