from django.urls import path
from .views import post_list, post_detail
from . import views

urlpatterns = [
    # Your existing URL patterns
    path('', post_list, name='post_list'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    # Add the contact URL pattern here
    path('contact_us/<int:post_id>/', views.contact_us, name='contact_us'),
]
