from django.shortcuts import render,redirect
from bookspdf.models import Potterheads
# Create your views here.
def join(request):
    

    if request.method=="POST":
        fname=request.POST['name']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if pass1==pass2:
            hpuser=Potterheads(name=fname,emailid=email,password=pass2)
            hpuser.save()
            
            return redirect('login')
        else:
            return render(request,'join.html')
            
        

    return render(request,'join.html')

def login(request):
    
    if request.method=="POST":
        EMAIL=request.POST['email']
        passw=request.POST['password3']
        post=Potterheads.objects.get(emailid=EMAIL)
        a=post.password
        if passw==a:
            return render(request, 'hpb.html')
        else:
            blog="WRONG PASSWORD"
            return render(request, "login.html", {'blog': blog})
        
    
    return render(request, 'login.html')
        
        

    

def hpb(request):

    return render(request,'hpb.html')