from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("feed", views.feed_view, name="feed"),
    
    path("register", views.register_view, name="register"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    
    path("user_profile/<str:primary_key>", views.user_profile_view, name="user_profile"),
    path("update_user_profile", views.update_user_profile_view, name="update_user_profile"),
    path("delete_user_profile", views.delete_user_profile_view, name="delete_user_profile"),
    
    path("excuses", views.excuses_view, name="excuses"),
    path("excuses/<str:primary_key>", views.excuse_view, name="excuse"),
    
    path("excuses/categories", views.excuse_categories_view, name="excuse_categories"),
    path("excuses/categories/<str:primary_key>", views.excuse_category_view, name="excuse_category"),

    path("create_excuse", views.create_excuse_view, name="create_excuse"),
    path("update_excuse/<str:primary_key>", views.update_excuse_view, name="update_excuse"),
    path("delete_excuse/<str:primary_key>", views.delete_excuse_view, name="delete_excuse"),
    
]