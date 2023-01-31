# Generated by Django 3.1.2 on 2021-10-17 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('part4', '0007_auto_20211017_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='part4.cart'),
        ),
        migrations.AlterField(
            model_name='computer',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='part4.order'),
        ),
        migrations.AlterField(
            model_name='storeuser',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='part4.cart'),
        ),
        migrations.AlterField(
            model_name='storeuser',
            name='orders',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='part4.order'),
        ),
    ]