from django.shortcuts import render, redirect
from .models import Ubicacion,Contacto,Empresa,Dueño
from NewApp.forms import UbicacionForm, ContactoForm, EmpresaForm, DueñoForm
from django.contrib import messages

def inicio(request):
    return render (request, "NewApp/inicio.html")

def registrar_formulario(request):
    if request.method == 'POST':
        try:
            # Guardar Dueño
            dueño = Dueño(nombre=request.POST['nombre'], apellido=request.POST['apellido'])
            dueño.save()
            
            # Guardar Empresa
            empresa = Empresa(
                razon_social=request.POST['razon_social'],
                cuil=request.POST['cuil'],
                nombre_de_fantasia=request.POST['nombre_de_fantasia'],
                actividad_comercial=request.POST['actividad_comercial']
            )
            empresa.save()
            
            # Guardar Ubicación
            ubicacion = Ubicacion(
                direccion=request.POST['direccion'],
                localidad=request.POST['localidad'],
                ciudad=request.POST['ciudad'],
                pais=request.POST['pais']
            )
            ubicacion.save()
            
            # Guardar Contacto
            contacto = Contacto(
                Tel=request.POST['Tel'],
                email=request.POST['email'],
                Tel_alternativo=request.POST['Tel_alternativo']
            )
            contacto.save()
            
            messages.success(request, 'Todos los datos fueron registrados exitosamente.')
            return redirect('fin')
        
        except Exception as e:
            messages.error(request, f'Error al registrar los datos: {e}')
            return render(request, 'NewApp/registros/registrar_formulario.html')
    
    return render(request, 'NewApp/registros/registrar_formulario.html')

def buscar_empresas(request):
    query = request.GET.get('q', '')
    empresas = []
    if query:
        empresas = Empresa.objects.filter(nombre_de_fantasia__icontains=query)
    return render(request, "NewApp/inicio.html", {'empresas': empresas, 'query': query})

def fin(request):
    return render(request, "NewApp/registros/fin.html")
