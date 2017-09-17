from django.conf.urls import url, include
from django.contrib import admin
from umadko import views

urlpatterns = [

    url(r'^index/$',views.index),
    url(r'^register/$',views.register),
    url(r'^form/$',views.form_ht),
    url(r'^dashboard/$',views.dashboard),
    url(r'^tab-panel/$', views.tab_panel),
    url(r'^chart/$',views.chartindex),
    #url(r'^table/$', views.table_func),
    url(r'^skills/$', views.skills_func),
    url(r'^submit/$', views.submit_func),
]
