# Generated by Django 4.2.1 on 2023-05-19 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('garagem', '0005_rename_nome_modelo_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='acessorio',
            options={'verbose_name': 'acessório', 'verbose_name_plural': 'acessórios'},
        ),
        migrations.AlterModelOptions(
            name='cor',
            options={'verbose_name': 'Cor', 'verbose_name_plural': 'Cores'},
        ),
        migrations.RemoveField(
            model_name='veiculo',
            name='modelo',
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='ano',
            field=models.DateField(max_length=4),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='veiculos', to='garagem.categoria'),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='cor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='veiculos', to='garagem.cor'),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='veiculos', to='garagem.marca'),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='preco',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
    ]
