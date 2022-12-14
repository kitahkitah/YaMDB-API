# Generated by Django 2.2.16 on 2022-05-12 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_third_branch'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('slug',)},
        ),
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ('-pub_date',)},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ('slug',)},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ('-pub_date',)},
        ),
        migrations.AlterModelOptions(
            name='title',
            options={'ordering': ('-name',)},
        ),
    ]
