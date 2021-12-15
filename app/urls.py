from django.urls import path
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.contrib.auth.decorators import login_required

from.views import home,agregar_tarea,agregarProyecto,eliminarProyecto,listar_Tarea,modificar_Tareas,eliminar_Tareas\
    ,modificarProyecto,registro

urlpatterns = [
    path('', login_required(home),name="home"),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico'))),
    path('agregarProyecto/',agregarProyecto, name="agregar_proyecto"),
    path('eliminarProyecto/<id>',eliminarProyecto, name="eliminarProyecto"),
    path('modificarProyecto/<id>',modificarProyecto, name="modificarProyecto"),
    path('agregar_tarea/', agregar_tarea, name="agregar_tarea"),
    path('listar_Tarea/', listar_Tarea, name="listar_Tarea"),
    path('modificar_Tareas/<id>/', modificar_Tareas, name="modificar_Tareas"),
    path('eliminar_Tareas/<id>/',eliminar_Tareas,name="eliminar_Tareas"),
    path('registro/',registro, name ="registro"),

]
