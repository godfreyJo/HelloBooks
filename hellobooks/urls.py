from django.urls import path, include
from django.contrib import admin
from django.urls import path

urlpatterns = [
	path('', include('pages.urls')),
	path('listings/', include('listings.urls')),
	path('accounts/', include('accounts.urls')),
	path('contacts/', include('contacts.urls')),
    path('admin/', admin.site.urls),
    
]
