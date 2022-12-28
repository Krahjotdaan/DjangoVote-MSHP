from django.shortcuts import render

def index(request):
    context = {
        'message': 'if u read it, u will lose your brain very soon'
    }
    return render(request, 'index.html', context)
