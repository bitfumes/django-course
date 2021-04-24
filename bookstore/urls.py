from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('book/', include('books.urls')),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True)),
    path('', include('django.contrib.auth.urls')),
]
