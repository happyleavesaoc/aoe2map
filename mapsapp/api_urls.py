from django.urls import path

from . import views, api

app_name = 'api'
urlpatterns = [
    path('version', api.version, name='version'),
    path('status', api.status, name='status'),
    path('maps', api.maps, name='maps'),
    path('mymaps', api.mymaps, name='mymaps'),
    path('rms/<uuid:rms_id>', api.rms, name='rms'),
    path('rms/s/<name>', api.rms_by_name, name='rms_by_name'),
    path('collection/<uuid:collection_id>/maps', api.collection, name='collection'),
]