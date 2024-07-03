from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from app.views import ReactView, ContactView  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('drawings/', ReactView.as_view(), name='react-view'),  
    path('contact/', ContactView.as_view(), name='contact-list-create'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
