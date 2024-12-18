from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .forms import InscritoForm, InstitucionForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Inscrito, Institucion
from .serializer import InscritoSerializer, InstitucionSerializer

# Página principal con botones de navegación
def index(request):
    return render(request, 'index.html')

# Formulario para Inscripciones
def formulario_inscripciones(request):
    form = InscritoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_inscripciones')
    return render(request, 'formulario_inscripciones.html', {'form': form})

# Listar Inscripciones
def listar_inscripciones(request):
    inscritos = Inscrito.objects.all()
    return render(request, 'listar_inscripciones.html', {'inscritos': inscritos})

def editar_inscripcion(request, pk):
    inscrito = get_object_or_404(Inscrito, pk=pk)
    form = InscritoForm(request.POST or None, instance=inscrito)
    if form.is_valid():
        form.save()
        return redirect('listar_inscripciones')
    return render(request, 'formulario_inscripciones.html', {'form': form})


# Eliminar Inscripción
def eliminar_inscripcion(request, pk):
    inscrito = get_object_or_404(Inscrito, pk=pk)
    if request.method == 'POST':
        inscrito.delete()
        return redirect('listar_inscripciones')
    return render(request, 'confirmar_eliminar.html', {'objeto': inscrito, 'tipo': 'Inscripción'})

# Formulario para Instituciones
def formulario_instituciones(request):
    form = InstitucionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_instituciones')
    return render(request, 'formulario_instituciones.html', {'form': form})

# Listar Instituciones
def listar_instituciones(request):
    instituciones = Institucion.objects.all()
    return render(request, 'listar_instituciones.html', {'instituciones': instituciones})

# Editar Institución
def editar_institucion(request, pk):
    institucion = get_object_or_404(Institucion, pk=pk)
    form = InstitucionForm(request.POST or None, instance=institucion)
    if form.is_valid():
        form.save()
        return redirect('listar_instituciones')
    return render(request, 'formulario_instituciones.html', {'form': form})

# Eliminar Institución
def eliminar_institucion(request, pk):
    institucion = get_object_or_404(Institucion, pk=pk)
    if request.method == 'POST':
        institucion.delete()
        return redirect('listar_instituciones')
    return render(request, 'confirmar_eliminar.html', {'objeto': institucion, 'tipo': 'Institución'})

# Class-Based Views para Inscritos
class InscritosListCreateAPIView(ListCreateAPIView):
    queryset = Inscrito.objects.all()
    serializer_class = InscritoSerializer

class InscritosDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Inscrito.objects.all()
    serializer_class = InscritoSerializer

# Function-Based Views para Instituciones
@api_view(['GET', 'POST'])
def instituciones_list(request):
    if request.method == 'GET':
        instituciones = Institucion.objects.all()
        serializer = InstitucionSerializer(instituciones, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = InstitucionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def institucion_detail(request, pk):
    institucion = get_object_or_404(Institucion, pk=pk)
    if request.method == 'GET':
        serializer = InstitucionSerializer(institucion)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = InstitucionSerializer(institucion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        institucion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Datos del Autor
@api_view(['GET'])
def autor_info(request):
    autor_data = {
        "nombre": "Aaron",
        "email": "aaron.segura@inacapmail.cl",
        "proyecto": "Aaron_Segura_FINAL"
    }
    return Response(autor_data)

