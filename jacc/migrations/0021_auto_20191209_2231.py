# Generated by Django 2.2.8 on 2019-12-09 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jacc', '0020_auto_20191202_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountentry',
            name='settled_invoice',
            field=models.ForeignKey(blank=True, default=None, help_text='entry.settled.invoice.help.text', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='jacc.Invoice', verbose_name='settled invoice'),
        ),
        migrations.AlterField(
            model_name='accountentry',
            name='settled_item',
            field=models.ForeignKey(blank=True, default=None, help_text='entry.settled.item.help.text', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='settlement_set', to='jacc.AccountEntry', verbose_name='settled item'),
        ),
        migrations.AlterField(
            model_name='accountentry',
            name='source_file',
            field=models.ForeignKey(blank=True, default=None, help_text='entry.source.file.help.text', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='jacc.AccountEntrySourceFile', verbose_name='account entry source file'),
        ),
        migrations.AlterField(
            model_name='accountentry',
            name='source_invoice',
            field=models.ForeignKey(blank=True, default=None, help_text='entry.source.invoice.help.text', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='jacc.Invoice', verbose_name='source invoice'),
        ),
    ]