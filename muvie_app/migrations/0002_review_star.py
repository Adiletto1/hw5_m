# Generated by Django 5.0.4 on 2024-05-02 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muvie_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='star',
            field=models.IntegerField(choices=[(1, '* '), (2, '* * '), (3, '* * * '), (4, '* * * * '), (5, '* * * * * ')], default=0, null=True),
        ),
    ]
