from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
# Create your views here.


def home(request):
    return render(request,'payment/home.html')

def donate(request):
    name = request.POST.get('name', 'none')
    email = request.POST.get('email', 'none')
    number = request.POST.get('number', 'none')
    ammount = request.POST.get('ammount', 'none')

    dict={'ammount':ammount}

    if request.method=="POST" and name!='' and email!='' and number!='' and ammount!='':
        print(name,email,number,ammount)
        send_mail('Kind Donation', f'Thankyou {name}, you have successfully donated {ammount}$',
                  'sdsoumyadey2910@gmail.com', [email], fail_silently=True)
        return render(request,'payment/donation.html',dict)
    else:
        return HttpResponse('error')


