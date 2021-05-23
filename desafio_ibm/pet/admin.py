from django.contrib import admin

from .models import Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ["name", "race", "age", "weight", "city", ]
    search_fields = ["name", "race", "city"]
    list_filter = ["city__name", "age", "race"]
