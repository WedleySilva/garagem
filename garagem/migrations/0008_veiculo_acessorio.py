# Generated by Django 4.2.2 on 2023-06-06 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garagem', '0007_remove_veiculo_nome_veiculo_modelo'),
    ]

    operations = [
        migrations.AddField(
            model_name='veiculo',
            name='acessorio',
            field=models.ManyToManyField(related_name='veiculos', to='garagem.acessorio'),
        ),
    ]
