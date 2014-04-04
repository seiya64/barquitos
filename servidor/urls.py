from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'barquitos.views.home', name='home'),
    # url(r'^barquitos/', include('barquitos.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', 'servidor.views.home', name='servidor_home'),
    url(r'^tramitar_peticiones_partidas$', 'servidor.views.tramitar_peticiones_partidas', name='servidor_tramitar_peticiones_partidas'),
    url(r'^peticion_nueva_partida$', 'servidor.views.peticion_nueva_partida', name='servidor_peticion_nueva_partida'),
    url(r'^obtener_tableros/(?P<partida>\d+)$', 'servidor.views.obtener_tableros', name='servidor_obtener_tableros'),
    url(r'^atacar/(?P<partida>\d+)$', 'servidor.views.atacar', name='servidor_atacar'),
    url(r'^abandonar/(?P<partida>\d+)$', 'servidor.views.abandonar', name='servidor_abandonar'),
)
