# Generated by Django 5.1.6 on 2025-03-04 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(default='email@exemplo.com', max_length=254),
        ),
    ]
