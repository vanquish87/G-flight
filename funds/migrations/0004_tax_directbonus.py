# Generated by Django 4.0.5 on 2022-06-16 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bonuses', '0001_initial'),
        ('funds', '0003_balance_rename_payment_number_payment_payment_num_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tax',
            name='directbonus',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.RESTRICT, to='bonuses.directbonus'),
        ),
    ]
