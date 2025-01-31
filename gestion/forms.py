from django import forms
from .models import Cliente, Tecnico, Producto, ParteTrabajo, DetalleParte

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'direccion', 'telefono', 'email']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.Textarea(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class TecnicoForm(forms.ModelForm):
    class Meta:
        model = Tecnico
        fields = ['nombre', 'telefono']
        widgets = {
          'nombre': forms.TextInput(attrs={'class': 'form-control'}),           
          'telefono': forms.TextInput(attrs={'class': 'form-control'}),      
        }

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'iva']

class ParteTrabajoForm(forms.ModelForm):
    fecha = forms.DateField(
        'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        input_formats=['%Y-%m-%d', '%d/%m/%Y', '%m/%d/%Y'],
    )
    class Meta:
        model = ParteTrabajo
        fields = ['fecha', 'cliente', 'tecnico', 'tiempo_empleado', 'observaciones']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),  # Ajusta 'rows' según necesidad     
        }
        def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tecnico'] = forms.ModelChoiceField(
            queryset=Tecnico.objects.all(),
            empty_label="Selecciona un tecnico", # Texto para la opción vacía
            label="Tecnico", # Sobreescribe la etiqueta del campo si es necesario
            widget=forms.Select(attrs={'class': 'form-control'}) # Añade una clase CSS de Bootstrap
        )
        self.fields['cliente'] = forms.ModelChoiceField(
            queryset=Cliente.objects.all(),
            empty_label="Selecciona un cliente",
            label="Cliente",
            widget=forms.Select(attrs={'class': 'form-control'})
        )

class DetalleParteForm(forms.ModelForm):
    class Meta:
        model = DetalleParte
        fields = ['parte', 'producto', 'cantidad']
        widgets = {
            'parte': forms.HiddenInput(),
        }
