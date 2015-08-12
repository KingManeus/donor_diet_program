from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.identification, name='identification'),
    url(r'vitamins/$', views.vitamins, name='vitamins'),
    url(r'genq/$', views.genq, name='genq'),
    url(r'dairy/$', views.dairy, name='dairy'),
    url(r'fruits/$', views.fruits, name='fruits'),
    url(r'vegetables/$', views.vegetables, name='vegetables'),
    url(r'eggsmeat/$', views.eggsmeat, name='eggsmeat'),
    url(r'carbs/$', views.carbs, name='carbs'),
    url(r'beverages/$', views.beverages, name='beverages'),
    url(r'sweetsetc/$', views.sweetsetc, name='sweetsetc'),
    url(r'genq2/$', views.genq2, name='genq2'),
    
]
