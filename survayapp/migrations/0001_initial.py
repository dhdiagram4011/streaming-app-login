# Generated by Django 2.1.5 on 2020-09-30 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Survay_01',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_01', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Survay_02',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_02', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Survay_03',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_03', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Survay_04',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_04', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Survay_05',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_05', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Survay_06',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_06', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Survay_07',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_07', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Survay_08',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_08', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Survay_09',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_09', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Survay_email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Survay_name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
