
from django.conf.urls import url
from django.contrib import admin

from app.views import tab_search_view, tab_detail_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', tab_search_view, name="tab_list_view"),
    url(r'^(?P<url>.+)', tab_detail_view, name="tab_detail_view")
]
