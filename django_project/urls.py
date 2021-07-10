"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views #can import multiple views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/',
        auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
        name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
            auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
            name='password_reset_confirm'),
    path('password-reset/done/',
            auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
            name='password_reset_done'),
    path('password-reset-complete',
            auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
            name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#place to set up the mapping from certain urls to where we send the user
#ex. if we go the site and go to the route admin, it sends us to admin.site.urls
#the logic in admin.site.urls allows the /admin/ page to work correctly
#if we go to /blog, then it maps to blog urls
#login and logout django gave us, handles the logic and form stuff, but it does not handle the templates
