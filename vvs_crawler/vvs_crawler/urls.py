from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'vvs_crawler.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^admin/', admin.site.urls)
    
]
