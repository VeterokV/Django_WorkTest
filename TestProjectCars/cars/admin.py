from django.contrib import admin
from .models import Car, Comment


class CarAdmin(admin.ModelAdmin):
    readonly_fields = ('updated_at', 'created_at')                                                                      # Отображение дат записи в админ-панели


admin.site.register(Car, CarAdmin)
admin.site.register(Comment)
