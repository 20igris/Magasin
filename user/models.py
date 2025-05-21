from django.db import models

class Role(models.Model):
    role_name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.role_name


class User(models.Model):
    firstname = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # à sécuriser plus tard
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    role = models.ForeignKey(Role, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Category(models.Model):
    cat_name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cat_name


class Product(models.Model):
    pro_name = models.CharField(max_length=45)
    pro_price = models.IntegerField()
    pro_desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.pro_name


class Sale(models.Model):
    sale_code = models.CharField(max_length=45, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.sale_code


class Bill(models.Model):
    qty = models.IntegerField()
    bill_code = models.CharField(max_length=45, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    prix_vente = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return self.bill_code


class PayMethod(models.Model):
    pay_name = models.CharField(max_length=45, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.pay_name


class Payment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_up = models.DateTimeField(auto_now=True)
    paymethod = models.ForeignKey(PayMethod, on_delete=models.PROTECT)
    sale = models.ForeignKey(Sale, on_delete=models.PROTECT)

    def __str__(self):
        return f"Payment #{self.id}"
