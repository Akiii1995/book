"""B6_Book URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path

from Book_App import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/",views.homepage,name="homepage"),
    path('show-all-books/',views.show_all_books,name="show_all_books"),
    path('edit/<int:id>',views.edit_data,name="edit"),
    path('delete/<int:id>',views.delete_data,name="delete"),
    path('delete-books',views.delete_all_books,name="delete-books"),
    path('soft-delete/<int:id>',views.soft_delete_data,name="soft delete"),
    path('json',views.Restore_All_Data,name='json'),

    
    
    
    
         
]
