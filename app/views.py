from django.shortcuts import render,redirect,get_object_or_404
from .models import Tarea,Proyecto
from .forms import TareaForm,ProyectoForm,CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required



def home(request):
    proyectos = Proyecto.objects.all()
    data={
        'proyectos':proyectos 
    }
    
    return render(request,'app/home.html',data)




def agregarProyecto(request):
    nombre = request.POST['txtNombre']
    
    
    adicion = Proyecto.objects.create(nombre=nombre)

    return redirect('/') 
def eliminarProyecto(request,id):
    proyectos = Proyecto.objects.get(id=id)
    proyectos.delete()
    return redirect('/')

def modificarProyecto(request,id):
    proyecto = get_object_or_404(Proyecto, id=id)

    data = {
        'form': ProyectoForm(instance=proyecto)
    }
    if request.method == 'POST':
        formulario = ProyectoForm(data=request.POST, instance = proyecto)
        if formulario.is_valid():
            formulario.save()
            return redirect(to ="home")
        data["form"]=formulario
    
    return render(request,'app/proyectos/edicionProyecto.html',data)
    

def listar_Tarea(request):
    tareas = Tarea.objects.all() 
    data ={
        'tareas': tareas
    }
    return render(request,'app/tareas/listar.html',data)

def modificar_Tareas(request,id):
    tarea = get_object_or_404(Tarea, id=id)

    data = {
        'form': TareaForm(instance=tarea)
    }
    if request.method == 'POST':
        formulario = TareaForm(data=request.POST, instance = tarea,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to ="listar_Tarea")
        data["form"]=formulario
    
    return render(request,'app/tareas/editar.html',data)

def eliminar_Tareas(request, id):
    tarea = get_object_or_404(Tarea,id=id)
    tarea.delete()
    return redirect(to ='listar_Tarea')

def agregar_tarea(request):
    data = {
        'form': TareaForm()
    }
    if request.method == 'POST':
        formulario =TareaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado correctamente"
            return redirect(to ="listar_Tarea")
            

    return render(request,'app/tareas/agregar.html',data)


def registro(request):
    data={
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user= authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request,user)
            
            return redirect(to="home")
        data["form"] = formulario

    return render(request,'registration/registro.html',data)
