from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import RedirectView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from web.forms import login_helper

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'barquitos.views.home', name='home'),
    # url(r'^barquitos/', include('barquitos.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', RedirectView.as_view(url='/barcos/web/', permanent=False), name='barquitos_home'),
    url(r'^servidor/', include('servidor.urls')),
    url(r'^web/', include('web.urls')),
    
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'extra_context': {'login_helper': login_helper}}, name='auth_login'),
    #url(r'^accounts/login/$', 'mysite.accounts.views.signup', {'extra_context': {'login_helper': login_helper}}, name='auth_signup'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', name='auth_logout'),
    url(r'^accounts/profile/$', RedirectView.as_view(url='/barcos/web/', permanent=False), name='home2'),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
