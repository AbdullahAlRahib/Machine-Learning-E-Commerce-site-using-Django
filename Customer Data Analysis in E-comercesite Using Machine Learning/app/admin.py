from audioop import reverse
from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import (
    Customer,
    Product,
    Cart,
    UserProfile,
    OrderPlaced,
    DataTable
)
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'locality', 'city', 'zipcode', 'state']
    
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'selling_price', 'discounted_price', 'description',
                    'brand', 'category', 'product_image']
    
@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity']
    



#work for profile value submit
@admin.register(UserProfile)
class UserProfileModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'fullname', 'age', 'location', 'phone_num', 'gender', 'marital', 'interest']





@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'customer', 'userprofile', 'customer_info', 'product_info', 'product', 'quantity', 'ordered_date', 'status']

    def customer_info(self, obj):
        link = reverse("admin:app_customer_change", args=[obj.customer.pk])
        return format_html('<a href="{}">{}</a>', link, obj.customer.name)

    def userprofile_info(self, obj):
        link = reverse("admin:app_userprofile_change", args=[obj.userprofile.pk])
        return format_html('<a href="{}">{}</a>', link, obj.userprofile.fullname)

    def product_info(self, obj):
        link = reverse("admin:app_product_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.title)








#rahib query start from here-
@admin.register(DataTable)
class DataTableModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'gender']
