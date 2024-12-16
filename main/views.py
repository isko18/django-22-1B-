from django.shortcuts import render

# Create your views here.
def main(requset):
    context = {
        'head': "Geeks",
        'title': "Привет Geeks",
        'description': 'Время'
    }
    return render(requset, 'index.html', context=context)


