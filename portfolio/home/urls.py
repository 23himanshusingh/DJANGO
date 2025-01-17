from django.contrib import admin
from django.urls import path, include
from home import views


#django admin header customization

admin.site.site_header = "Login to Developer Himanshu"
admin.site.site_title = "Welcome to Himanshu's Dashboard"
admin.site.index_title = "Welcome to this portal"
urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('projects', views.projects, name='projects')
]
