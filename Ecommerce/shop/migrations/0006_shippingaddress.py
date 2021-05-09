# Generated by Django 3.1.7 on 2021-05-08 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_cart_cartproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('zipcode', models.CharField(max_length=200)),
                ('cardproduct', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.cartproduct')),
                ('userr', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.user')),
            ],
        ),
    ]