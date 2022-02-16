from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as authlogin, logout as authlogout, authenticate
from question.models import questionCategory
from django.contrib.auth.forms import UserCreationForm
from .form import userform


class LoginPage(View):
    template_name='login.html'
    form_class=AuthenticationForm
    questionCategories=questionCategory.objects.all()

    def get(self, request):
        forms=self.form_class()
        context={
            'questionCategories':self.questionCategories,
            'form':forms,
            'next':request.GET.get('next'),
        }

        return render(request, self.template_name, context)
    
    def post(self, request):
        form=self.form_class(data=request.POST)
        if form.is_valid():
            authlogin(request,form.get_user())
            return redirect("HomePage")
        context={
            'questionCategories':self.questionCategories,
            'form':form,
        }

        return render(request, self.template_name, context)

def LogoutPage(request):
    authlogout(request)
    return redirect("HomePage")

class CreateAccount(View):

    template_name='create-account.html'
    form_class= UserCreationForm
    questionCategories=questionCategory.objects.all()

    def get(self, request):
        form=self.form_class()
        context={
            'questionCategories':self.questionCategories,
            'form':form,
        }
        return render(request, self.template_name, context)
        
    def post(self, request):
        form=self.form_class(data=request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            user=authenticate(username=username, password=password)
            authlogin(request,user)
        return redirect("updateProfile")

class updateProfile(View):

    template_name='update-profile.html'
    questionCategories=questionCategory.objects.all()
    form_class=userform


    def get(self, request):
        form=self.form_class()
        context={
            'questionCategories':self.questionCategories,
            'form':form,
        }
        return render(request, self.template_name, context)
    def post(self, request):
        form=self.form_class(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("HomePage")
        form=self.form_class()
        context={
            'questionCategories':self.questionCategories,
            'form':form,
        }
        return render(request, self.template_name, context)