from django.contrib import admin
from django.urls import path, include

# URL configurations for the BuildMart project
urlpatterns = [
    # Admin site URLs
    path('admin/', admin.site.urls),
    
    # Include URL configurations from the shop application
    path('shop/', include('shop.urls')),
    # The 'shop.urls' module should define paths specific to the shop application,
    # such as listing products, viewing product details, etc.
]