# Generated by Django 4.0.5 on 2022-10-29 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_statementpage_intro'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StatementPage',
        ),
    ]
