# Generated by Django 4.1.3 on 2022-11-22 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_order_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(through='payments.OrderItem', to='payments.item'),
        ),
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(max_length=255, null=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=255, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='order',
            name='description',
            field=models.TextField(null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payments.item'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payments.order'),
        ),
    ]
