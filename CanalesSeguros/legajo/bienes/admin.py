from django.contrib import admin
from .models import Motorizados, Accesorio
# Register your models here.


class AccesoriosInline(admin.StackedInline):
    model = Accesorio


class MotorizadosAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    inlines = [
        AccesoriosInline,
    ]
    exclude = ['usuario_bien']

    def save_model(self, request, obj, form, change):
        obj.usuario_bien = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Motorizados, MotorizadosAdmin)
