"""crimeproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from crimeapp import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static





urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),

    path('st_login/',views.st_login),
    
    path('login_process/',views.login_process),            #st_login/police_home/
    path('st_login/',views.st_login),        # login form repeat call b/c login fail

    path('officer_login/',views.officer_login),
    path('save_officer_login/',views.save_officer_login),

    path('officer_reg_html/',views.officer_reg_html),




    #path('station_reg_html/',views.station_reg_html),
    path('station_reg_html/',views.station_reg_html),  # Station regisration repeat call after login fail
    path('station_reg/',views.station_reg),
    
    path('fir_reg/',views.fir_reg),
    path('save_fir_reg/',views.save_fir_reg),

    path('view_criminal/',views.view_criminal),
   # path("criminal_search/", views.criminal_search),
    path('criminal_search/',views.criminal_search),

    path('view_criminal/',views.all_criminal),
    path('all_criminal/',views.all_criminal),

    path('criminal_search/',views.criminal_search),


    path('delete/<int:fir_id>',views.delete,name="delete"),
    path('update/<int:fir_id>',views.update,name="update"),
    path('more/<int:fir_id>',views.more),
    path('do_update/<int:fir_id>',views.do_update),



    path('criminal_back/',views.criminal_back),

    path('graphical/', views.index, name='index'),
    path('graph_data/',views.graph_data),
    path("graph_from_html/",views.graph_from_html),


    path('gallary/',views.gallary1),
    path('printed_gallary/',views.printed_gallary),
    path('photo_gallery/',views.photo_gallery),
    

    # Public section
    path('online_complaint/',views.online_complaint),
    path('save_comp_reg/',views.save_comp_reg),
    path('viewcomplaint/<str:comp_station>',views.viewcomplaint),
    path('comp_delete/<int:comp_id>',views.comp_delete),
    path('comp_add_fir/<int:comp_id>',views.comp_add_fir),
    path('comp_more/<int:comp_id>',views.comp_more),
    path('public_alert/',views.public_alert),


    #path('pdf/', views.GeneratePdf),


    path('public_login/',views.public_login),
    path('user_registration/',views.user_registration),
    path('save_user/',views.save_user),
    path('char_certificate/',views.char_certificate),
    path('char_reg/',views.char_reg),
    path('demo',include('crimeapp.urls')),

    path('feedback/',views.feedback),
    path('save_feedback/',views.save_feedback),
    path('view_feedback/<str:st_name>',views.view_feedback),

    path('manage_staff/<str:st_name>',views.manage_staff),
    path('insert_new_staff/',views.insert_new_staff),
    path('update_staff/',views.update_staff),
    path('doupdateStaff/',views.doupdateStaff),
    path('measing_people/',views.measing_people),
    path('insert_missing/',views.insert_missing), 
    path('insert_messing_people/',views.insert_messing_people), 

    path('save_update_staff/<str:insert_staff_adhar>',views.save_update_staff),
    path('view_staff/',views.view_staff),


    path('pdf/', views.GeneratePdf.as_view())

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)