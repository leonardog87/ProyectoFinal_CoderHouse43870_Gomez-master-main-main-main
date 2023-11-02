# Generated by Django 4.2.3 on 2023-09-05 21:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppWeb', '0020_alter_mensaje_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensaje',
            name='messageid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rmensaje', to='AppWeb.blog'),
        ),
        migrations.AlterField(
            model_name='mensaje',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]