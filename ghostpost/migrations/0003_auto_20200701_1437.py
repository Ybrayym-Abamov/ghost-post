# Generated by Django 3.0.6 on 2020-07-01 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ghostpost', '0002_boastsroasts_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='boastsroasts',
            name='secret_id',
            field=models.CharField(default='nzbrtnlxes', max_length=10),
        ),
        migrations.AlterField(
            model_name='boastsroasts',
            name='downvotes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='boastsroasts',
            name='upvotes',
            field=models.IntegerField(default=0),
        ),
    ]
