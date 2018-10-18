from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Articolo

from django.contrib.auth import authenticate, login

#Mostro gli articoli piu' recenti (ultimi 10)
def main(request):
    ultimi_articoli = Articolo.objects.order_by('-data', 'titolo')[:10]
    
    return render(request, 'blog/ultimi_articoli.html',
                { 'ultimi_articoli': 'articoli'},
                content_type='application/xhtml+xml')

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.





