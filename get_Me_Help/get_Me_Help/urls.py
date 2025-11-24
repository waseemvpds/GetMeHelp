"""get_Me_Help URL Configuration

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
from django.urls import path

from MYAPP import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('view_fuel_provider',views.view_fuel_provider),
    path('approved__fuel_provider',views.approved__fuel_provider),
    path('view_mechanic',views.view_mechanic),
    path('view_approved_mechanic',views.view_approved_mechanic),
    path('send_reply/<id>',views.send_reply),
    path('send_reply_post/<id>',views.send_reply_post),
    path('view_feedback',views.view_feedback),
    path('view_complaint',views.view_complaint),
    path('view_rating',views.view_rating),
    path('view_user',views.view_user),
    path('',views.log),
    path('log_post',views.log_post),
    path('approve_fuel_provider/<id>',views.approve_fuel_provider),
    path('approve_mechanic/<id>',views.approve_mechanic),
    path('reject_fuel_provider/<id>',views.reject_fuel_provider),
    path('reject_mechanic/<id>',views.reject_mechanic),
    path('admin_home',views.admin_home),
    path('logout',views.logout),
    path('Adding_Fuel_Price',views.Adding_Fuel_Price),
    path('Fuel_Price_Edit/<id>',views.Fuel_Price_Edit),
    path('Fuel_Price_View',views.Fuel_Price_View),
    path('Fuel_Provider_Profile_Manager',views.Fuel_Provider_Profile_Manager),
    path('Fuel_Provider_Payment_Table',views.Fuel_Provider_Payment_Table),
    path('Fuel_Provider_Rating',views.Fuel_Provider_Rating),
    path('Fuel_Provider_Register_Table',views.Fuel_Provider_Register_Table),
    path('Fuel_Provider_View_User_request',views.Fuel_Provider_View_User_request),
    path('Fuel_Provider_Register_Table_post',views.Fuel_Provider_Register_Table_post),
    path('Fuel_Price_Edit_post/<id>',views.Fuel_Price_Edit_post),
    path('Fuel_Provider_Home',views.Fuel_Provider_Home),
    path('Adding_Fuel_Price_post',views.Adding_Fuel_Price_post),
    path('Delete_Fuel_Price/<id>',views.Delete_Fuel_Price),
    path('approve_user_request/<id>',views.approve_user_request),
    path('reject_user_request/<id>',views.reject_user_request),
    path('Fuel_Provider_Profile_Manager_post',views.Fuel_Provider_Profile_Manager_post),
    path('Fuel_Provider_Order_History',views.Fuel_Provider_Order_History),
    path('Fuel_Provider_trackOrder',views.Fuel_Provider_trackOrder),
    path('Mechanic_Home',views.Mechanic_Home),
    path('Mechanic_Add_Amount',views.Mechanic_Add_Amount),
    path('Mechanic_Edit_Amount/<id>',views.Mechanic_Edit_Amount),
    path('Mechanic_Manage_Profile',views.Mechanic_Manage_Profile),
    path('Mechanic_Payment_History',views.Mechanic_Payment_History),
    path('Mechanic_Register_Table',views.Mechanic_Register_Table),
    path('Mechanic_TrackOrder',views.Mechanic_TrackOrder),
    path('Mechanic_View_order_History',views.Mechanic_View_order_History),
    path('Mechanic_View_Service_Details',views.Mechanic_View_Service_Details),
    path('Mechanic_View_User_Request',views.Mechanic_View_User_Request),
    path('Mechanic_Rating',views.Mechanic_Rating),
    path('Mechanic_Register_Table_post',views.Mechanic_Register_Table_post),
    path('Mechanic_Manage_Profile_post',views.Mechanic_Manage_Profile_post),
    path('Mechanic_Add_Amount_Post',views.Mechanic_Add_Amount_Post),
    path('Mechanic_View_Amount',views.Mechanic_View_Amount),
    path('Mechanic_Edit_Amount_Post/<id>',views.Mechanic_Edit_Amount_Post),
    path('Mechanic_Delete_Amount/<id>',views.Mechanic_Delete_Amount),
    path('Mechanic_Request_Approve/<id>',views.Mechanic_Request_Approve),
    path('Mechanic_Request_Reject/<id>',views.Mechanic_Request_Reject),
    path('Mechanic_View_User_Request_Approved',views.Mechanic_View_User_Request_Approved),
    path('user_login',views.user_login),
    path('user_register',views.user_register),
    path('user_Manage_profile',views.user_Manage_profile),
    path('user_view_nearby_fuel_provider',views.user_view_nearby_fuel_provider),
    path('user_book_fuel',views.user_book_fuel),
    path('user_view_nearby_mechanic',views.user_view_nearby_mechanic),
    path('user_book_mechanic',views.user_book_mechanic),
    path('user_view_fuel_booking_status',views.user_view_fuel_booking_status),
    path('user_view_mechanic_booking_status',views.user_view_mechanic_booking_status),
    path('user_make_payment',views.user_make_payment),
    path('user_payment_history',views.user_payment_history),
    path('user_network_call_with_fuel_provider',views.user_network_call_with_fuel_provider),
    path('user_network_call_with_worker',views.user_network_call_with_worker),
    path('user_send_feedback',views.user_send_feedback),
    path('user_send_complaint',views.user_send_complaint),
    path('user_view_reply',views.user_view_reply),
    path('user_rating',views.user_rating),
    path('mechaic_rating',views.mechaic_rating),
    path('book_mechanic',views.book_mechanic),
    path('book_fuel_provider',views.book_fuel_provider),
    path('view_fuelprice',views.view_fuelprice),
    path('edit_profile',views.edit_profile),
    path('online_payment',views.online_payment),
    path('offline_payment',views.offline_payment),
    path('offline_payment_mech',views.offline_payment_mech),
    path('online_payment_mech',views.online_payment_mech),

    path('chatt/<u>', views.chatt),
    path('chatsnd', views.chatsnd),
    path('chatrply', views.chatrply),

    path('chatt_m/<u>',views.chatt_m),
    path('chatsnd_m',views.chatsnd_m),
    path('chatrply_m',views.chatrply_m),

    path('fuel_add_chat',views.fuel_add_chat),
    path('fuel_view_chat',views.fuel_view_chat),


    path('mech_add_chat',views.mech_add_chat),
    path('mech_view_chat',views.mech_view_chat),

    path('user_view_services',views.user_view_services),
    path('update_location',views.update_location),









]