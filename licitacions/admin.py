from django.contrib import admin

from .models import Contractant


@admin.register(Contractant)
class ContractantAdmin(admin.ModelAdmin):
    list_display = ('codi', 'nom', 'descartat', )
    list_display_links = ('codi', 'nom')
    search_fields = ('=codi', 'nom')
    list_filters = ('descartat')
