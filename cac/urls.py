from django.urls import path
from . import views

urlpatterns = [
    path('hola/',views.hola),
    path('saludar/<str:nombre>/',views.saludar),
    path('saludar/',views.saludar ),
    path('proyectos/<int:anio>/<int:mes>',views.ver_proyectos,name="ver_proyectos" ),
]
