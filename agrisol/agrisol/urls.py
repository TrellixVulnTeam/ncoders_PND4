"""agrisol URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("email",views.Email,name="email"),
    #path("farmer",views.farmer,name="farmer"),
    path("farmer/",include("farmer.urls",namespace="cust_sell")),
    path("cust_sell/",include("cust_sell.urls",namespace="cust_sell")),
    path("accounts/",include("accounts.urls",namespace="accounts")),
    path("hepline/",include("helpline.urls",namespace="helpline")),
    path("household/",include("household.urls",namespace="household")),
    path("logout",views.log_out,name="log_out"),
    path("signup", views.sign_up, name="sign_up"),
]
