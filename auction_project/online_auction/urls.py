from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.landing,name="landing"),
    path('register/',views.register,name="register"),
    path('login/',views.login_view,name="login"),
    path('listings/',views.Listings_view,name="listings"),
    path('item/',views.item,name="item_listed"),
    path('auth_failed/',views.auth_failed,name="auth_failed"),
]