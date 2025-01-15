from django import forms
from .models import Cliente, Tecnico, Producto, ParteTrabajo, DetalleParte

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'direccion', 'telefono', 'email']

class TecnicoForm(forms.ModelForm):
    class Meta:
        model = Tecnico
        fields = ['nombre', 'telefono']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'iva']

class ParteTrabajoForm(forms.ModelForm):
    fecha = forms.DateField(
        widget=forms.DateInput(attrs={'type':'date'}),
        input_formats=['%Y-%m-%d', '%d/%m/%Y', '%m/%d/%Y'],
    )
    class Meta:
        model = ParteTrabajo
        fields = ['fecha', 'cliente', 'tecnico', 'tiempo_empleado', 'observaciones']

class DetalleParteForm(forms.ModelForm):
    class Meta:
        model = DetalleParte
        fields = ['parte', 'producto', 'cantidad']
        widgets = {
            'parte': forms.HiddenInput(),
        }
