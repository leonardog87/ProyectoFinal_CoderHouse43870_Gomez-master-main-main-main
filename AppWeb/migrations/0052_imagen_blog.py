# Generated by Django 4.2.3 on 2023-09-07 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppWeb', '0051_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagen',
            name='Blog',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='imagenes2', to='AppWeb.blog'),
        ),
    ]