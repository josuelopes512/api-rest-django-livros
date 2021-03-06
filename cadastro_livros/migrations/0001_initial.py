# Generated by Django 3.2.5 on 2021-07-21 05:13

from django.db import migrations, models
import isbn_field.fields
import isbn_field.validators
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id_livro', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('autor', models.CharField(max_length=255)),
                ('isbn', isbn_field.fields.ISBNField(clean_isbn=False, max_length=28, validators=[isbn_field.validators.ISBNValidator], verbose_name='ISBN')),
                ('data_de_lancamento', models.DateField()),
                ('estado', models.CharField(choices=[('1', 'Ativo'), ('2', 'Não Ativo')], default='Ativo', max_length=6)),
                ('paginas', models.PositiveIntegerField()),
                ('empresa_publicadora', models.CharField(max_length=255)),
                ('create_at', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-create_at',),
            },
        ),
    ]
