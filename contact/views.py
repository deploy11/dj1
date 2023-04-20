from django.shortcuts import render,redirect
from .models import Contact

# Create your views here.
def home2(request):
    if request.method == 'POST':
        Contact.objects.create(
            email = request.POST['email'],
            text = request.POST['text'],
            name = request.POST['name'],
            subject = request.POST['subject']
        )
        return redirect('home')
    return render(request,'contact.html')