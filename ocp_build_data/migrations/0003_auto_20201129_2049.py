# Generated by Django 3.0.7 on 2020-11-29 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocp_build_data', '0002_auto_20200730_0647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openshiftcurrentadvisory',
            name='previous_advisory_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
