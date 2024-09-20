from django.shortcuts import render,redirect
from django.views.generic import FormView
from .forms import UserRegistrationForm,UserUpdateForm
from django.contrib.auth import login,logout,update_session_auth_hash
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView
from django.views import View
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm

# Create your views here.
class UserRegistrationView(FormView):
    template_name='accounts/user_registration.html'
    form_class=UserRegistrationForm
    success_url=reverse_lazy('register')

    def form_valid(self,form):
        print(form.cleaned_data)
        user=form.save()
        login( self.request,user)
        print(user)
        return super().form_valid(form)

    def form_invalid(self, form):
        print("Form is invalid")
        print(form.errors)  # Print out form errors to see what's going wrong
        return super().form_invalid(form)    

class UserLogInView(LoginView):
    template_name='accounts/user_login.html'
    def get_success_url(self):
        return reverse_lazy('profile')
        

class UserLogOutView(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('home')
        
class UserBankAccountUpdateView(View):
    template_name = 'accounts/profile.html'

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the user's profile page
        return render(request, self.template_name, {'form': form})            
   
def PasswordChange(request):
    if request.method=='POST':
        form=PasswordChangeForm(request.user,data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"PassWord Updated Successlly")  
            update_session_auth_hash(request,form.user)
            return redirect('profile')  
    else:
        form=PasswordChangeForm(user=request.user)
    return render(request,'accounts/password.html',{'form':form}) 
