from django.contrib import admin
from .models import Brand, CartItem, Category, Product
# Register your models here.

#admin.site.register(Brand)

class BrandAdmin(admin.ModelAdmin):
    list_display = ["name",]
    search_fields = ["name",]
    # list_filter = ["brand",]
    # readonly_fields = ["quantity",]
    class Meta:
        model = Brand

admin.site.register(Brand, BrandAdmin)

# admin.site.register(Category)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name",]
    search_fields = ["name",]
    # list_filter = ["category",]
    # readonly_fields = ["quantity",]
    
    class Meta:
        model = Category

admin.site.register(Category, CategoryAdmin)




# admin.site.register(Product)

class ProductAdmin(admin.ModelAdmin):
    list_display = ["image_tag", "name", "price", "brand", "category",]
    search_fields = ["name", "price", "brand__name", "category__name",]
    list_filter = ["brand", "category",]
    #readonly_fields = ["quantity",]

    class Meta:
        model = Product
        
admin.site.register(Product, ProductAdmin)

#TODO: for cartItem
admin.site.register(CartItem)