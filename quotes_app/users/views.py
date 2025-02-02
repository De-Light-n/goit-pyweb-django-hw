from django.shortcuts import redirect, render
from django.views import View
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

from .forms import SignUpForm
# Create your views here.


class SignUpView(View):
    template_name = "users/signup.html"
    form_class = SignUpForm
    
    def get(self, request):
        return render(request, self.template_name, context={"form":self.form_class})
    
    def post(self, request):
        if request.user.is_authenticated:
            return redirect(to='quotes:main')
        
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="quotes:main")
        else:
            messages.info(request, "шось не так")
            return render(request, 'users/signup.html', context={"form": form})
      
@login_required
def logoutuser(request):
    logout(request)
    return redirect(to='quotes:main')  
     
class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    html_email_template_name = 'users/password_reset_email.html'
    success_url = reverse_lazy('users:password_reset_done')
    success_message = "An email with instructions to reset your password has been sent to %(email)s."
    subject_template_name = 'users/password_reset_subject.txt'   
            