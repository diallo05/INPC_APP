# Generated by Django 5.0.6 on 2025-01-13 09:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cart",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("code", models.CharField(max_length=45)),
                ("name", models.CharField(max_length=45)),
                ("description", models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name="Moughataa",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("code", models.CharField(max_length=45)),
                ("label", models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("code", models.CharField(max_length=45)),
                ("name", models.CharField(max_length=45)),
                ("description", models.CharField(max_length=45)),
                ("unit_measure", models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name="ProductType",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("code", models.CharField(max_length=45)),
                ("label", models.CharField(max_length=45)),
                ("description", models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name="Wilaya",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("code", models.CharField(max_length=2)),
                ("name", models.CharField(max_length=252)),
            ],
        ),
        migrations.CreateModel(
            name="Commune",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("code", models.CharField(max_length=45)),
                ("name", models.CharField(max_length=45)),
                (
                    "moughataa",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="myapp.moughataa",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PointOfSale",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("code", models.CharField(max_length=45)),
                ("type", models.CharField(max_length=45)),
                ("gps_lat", models.FloatField()),
                ("gps_lon", models.FloatField()),
                (
                    "commune",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.commune"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CartProducts",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("weight", models.FloatField()),
                ("date_from", models.DateField()),
                ("date_to", models.DateField(blank=True, null=True)),
                (
                    "cart",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.cart"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.product"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductPrice",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("value", models.FloatField()),
                ("date_from", models.DateField()),
                ("date_to", models.DateField(blank=True, null=True)),
                (
                    "point_of_sale",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="myapp.pointofsale",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.product"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="product",
            name="product_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="myapp.producttype"
            ),
        ),
        migrations.AddField(
            model_name="moughataa",
            name="wilaya",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="myapp.wilaya"
            ),
        ),
    ]
