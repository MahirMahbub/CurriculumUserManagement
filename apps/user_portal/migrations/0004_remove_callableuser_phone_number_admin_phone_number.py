# Generated by Django 4.2.7 on 2023-11-17 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_portal', '0003_callableuser_is_staff_callableuser_phone_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='callableuser',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='admin',
            name='phone_number',
            field=models.CharField(default=None, max_length=10, unique=True),
            preserve_default=False,
        ),
    ]
