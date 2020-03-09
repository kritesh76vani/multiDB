"""SysProj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from CustomUsers import views as reg_view
from django.contrib.auth import views as auth_views
from Products import views as product_view
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', reg_view.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', reg_view.signup, name='signup'),
    url(r'^db-list/$', product_view.ViewAllDB.as_view(), name='show_db'),
    # url(r'^creat-product/$', product_view.CreateProduct.as_view(), name='create_product'),
    url(r'^creat-product/\w+/$', product_view.CreateProduct.as_view(), name='create_product'),
]