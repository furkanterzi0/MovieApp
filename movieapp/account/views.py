from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

def AccountLogin(request):

    if request.user.is_authenticated:
        return redirect("home")
    
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            errorMessage="username ya da parola yanlis"
            return render(request,"login.html",{
                "errorMessage":"username or password invalid"
            })    

    return render(request,"login.html")

def AccountRegister(request):
    
    if request.user.is_authenticated:
        return redirect("home")
    
    if request.method=="POST":
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]
        confirm_password=request.POST["confirm_password"]
        
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                return render(request,"register.html",{"errorMessage":"usarname already using"})
                                             
            else:
                if User.objects.filter(email=email).exists():
                     return render(request,"register.html",{"errorMessage":"usarname already using"})
                else:
                    user=User.objects.create_user(first_name=first_name, last_name=last_name, username=username, password=password, email=email)
                    user.save()
                    return redirect("AccountLogin")
        else:
            return render(request,"register.html",{"errorMessage":"parolalar eşleşmiyo"})


    return render(request,"register.html")



def AccountLogout(request):
    logout(request)
    return redirect("home")