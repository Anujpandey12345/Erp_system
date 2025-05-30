"""
URL configuration for CodingIndiaErp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from CodingIndiaErp.views import SignUpView, LoginView, LogOut, verifyOTP, verifyLoginOTP

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('erp.urls')),
    path('project/', include('project.urls')),
    path('Employee/', include('Employee.urls')),

    # For signup
    path('signup/', SignUpView, name='signup'),
    path('login/', LoginView, name='loginview'),
    path('logout/', LogOut, name='logout'),
    path('verifyEmail/', verifyOTP, name='verifyEmail'),
    path('verifyLogin/', verifyLoginOTP, name='verifyLogin')

    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)