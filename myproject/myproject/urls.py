from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from firstapp.views import index
from firstapp.views import display
from firstapp.views import delete
# from firstapp.views import update
from firstapp.views import update_now,update


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',index),
    url(r'^index$',index),
    url(r'^display$',display),
    url(r'^delete/(\d+)$',delete),
    url(r'^update_now/(\d+)$',update_now),
    url(r'^update/(\d+)$',update),
    # url(r'^update$',update),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
