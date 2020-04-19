import apps.base.utils
from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('id', models.CharField(default=apps.base.utils.custom_uuid, editable=False, max_length=11, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='full name')),
                ('description', models.TextField(blank=True, max_length=3000, verbose_name='description')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='start date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='end date')),
            ],
            options={
                'db_table': 'courses',
            },
        ),
    ]
