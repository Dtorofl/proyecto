from django.contrib import admin
from .models import Proyecto,Tarea 

# Register your models here.

class TareaAmin(admin.ModelAdmin):
    list_display = ["id","nombre", "descripcion","codigo", "fecha", "estado"]
admin.site.register(Proyecto)
admin.site.register(Tarea,TareaAmin)