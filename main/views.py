from django.shortcuts import render
from main.models import Main

# Create your views here.
def main(requset):
    main = Main.objects.all()
    return render(requset, 'index.html', locals())


