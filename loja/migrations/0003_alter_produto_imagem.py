# Generated by Django 5.1.2 on 2024-10-17 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0002_alter_produto_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
