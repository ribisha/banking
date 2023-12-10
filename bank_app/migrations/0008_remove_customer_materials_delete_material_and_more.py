# Generated by Django 4.2.7 on 2023-12-09 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0007_remove_customer_account_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='materials',
        ),
        migrations.DeleteModel(
            name='Material',
        ),
        migrations.AddField(
            model_name='customer',
            name='materials',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]