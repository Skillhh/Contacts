from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'status':'Working on the project'
    }
    return render(request, 'index.html', context)
    
