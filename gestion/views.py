from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente, Tecnico, Producto, ParteTrabajo, DetalleParte
from .forms import ClienteForm, TecnicoForm, ProductoForm, ParteTrabajoForm, DetalleParteForm
from django.db.models import Sum, F, FloatField
from django.contrib.auth.decorators import login_required

def index(request):
   # partes = ParteTrabajo.objects.all()
   # return render(request, 'gestion/index.html', {'partes': partes})
   @login_required
   def index(request):
    return render(request, 'gestion/index.html')

def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'gestion/cliente_list.html', {'clientes': clientes})

def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm()
    return render(request, 'gestion/cliente_form.html', {'form': form})

def cliente_update(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'gestion/cliente_form.html', {'form': form})

def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('cliente_list')
    return render(request, 'gestion/cliente_confirm_delete.html', {'cliente': cliente})
# Vistas para Técnicos
def tecnico_list(request):
    tecnicos = Tecnico.objects.all()
    return render(request, 'gestion/tecnico_list.html', {'tecnicos': tecnicos})

def tecnico_create(request):
    if request.method == 'POST':
        form = TecnicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tecnico_list')
    else:
        form = TecnicoForm()
    return render(request, 'gestion/tecnico_form.html', {'form': form})

def tecnico_update(request, pk):
    tecnico = get_object_or_404(Tecnico, pk=pk)
    if request.method == 'POST':
        form = TecnicoForm(request.POST, instance=tecnico)
        if form.is_valid():
            form.save()
            return redirect('tecnico_list')
    else:
        form = TecnicoForm(instance=tecnico)
    return render(request, 'gestion/tecnico_form.html', {'form': form})

def tecnico_delete(request, pk):
    tecnico = get_object_or_404(Tecnico, pk=pk)
    if request.method == 'POST':
        tecnico.delete()
        return redirect('tecnico_list')
    return render(request, 'gestion/tecnico_confirm_delete.html', {'tecnico': tecnico})


# Vistas para Productos
def producto_list(request):
    productos = Producto.objects.all()
    return render(request, 'gestion/producto_list.html', {'productos': productos})

def producto_create(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm()
    return render(request, 'gestion/producto_form.html', {'form': form})

def producto_update(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'gestion/producto_form.html', {'form': form})

def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('producto_list')
    return render(request, 'gestion/producto_confirm_delete.html', {'producto': producto})


# Vistas para Partes de Trabajo
def parte_list(request):
    partes = ParteTrabajo.objects.all()
    return render(request, 'gestion/parte_list.html', {'partes': partes})

def parte_create(request):
    if request.method == 'POST':
        form = ParteTrabajoForm(request.POST)
        if form.is_valid():
            parte = form.save()
            return redirect('parte_list')
    else:
        form = ParteTrabajoForm()

    return render(request, 'gestion/parte_form.html', {
        'form': form,
        'parte': None,
        'detalles': [],
        'total_materiales': 0,
        })


def parte_update(request, pk):
    parte = get_object_or_404(ParteTrabajo, pk=pk)
    detalles = DetalleParte.objects.filter(parte=parte)


    # Calcular el subtotal para cada detalle y el total general
    for detalle in detalles:
        detalle.subtotal = detalle.cantidad * detalle.producto.precio

    total_materiales = detalles.aggregate(
        total=Sum(F('cantidad') * F('producto__precio'), output_field=FloatField())
    )['total'] or 0


    if request.method == 'POST':
        form = ParteTrabajoForm(request.POST, instance=parte)
        if form.is_valid():
            form.save()
            return redirect('parte_list')
    else:
        form = ParteTrabajoForm(instance=parte)
    return render(request, 'gestion/parte_form.html', {
        'form': form,
        'parte': parte,
        'detalles': detalles,
        'total_materiales': total_materiales,
        })

def parte_delete(request, pk):
    parte = get_object_or_404(ParteTrabajo, pk=pk)
    if request.method == 'POST':
        parte.delete()
        return redirect('parte_list')
    return render(request, 'gestion/parte_confirm_delete.html', {'parte': parte})

# Vistas para DetalleParte
def detalleparte_list(request):
    detalles = DetalleParte.objects.all()
    return render(request, 'gestion/detalleparte_list.html', {'detalles': detalles})

def detalleparte_create(request):
    if request.method == 'POST':
        form = DetalleParteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('detalleparte_list')
    else:
        form = DetalleParteForm()
    return render(request, 'gestion/detalleparte_form.html', {'form': form})

def detalleparte_update(request, pk):
    detalle = get_object_or_404(DetalleParte, pk=pk)
    if request.method == 'POST':
        form = DetalleParteForm(request.POST, instance=detalle)
        if form.is_valid():
            form.save()
            return redirect('detalleparte_list')
    else:
        form = DetalleParteForm(instance=detalle)
    return render(request, 'gestion/detalleparte_form.html', {'form': form})

def detalleparte_delete(request, pk):
    detalle = get_object_or_404(DetalleParte, pk=pk)
    parte_id = detalle.parte.id

    if request.method == 'POST':
        detalle.delete()
        return redirect('parte_update', pk=parte_id)
    
    return render(request, 'gestion/detalleparte_confirm_delete.html', {'detalle': detalle})

def detalleparte_add(request, parte_id):
    parte = get_object_or_404(ParteTrabajo, id=parte_id)
    if request.method == 'POST':
        form = DetalleParteForm(request.POST)
        if form.is_valid():
            detalle = form.save(commit=False)
            detalle.parte = parte
            detalle.save()
            return redirect('parte_update', pk=parte.id)
    else:
        form = DetalleParteForm(initial={'parte': parte})
    return render(request, 'gestion/detalleparte_form.html', {'form': form, 'parte': parte})
