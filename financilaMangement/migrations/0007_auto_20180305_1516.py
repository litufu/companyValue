# Generated by Django 2.0.2 on 2018-03-05 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financilaMangement', '0006_auto_20180304_2206'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='companylist',
            options={'verbose_name': '公司列表', 'verbose_name_plural': '公司列表清单'},
        ),
        migrations.AlterModelOptions(
            name='reporttype',
            options={'verbose_name': '报表类型', 'verbose_name_plural': '报表类型清单'},
        ),
    ]
