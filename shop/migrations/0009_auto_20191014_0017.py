# Generated by Django 2.2.6 on 2019-10-13 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_merge_20191013_2313'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=200),
        ),
    ]