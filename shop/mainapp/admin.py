from django import forms
from django.contrib import admin
# Register your models here.
from .models import *


class NotebookCategoryChoiceField(forms.ModelChoiceField):
    pass

class NotebookAdmin(admin.ModelAdmin):
    def formfield_for_choice_field(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return NotebookCategoryChoiceField(Category.objects.filter(slug='notebooks'))
        return super().formfield_for_foreignkey(db_field,request,**kwargs)

admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(NotebookProduct, NotebookAdmin)
admin.site.register(CartProduct)
admin.site.register(Customer)