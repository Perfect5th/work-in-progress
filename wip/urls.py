from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from django_nyt.urls import get_pattern as get_nyt_pattern

from wiki.urls import get_pattern as get_wiki_pattern

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^notifications/', get_nyt_pattern()),
    url(r'', get_wiki_pattern()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
