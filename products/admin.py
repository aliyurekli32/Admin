from django.contrib import admin
import datetime

# Register your models here.
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "create_date", "is_in_stock", "update_date")
    list_editable = ( "is_in_stock", )
    list_display_links = ("name", )
    list_filter = ("is_in_stock", "create_date")
    ordering = ("name","update_date")
    search_fields = ("name",)
    prepopulated_fields = {'slug' : ('name',)}
    list_per_page = 25
    date_hierarchy = "update_date"
    # fields = (('name', 'slug'), 'description', "is_in_stock")
    fieldsets = (
        (None, {
            "fields": (
                ('name', 'slug'), "is_in_stock" # to display multiple fields on the same line, wrap those fields in their own tuple
            ),
            # 'classes': ('wide', 'extrapretty'), wide or collapse
        }),
        ('Optionals Settings', {
            "classes" : ("collapse", ), #collapse or wide
            "fields" : ("description",), #only editable ones can be choosen
            'description' : "You can use this section for optionals settings"
        })
    )
    
    actions = ("is_in_stock", )
    def is_in_stock(self, request, queryset):
        count = queryset.update(is_in_stock=True,)
        self.message_user(request, f"{count} çeşit ürün stoğa eklendi")
    
    is_in_stock.short_description = 'İşaretlenen ürünleri stoğa ekle'
    
    
admin.site.register(Product,ProductAdmin)

admin.site.site_title = "Clarusway Title"
admin.site.site_header = "Clarusway Admin Portal"  
admin.site.index_title = "Welcome to Clarusway Admin Portal"

