from django.urls import path,include,re_path
from django.urls.resolvers import URLPattern
from pages.views import (index,
                        SignUpPageView,
                        pages,
                        manage_vehicle,
                        view_records,
                        manage_traffic_police,
                        manage_system_admin,
                        add_vehicle,
                        add_vehicle_save,
                        edit_vehicle,
                        edit_vehicle_save,
                        delete_vehicle,
                        admin_profile,
                        admin_profile_update,
                        add_traffic_police
                        )

urlpatterns = [
    path('api/rest-auth/',include("rest_auth.urls")),
    path('',index,name='home'),
    path('signup/', SignUpPageView.as_view(), name = 'register'),
    path('manage_vehicle/',manage_vehicle, name = 'manage_vehicle'),
    path('add_vehicle/',add_vehicle, name = 'add_vehicle'),
    path('add_vehicle_save',add_vehicle_save, name = 'add_vehicle_save'),
    path('edit_vehicle/<vehicle_id>',edit_vehicle, name = 'edit_vehicle'),
    path('edit_vehicle_save/', edit_vehicle_save, name = 'edit_vehicle_save'),
    path('delete_vehicle/<vehicle_id>', delete_vehicle, name = 'delete_vehicle'),
    path('view_records/',view_records, name ='view_records'),
    path('manage_traffic_police/',manage_traffic_police, name = 'manage_traffic_police'),
    path('manage_system_admin/',manage_system_admin, name = 'manage_system_admin'),
    path('admin_profile', admin_profile, name = 'admin_profile'),
    path('admin_profile_update', admin_profile_update, name = 'admin_profile_update'),
    path('add_traffic_police', add_traffic_police, name = 'add_traffic_police'),
    re_path(r'^.*\.*', pages, name='pages'),

    
]