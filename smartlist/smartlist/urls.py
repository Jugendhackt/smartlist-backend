from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^$',                                                                                
        TemplateView.as_view(template_name='index.html'),                                      
        name='home'),           
]
