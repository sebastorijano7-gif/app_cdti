from django.shortcuts import render, get_object_or_404, redirect
from .models import Equipo, Prestamo

def lista_equipos(request):
    equipos = Equipo.objects.all()
    return render(request, 'cdti_app/lista_equipos.html', {'equipos': equipos})

def prestar_equipo(request):
    error = None
    if request.method == 'POST':
        serial_form = request.POST.get('serial')
        documento_form = request.POST.get('documento')
        ambiente_form = request.POST.get('ambiente')

        try:
            equipo = Equipo.objects.get(serial=serial_form, estado='Disponible')
            
            Prestamo.objects.create(
                equipo=equipo,
                documento_aprendiz=documento_form,
                ambiente=ambiente_form
            )
            
            equipo.estado = 'Prestado'
            equipo.save()

            return redirect('detalle_equipo', id=equipo.id)

        except Equipo.DoesNotExist:
            error = "El equipo no existe o ya se encuentra prestado."

    equipos_disponibles = Equipo.objects.filter(estado='Disponible')
    return render(request, 'cdti_app/prestar_equipo.html', {
        'equipos_disponibles': equipos_disponibles,
        'error': error
    })

def detalle_equipo(request, id):
    equipo = get_object_or_404(Equipo, id=id)
    ultimo_prestamo = equipo.prestamos.order_by('-fecha_prestamo').first()
    return render(request, 'cdti_app/detalle_equipo.html', {
        'equipo': equipo,
        'ultimo_prestamo': ultimo_prestamo
    })