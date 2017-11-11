from django.contrib import admin
from .models import Catagory, Wine, Company, WineInstance

admin.site.site_header = "Grape Administrator"
admin.site.site_title = "Grape Site Administrator"
#admin.site.register(Wine)
#admin.site.register(Catagory)
#admin.site.register(WineInstance)
#admin.site.register(Company)
class WineInline(admin.TabularInline):
	model = Wine
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'established_date')
    fields = ['company_name', ('established_date')]
    inlines = [WineInline]
# Register the admin class with the associated model
admin.site.register(Company, CompanyAdmin)

class WineInstanceInline(admin.TabularInline):
    model = WineInstance
# Register the Admin classes for wine using the decorator
@admin.register(Wine)
class WineAdmin(admin.ModelAdmin):
    list_display = ('Brand_name', 'company_name', 'display_catagory')
    inlines = [WineInstanceInline]
# Register the Admin classes for wineInstance using the decorator
@admin.register(WineInstance)
class WineInstanceAdmin(admin.ModelAdmin):
	list_filter = ('wine_type', 'wine')
	list_display = ('wine', 'wine_type', 'id')
	fieldsets = (
        (None, {
            'fields': ('wine','wine_type', 'id')
        }),
        ('Availability', {
            'fields': (['status'])
        }),
    )

@admin.register(Catagory)
class CatagoryAdmin(admin.ModelAdmin):
	list_display = (['type_name'])

