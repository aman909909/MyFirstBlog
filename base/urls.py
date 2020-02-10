from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.home,name="home_page"),
    path('new/',views.new,name="new_page"),
    path('submit/',views.sub,name="submit_page"),
    path('show/',views.show,name="show_page"),
    path('showdetail/<int:k>',views.showdetail,name="show_detail"),
    path('delete/<int:z>',views.delete,name="delete"),
    path('search/',views.search,name="search"),
    path('deletepage/<int:z>',views.delp,name="delete_page"),
 #path('showdetail/<int:k>/comment/',views.showcomment,name="comment_page"),
   # path('showdetail/<int:k>/comment/show_comment/',views.showcomment,name="show_comment"),

]
