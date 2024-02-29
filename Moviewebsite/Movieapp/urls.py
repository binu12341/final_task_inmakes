from . import views
from django.urls import path

urlpatterns = [
    path('',views.login,name='login'),
    path('index/',views.index,name='index'),
    path('register',views.register,name='register'),
    path('user_profile',views.user_profile,name='user_profile'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('back/',views.back,name='back'),
    path('add/',views.add_movie,name='add_movie'),
    path('allMov',views.allMov,name='allMov'),
    path('<slug:c_slug>/',views.MovDetail,name='category_slug'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('cancel/<int:id>/',views.cancel,name='cancel'),
    path('SearchResult',views.SearchResult,name='SearchResult'),
    path('logout',views.logout,name='logout'),
]