from django.contrib import admin
from django.urls import path
from Home import views


urlpatterns = [
    path('', views.index, name="home"),
    path('Home', views.index, name="home"),
    path('Analysis', views.analysis, name="analysis"),
    path('MIES', views.mies, name="mies"),
    path('MPW', views.mpw, name="mpw"),
    path('MPWWP', views.mpwwp, name="mpwwp"),
    path('SM', views.sm, name="sm"),
    path('DAWT', views.dawt, name="dawt"),
    path('RDPS', views.rdps, name="rdps"),
    path('HSOI', views.hsoi, name="hsoi"),
    path('Prediction', views.prediction, name="prediction"),
    path('BeforeToss', views.beforetoss, name="beforetoss"),
    path('BTResult', views.btresult, name="btresult"),
    path('AfterToss', views.aftertoss, name="aftertoss"),
    path('ATResult', views.atresult, name="atresult"),
]
