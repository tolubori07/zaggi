from django.urls import path

from. import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/',views.loginpage,name='login'),
    path('', views.home, name= 'home'),
    path('market/', views.all, name = 'all'),
    path('item/<str:item_id>/', views.view, name = 'view'),
    path('bag/',views.bag, name = 'bag'),
    path('sign-up/', views.registerpage, name = 'signup'),
    path('logout/',views.logoutuserpage, name="logout"),
    path('checkout/',views.checkout, name = 'checkout'),
    
]
