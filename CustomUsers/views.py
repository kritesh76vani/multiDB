from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from CustomUsers.forms import SignUpForm
from django.core.mail import send_mail, EmailMultiAlternatives
from SysProj.settings import EMAIL_HOST_USER


@login_required
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            try:
                subject, from_email, to = 'DATABASE MANAGEMENT SYSTEM', EMAIL_HOST_USER, email
                text_content = 'Here is your login crediantials : username "{0}" and  password "{1}"'.format(username,raw_password)
            
                html_content = ""
                msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()
            except Exception as e:
                pass
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})