import apps.base.utils
from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('id', models.CharField(default=apps.base.utils.custom_uuid, editable=False, max_length=11, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255, verbose_name='first name')),
                ('last_name', models.CharField(max_length=255, verbose_name='last name')),
                ('email', models.EmailField(max_length=254, verbose_name='email address')),
            ],
            options={
                'db_table': 'students',
            },
        ),
    ]
