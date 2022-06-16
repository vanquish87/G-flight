# Generated by Django 4.0.5 on 2022-06-16 05:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('funds', '0002_alter_tax_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='payment_number',
            new_name='payment_num',
        ),
        migrations.AlterField(
            model_name='tax',
            name='type',
            field=models.CharField(choices=[('GST', 'GST'), ('TDS', 'TDS')], max_length=200),
        ),
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('issue_num', models.CharField(max_length=200, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('payment', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to='funds.payment')),
            ],
        ),
    ]
