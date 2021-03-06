from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import User, PermissionsMixin


class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        super_user = self.model(email=email, **extra_fields)
        super_user.set_password(password)
        super_user.save()

        return super_user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'is_staff', 'is_superuser']

    def get_full_name(self):
        return self.first_name

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email


class Author(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.name} | {self.company_name}"


class BookShelf(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Language(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Genres(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    title = models.CharField(max_length=200)
    isbn13 = models.CharField(max_length=17, blank=True, null=True)
    publicationDate = models.DateField(blank=True, null=True)
    availableQuantity = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    author = models.ManyToManyField(Author)
    language = models.ManyToManyField(Language)
    bookshelf = models.ManyToManyField(BookShelf)
    genres = models.ManyToManyField(Genres)
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    rating = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, upload_to='jpg')
    pdf = models.FileField(null=True, blank=True, upload_to='pdf')
    epub = models.FileField(null=True, blank=True, upload_to='epub')
    txt = models.FileField(null=True, blank=True, upload_to='txt')

    def __str__(self):
        return f"{self.title}"


class UserBooks(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    book = models.ManyToManyField(Book)


class Review(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    review = models.TextField(null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.rating)


class Order(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True)
    paymentMethod = models.CharField(max_length=200, blank=True, null=True)
    orderType = models.CharField(max_length=200, blank=True, null=True)
    taxPrice = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    totalPrice = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    paidAt = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    isPaid = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    discount = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return str(self.createdAt)


class OrderItem(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    quantity = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    image = models.URLField()

    def __str__(self):
        return str(self.name)


class Shipping(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    order = models.OneToOneField(Order, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    postalCode = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    ShippingPrice = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    isDelivered = models.BooleanField(default=False)
    deliveredAt = models.DateTimeField(auto_now_add=False, blank=True, null=True)

    def __str__(self):
        return self.address
