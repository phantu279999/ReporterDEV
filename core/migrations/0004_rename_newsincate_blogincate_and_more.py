# Generated by Django 5.1.4 on 2025-01-04 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_category_blog_newsincate'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NewsInCate',
            new_name='BlogInCate',
        ),
        migrations.AddConstraint(
            model_name='newsinzone',
            constraint=models.UniqueConstraint(fields=('zone', 'news'), name='unique_zone_news'),
        ),
        migrations.AddConstraint(
            model_name='tagnews',
            constraint=models.UniqueConstraint(fields=('tag', 'news'), name='unique_tag_news'),
        ),
    ]
