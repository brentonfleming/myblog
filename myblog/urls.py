from django.contrib import admin
from django.urls import path, include
from blog import views  # Import your views module

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('contact/', views.contact_us, name='contact_us'),  # Updated URL pattern for contact page
]
