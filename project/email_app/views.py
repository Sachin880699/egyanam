from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from time import gmtime, strftime
from django.core.mail import EmailMessage

def home(request):
    if request.method == 'POST':
        ip_address = request.POST.get("ip_address")
        email = request.POST.get("email")
        try:
            user = auth.authenticate(username=request.POST['email'], password=request.POST['password'])
            if user:
                file = open("log/log.txt", 'a')
                file.write("\n"+"Date Time  ==>>"+ strftime("%Y-%m-%d %H:%M:%S", gmtime())+"\n")
                file.write("Email      ==>>"+ email+"\n")
                file.write("IP Address ==>>"+ ip_address+"\n")
                file.write("Login Status ==>>"+ "Login Sucess"+"\n")
                file.write("________________________________________")
                file.close()
            else:
                if request.session.get("temp",0) > 0:
                    request.session['temp'] = int(request.session["temp"])+1
                    request_count = request.session['temp']
                else:
                    request_count = request.session["temp"]=1
                if request_count > 3:
                    file = open("log/log.txt", 'a')
                    file.write("\n" + "Date Time  ==>>" + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + "\n")
                    file.write("Email      ==>>" + email + "\n")
                    file.write("IP Address ==>>" + ip_address + "\n")
                    file.write("Login Status ==>>" + "Login Fail" + "\n")
                    file.write("________________________________________")
                    file.close()
                    subject = f"Too many failed login attempts"
                    body = f"too many field login attempts from {ip_address}"
                    email = EmailMessage(subject,body, to=["sachinnihcas373@gmail.com"])
                    email.send()
                    return render(request, 'email_app.html', {"message": "Too_many_failed_login"})
        except:
            pass
    return render(request,'email_app.html')