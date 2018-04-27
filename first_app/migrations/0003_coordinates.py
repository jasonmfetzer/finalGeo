# Generated by Django 2.0.2 on 2018-04-20 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_order_rollstock_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=10, max_digits=16)),
                ('longitude', models.DecimalField(decimal_places=10, max_digits=16)),
                ('altitude', models.DecimalField(decimal_places=10, max_digits=16)),
                ('intensity', models.DecimalField(decimal_places=10, max_digits=16)),
            ],
        ),
    ]