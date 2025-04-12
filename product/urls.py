from django.contrib import admin
from django.urls import path,include
from product import views
urlpatterns = [
    path('',views.index,name = 'index' ),
    path('create/',views.create_game,name ='create'),
    path('delete/<int:id_game>',views.delete_game,name = 'delete'),
    path('detail/<int:id_product>',views.detail,name = 'detail')
]