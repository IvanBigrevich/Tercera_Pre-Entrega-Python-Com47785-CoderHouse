from django.urls import path
from App_Cursos.views import crear_curso, show_html, mostrar_cursos, crear_curso_form, busqueda_camada

urlpatterns = [
    path('agregar_curso/', crear_curso),
    path('curso/', crear_curso_form),
    path('buscar/', busqueda_camada),
    path('show/', show_html),
    path('cursos/', mostrar_cursos),
]
