# Generated by Django 4.2.7 on 2023-12-13 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_options_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='comment',
        ),
    ]
