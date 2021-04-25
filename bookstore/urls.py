from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('book/', include('books.urls')),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True)),
    path('', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
