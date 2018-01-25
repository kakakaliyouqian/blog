"""kk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import include, path
from .custom_site import custom_site
from django.conf.urls import url
from blog.views import IndexView, CategoryView, TagView, PostView
from blog import views



urlpatterns = [

    path('admin/', admin.site.urls),
    path('cus_admin/', custom_site.urls),
    #url(r'^admin/', admin.site.urls),
    #url(r'^cus_admin/', custom_site.urls),
    path('', views.IndexView.as_view(), name='home'),
    url(r'^category/(?P<category_id>\d+)/', CategoryView.as_view(), name="category"),
    url(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name="tag"),
    url(r'^post/(?P<pk>\d+)/$', PostView.as_view(), name="detail"),

]
