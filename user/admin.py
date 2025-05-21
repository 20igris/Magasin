from django.contrib import admin
from .models import Role, User, Category, Product, Sale, Bill, PayMethod, Payment

# Enregistrer les modèles simples sans customisation
admin.site.register(Role)
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Sale)
admin.site.register(Bill)
admin.site.register(PayMethod)
admin.site.register(Payment)