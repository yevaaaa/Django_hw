from django.contrib import admin
from .models import Human



@admin.register(Human)
class HumanAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'age')

    def age(self, obj):
        z = 2021 - obj.year_of_birth
        return str(z)

    age.short_description = 'age'
