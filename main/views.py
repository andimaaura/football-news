from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406409076',
        'name': 'Andi Maura Azzahra',
        'class': 'PBP c'
    }

    return render(request, "main.html", context)

