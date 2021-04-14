from django.conf.urls import url
from ServiceApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^service/$', views.serviceApi),
    url(r'^service/([0-9]+)$', views.serviceApi),

    url(r'^listing/$', views.listingApi),
    url(r'^listing/([0-9]+)$', views.listingApi),

    url(r'^vendor/$', views.vendorApi),
    url(r'^vendor/([0-9]+)$', views.vendorApi),

    url(r'^SaveFile$', views.SaveFile)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)