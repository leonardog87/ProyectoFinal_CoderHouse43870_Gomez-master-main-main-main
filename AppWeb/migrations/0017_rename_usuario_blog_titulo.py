# Generated by Django 4.2.3 on 2023-09-03 23:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppWeb', '0016_alter_blog_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='usuario',
            new_name='titulo',
        ),
    ]
