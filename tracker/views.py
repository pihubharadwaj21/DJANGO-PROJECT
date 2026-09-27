from django.shortcuts import render, redirect
from .models import Period


def home(request):
    periods = Period.objects.all().order_by('-start_date')

    return render(request, 'tracker/home.html', {
        'periods': periods
    })


def add_period(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        notes = request.POST.get('notes')

        Period.objects.create(
            name=name,
            start_date=start_date,
            end_date=end_date,
            notes=notes
        )

        return redirect('home')

    return render(request, 'tracker/add_period.html')