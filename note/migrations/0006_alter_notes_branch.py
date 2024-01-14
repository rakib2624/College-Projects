# Generated by Django 5.0 on 2023-12-25 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0005_alter_notes_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='branch',
            field=models.CharField(choices=[('CSE', 'CSE'), ('EEE', 'EEE'), ('CIVIL', 'CIVIL'), ('MECHANICAL', 'MECHANICAL'), ('IT', 'IT'), ('NETWORKING', 'NETWORKING'), ('ECE', 'ECE'), ('OTHER', 'OTHER')], default='CSE', max_length=30),
        ),
    ]
