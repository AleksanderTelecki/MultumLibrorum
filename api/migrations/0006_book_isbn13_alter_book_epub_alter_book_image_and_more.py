# Generated by Django 4.0.4 on 2022-05-07 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_book_epub_alter_book_pdf_alter_book_txt'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='isbn13',
            field=models.CharField(blank=True, max_length=17, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='epub',
            field=models.FileField(blank=True, null=True, upload_to='epub'),
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='jpg'),
        ),
        migrations.AlterField(
            model_name='book',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='pdf'),
        ),
        migrations.AlterField(
            model_name='book',
            name='txt',
            field=models.FileField(blank=True, null=True, upload_to='txt'),
        ),
    ]