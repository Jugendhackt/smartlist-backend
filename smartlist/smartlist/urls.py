from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from backend import views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^$',                                                                                
        TemplateView.as_view(template_name='index.html'),                                      
        name='home'),           
    path('user/lists', views.ShoppingListsOfUser.as_view()),
    url(r'^lists/(?P<pk>[0-9]+)/$', views.ShoppingLists.as_view()),
    url(r'^lists/[0-9]+/entries/$', views.Entries.as_view()),
    #url(r'^lists/[0-9]+/entries/(?P<pk>[0-9]+)/$', views.EntriesDetail.as_view()),
]
