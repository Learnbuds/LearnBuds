from django.contrib import admin
from django.urls import path,include
from django.conf.urls import handler400,handler403,handler404,handler500

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',include('U_Auth.urls')),
    path('',include('ErrHandler.urls')),
    path('',include('Core.urls')),
    path('Dating/',include('Dating.urls')),
    path('Matrimony/',include('Matrimony.urls')),
    path('JobPortal/',include('JobPortal.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler400 = 'ErrHandler.views.error_400'
handler403 = 'ErrHandler.views.error_403'
handler404 = 'ErrHandler.views.error_404'
handler500 = 'ErrHandler.views.error_500'
