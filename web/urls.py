from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    
    url(r'^$', 'web.views.home', name='web_home'),
    url(r'^peticiones$', 'web.views.peticiones', name='web_peticiones'),
    url(r'^nueva_partida$', 'web.views.nueva_partida', name='web_nueva_partida'),
    url(r'^partidas_empezadas$', 'web.views.partidas_empezadas', name='web_partidas_empezadas'),
    url(r'^partida/(?P<partida>\d+)$', 'web.views.partida', name='web_partida'),
    url(r'^nuevo_usuario$', 'web.views.nuevo_usuario', name='web_nuevo_usuario'),
    url(r'^clasificacion$', 'web.views.clasificacion', name='web_clasificacion'),
)
