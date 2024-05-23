# Generated by Django 5.0.6 on 2024-05-23 09:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screen', models.CharField(max_length=200)),
                ('os', models.CharField(max_length=200)),
                ('camera', models.CharField(max_length=200)),
                ('camera_front', models.CharField(max_length=200)),
                ('cpu', models.CharField(max_length=200)),
                ('ram', models.CharField(max_length=200)),
                ('rom', models.CharField(max_length=200)),
                ('micro_usb', models.CharField(max_length=200)),
                ('battery', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_payment', models.DateField()),
                ('method_payment', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Promo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('value', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('kind', models.CharField(max_length=200)),
                ('company', models.CharField(max_length=200)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('phone', models.CharField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200, unique=True)),
                ('role', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('img', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
                ('star', models.IntegerField(default=0)),
                ('rate_count', models.IntegerField(default=0)),
                ('detail', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.detail')),
                ('promo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.promo')),
            ],
        ),
        migrations.CreateModel(
            name='ShopOrder',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_order', models.DateField()),
                ('total_price', models.CharField(max_length=200)),
                ('status_order', models.CharField(max_length=200)),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.payment')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
                ('shipping', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.shipping')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
        ),
        migrations.CreateModel(
            name='ShopCart',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
        ),
        migrations.AddField(
            model_name='payment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user'),
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
        ),
        migrations.CreateModel(
            name='UserComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=200)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
        ),
    ]
