# Generated by Django 4.2.3 on 2023-09-06 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppWeb', '0036_alter_blog_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='imagen',
        ),
        migrations.DeleteModel(
            name='Blog2',
        ),
    ]
