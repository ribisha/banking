# Generated by Django 4.2.7 on 2023-12-09 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0003_rename_bank_form_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='materials',
            field=models.ManyToManyField(to='bank_app.bank'),
        ),
    ]
