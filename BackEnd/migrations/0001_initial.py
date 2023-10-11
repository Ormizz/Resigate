# Generated by Django 4.2.5 on 2023-10-10 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
                ('active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='AuthorizationStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
                ('active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='AuthorizationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
                ('active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
                ('active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_label', models.CharField(max_length=255)),
                ('short_label', models.CharField(max_length=255)),
                ('active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('label', models.CharField(max_length=255)),
                ('long_label', models.CharField(max_length=255)),
                ('short_label', models.CharField(max_length=255)),
                ('active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='ResidentialDistrict',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_label', models.CharField(max_length=255)),
                ('short_label', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('postal_code', models.CharField(max_length=6)),
                ('active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
                ('active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='ResiUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricule', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('birth_date', models.DateField()),
                ('sex', models.CharField(choices=[('FEMALE', 'Female'), ('MALE', 'Male')], max_length=6)),
                ('address', models.CharField(max_length=255)),
                ('postal_code', models.CharField(max_length=6)),
                ('house_number', models.CharField(max_length=10)),
                ('profession', models.CharField(max_length=255)),
                ('active', models.BooleanField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BackEnd.city')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BackEnd.userrole')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BackEnd.country'),
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_plate', models.CharField(max_length=10)),
                ('car_model', models.CharField(max_length=255)),
                ('car_color', models.CharField(max_length=255)),
                ('car_registration_document', models.TextField()),
                ('active', models.BooleanField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BackEnd.brand')),
            ],
        ),
        migrations.CreateModel(
            name='AccessHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_date', models.DateTimeField()),
                ('access_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BackEnd.accessstatus')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BackEnd.car')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BackEnd.resiuser')),
            ],
        ),
        migrations.CreateModel(
            name='AccessAuthorization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('active', models.BooleanField()),
                ('authorization_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BackEnd.authorizationtype')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BackEnd.authorizationstatus')),
            ],
        ),
    ]