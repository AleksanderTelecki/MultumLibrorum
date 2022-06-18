# Generated by Django 4.0.5 on 2022-06-18 21:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('company_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('isbn13', models.CharField(blank=True, max_length=17, null=True)),
                ('publicationDate', models.DateField(blank=True, null=True)),
                ('availableQuantity', models.IntegerField(blank=True, default=0, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('numReviews', models.IntegerField(blank=True, default=0, null=True)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='jpg')),
                ('pdf', models.FileField(blank=True, null=True, upload_to='pdf')),
                ('epub', models.FileField(blank=True, null=True, upload_to='epub')),
                ('txt', models.FileField(blank=True, null=True, upload_to='txt')),
                ('author', models.ManyToManyField(to='api.author')),
            ],
        ),
        migrations.CreateModel(
            name='BookShelf',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('paymentMethod', models.CharField(blank=True, max_length=200, null=True)),
                ('orderType', models.CharField(blank=True, max_length=200, null=True)),
                ('taxPrice', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('totalPrice', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('paidAt', models.DateTimeField(blank=True, null=True)),
                ('isPaid', models.BooleanField(default=False)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserBooks',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('book', models.ManyToManyField(to='api.book')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('postalCode', models.CharField(blank=True, max_length=200, null=True)),
                ('country', models.CharField(blank=True, max_length=200, null=True)),
                ('ShippingPrice', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('isDelivered', models.BooleanField(default=False)),
                ('deliveredAt', models.DateTimeField(blank=True, null=True)),
                ('order', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.order')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('review', models.TextField(blank=True, null=True)),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.book')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('image', models.URLField()),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.book')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.order')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='bookshelf',
            field=models.ManyToManyField(to='api.bookshelf'),
        ),
        migrations.AddField(
            model_name='book',
            name='genres',
            field=models.ManyToManyField(to='api.genres'),
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ManyToManyField(to='api.language'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.publisher'),
        ),
    ]
