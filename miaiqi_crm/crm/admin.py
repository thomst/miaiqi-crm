from django.contrib import admin
from .models import Store, Contact, StoreType


@admin.register(StoreType)
class StoreTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'description')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'store')
    search_fields = ('name', 'email', 'phone', 'note')


class ContactInline(admin.TabularInline):
    model = Contact
    extra = 1
    fields = ('name', 'email', 'phone', 'note')
    show_change_link = True


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'status')
    search_fields = ('name', 'address', 'note')
    inlines = (ContactInline,)
