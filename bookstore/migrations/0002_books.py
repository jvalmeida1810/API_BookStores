# Generated by Django 5.0.6 on 2024-05-12 13:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
        ('bookstore', '0001_initial'),
        ('editorial', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('ISBN', models.CharField(max_length=32)),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('authors', models.ManyToManyField(related_name='books_authors', to='author.author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='books_category', to='bookstore.category')),
                ('publishing_company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='books_company', to='editorial.editorial')),
            ],
            options={
                'verbose_name_plural': 'Books',
            },
        ),
    ]
