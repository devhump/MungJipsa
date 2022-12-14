# Generated by Django 3.2.13 on 2022-12-09 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deserted',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kindCd', models.CharField(max_length=100)),
                ('colorCd', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=50)),
                ('weight', models.CharField(max_length=30)),
                ('happenDt', models.DateField()),
                ('happenPlace', models.CharField(max_length=100)),
                ('noticeSdt', models.DateField()),
                ('noticeEdt', models.DateField()),
                ('processState', models.CharField(max_length=50)),
                ('sexCd', models.CharField(max_length=20)),
                ('neuterYn', models.CharField(max_length=20)),
                ('specialMark', models.CharField(max_length=200)),
                ('careNm', models.CharField(max_length=100)),
                ('careTel', models.CharField(max_length=100)),
                ('careAddr', models.CharField(max_length=100)),
                ('imageURL', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PetPlace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('tel', models.CharField(max_length=30)),
                ('url', models.CharField(max_length=200)),
                ('imageURL', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PetPlaceSlideImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slideimage', models.CharField(max_length=200)),
                ('petplace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slideimage', to='info.petplace')),
            ],
        ),
        migrations.CreateModel(
            name='PetPlaceBodyImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bodyimage', models.CharField(max_length=200)),
                ('petplace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bodyimage', to='info.petplace')),
            ],
        ),
    ]
