from django.shortcuts import render

def show_main(request):
    context = {
        'title': 'Solcaster United',
        'npm' : '2406496233',
        'name': 'Razan Muhammad Salim',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)