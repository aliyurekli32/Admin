from django.contrib import admin
from django.utils import timezone

# Register your models here.
from .models import Product,Review,Category

class ReviewInline(admin.TabularInline):  # StackedInline farklı bir görünüm aynı iş
    '''Tabular Inline View for '''
    model = Review
    extra = 2
    classes = ('collapse',)
    # min_num = 3
    # max_num = 20




class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "create_date", "is_in_stock", "update_date","added_days_ago","how_many_reviews")
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
            "fields" : ("description","categories"), #only editable ones can be choosen
            'description' : "You can use this section for optionals settings"
        })
    )
    filter_horizontal = ("categories", )
    inlines = (ReviewInline,)
    
    
    actions = ("is_in_stock", )
    def is_in_stock(self, request, queryset):
        count = queryset.update(is_in_stock=True,)
        self.message_user(request, f"{count} çeşit ürün stoğa eklendi")
    
    is_in_stock.short_description = 'İşaretlenen ürünleri stoğa ekle'
    
    def added_days_ago(self, product):
        fark = timezone.now() - product.create_date
        return fark.days


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created_date', 'is_released')
    list_per_page = 50
    raw_id_fields = ('product',)


admin.site.register(Product,ProductAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Category)

admin.site.site_title = "Clarusway Title"
admin.site.site_header = "Clarusway Admin Portal"  
admin.site.index_title = "Welcome to Clarusway Admin Portal"

