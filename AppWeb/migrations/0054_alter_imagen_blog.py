# Generated by Django 4.2.3 on 2023-09-08 01:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppWeb', '0053_rename_blog_imagen_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagen',
            name='blog',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='AppWeb.blog'),
        ),
    ]
