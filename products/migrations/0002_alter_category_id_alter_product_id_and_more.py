# Generated by Django 5.2.1 on 2025-05-26 07:31

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.UUIDField(default=uuid.UUID('a29e8003-1c00-4eac-b429-20974f2f3e61'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.UUIDField(default=uuid.UUID('37d8f04f-1524-41b4-853d-59ef3e28a9f5'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='id',
            field=models.UUIDField(default=uuid.UUID('34310601-602c-4fca-88ec-95b1a0da7fe4'), editable=False, primary_key=True, serialize=False),
        ),
    ]
