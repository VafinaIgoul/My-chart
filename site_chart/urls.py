from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from chart.api import DataResource
from chart import views
from chart.models import Data

v1_api = Api(api_name='v1')
v1_api.register(DataResource())

urlpatterns = [
    url(r'^chart/$', views.IndexView.as_view(), name = 'index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
    url(r'^$', views.import_sheet, name='import_sheet')
]
