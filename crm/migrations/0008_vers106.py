# Generated by Django 3.1.6 on 2021-03-28 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0007_ver105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='developer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='links', to='crm.developer', verbose_name='застройщик'),
        ),
    ]