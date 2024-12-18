from django import forms
from .models import Inscrito, Institucion

# Formulario para Inscrito
class InscritoForm(forms.ModelForm):
    class Meta:
        model = Inscrito
        fields = ['nombre', 'email', 'telefono', 'nro_personas', 'institucion', 'estado', 'observacion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre completo'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
            'nro_personas': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Número de personas'}),
            'institucion': forms.Select(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'observacion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Observaciones'}),
        }

    def clean_nro_personas(self):
        nro_personas = self.cleaned_data.get('nro_personas')
        if nro_personas is None:
            raise forms.ValidationError("Este campo es obligatorio.")
        
        try:
            # Convertir a entero
            nro_personas = int(nro_personas)
        except ValueError:
            raise forms.ValidationError("El número de personas debe ser un número entero.")
        
        if not (1 <= nro_personas <= 30):
            raise forms.ValidationError("El número de personas debe estar entre 1 y 30 maximo.")
        
        return nro_personas

    def clean_institucion(self):
        institucion = self.cleaned_data.get('institucion')
        if institucion is None:
            raise forms.ValidationError("Debes seleccionar una institución.")
        if len(institucion.nombre) > 80:  # Validación de longitud del nombre de la institución
            raise forms.ValidationError("El nombre de la institución no puede superar los 80 caracteres.")
        return institucion

# Formulario para Institución
class InstitucionForm(forms.ModelForm):
    class Meta:
        model = Institucion
        fields = ['nombre', 'direccion', 'telefono']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la institución'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if nombre and len(nombre) > 80:
            raise forms.ValidationError("El nombre no puede tener más de 80 caracteres.")
        return nombre