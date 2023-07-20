from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from allauth.exceptions import ImmediateHttpResponse
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

def social_login(request):
    if request.method == 'POST':
        # Here, you can handle the form submission for social authentication
        # For example, you can use 'django-allauth' signals to process the authentication

        # For demonstration purposes, let's assume the social authentication is successful
        social_login_success = True

        if social_login_success:
            return redirect('/profile/')
        else:
            # If social authentication failed, you can display a message or handle the error
            return render(request, 'app/social_media.html', {'message': 'Social authentication failed. Please try again.'})

    return render(request, 'app/social_media.html')
class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def get_connect_redirect_url(self, request, socialaccount):
        # Customize the redirect URL after a successful social login
        return '/login/'  # Replace this with your desired URL

    def pre_social_login(self, request, sociallogin):
        # Check if the email is already associated with a regular account
        email = sociallogin.user.email
        existing_user = User.objects.filter(email=email).first()

        if existing_user and not sociallogin.is_existing:
            # If a regular account exists with the same email, handle the conflict
            raise ImmediateHttpResponse(
                render(request, 'app/social_media.html', {'message': 'An account with this email already exists. Please log in using your regular account.'})
            )

