# Generated by Django 3.0.6 on 2020-07-01 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ghostpost', '0003_auto_20200701_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boastsroasts',
            name='secret_id',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
