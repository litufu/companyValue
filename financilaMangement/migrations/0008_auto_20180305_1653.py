# Generated by Django 2.0.2 on 2018-03-05 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('financilaMangement', '0007_auto_20180305_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balancesheet',
            name='stk_cd',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financilaMangement.CompanyList', verbose_name='股票代码'),
        ),
        migrations.AlterField(
            model_name='balancesheet',
            name='typ_rep',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financilaMangement.ReportType', verbose_name='报表类型'),
        ),
    ]
