from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306245075',
        'name': 'Affandi Shafwan Soleh',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)