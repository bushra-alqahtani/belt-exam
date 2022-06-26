from django.urls import path
from . import views


urlpatterns=[
    path('',views.index),
    path('register',views.register),
    path('success',views.success),
    path('login',views.login),
    path('logout',views.logout),
    path('toadd',views.addntn),
    path('additem',views.additem),
    path('items/<int:id>',views.show_item),
    path('wish/<int:id>',views.wish_item),
    path('unwish/<int:id>',views.unwish_item),
]