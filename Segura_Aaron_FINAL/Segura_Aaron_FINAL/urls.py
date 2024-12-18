from django.urls import path
from Segura_Aaron_FINALAPP import views

urlpatterns = [
    path('', views.index, name='index'),
    path('formulario-inscripciones/', views.formulario_inscripciones, name='formulario_inscripciones'),
    path('listar-inscripciones/', views.listar_inscripciones, name='listar_inscripciones'),
    path('editar-inscripcion/<int:pk>/', views.editar_inscripcion, name='editar_inscripcion'),
    path('eliminar-inscripcion/<int:pk>/', views.eliminar_inscripcion, name='eliminar_inscripcion'),
    path('formulario-instituciones/', views.formulario_instituciones, name='formulario_instituciones'),
    path('listar-instituciones/', views.listar_instituciones, name='listar_instituciones'),
    path('editar-institucion/<int:pk>/', views.editar_institucion, name='editar_institucion'),
    path('eliminar-institucion/<int:pk>/', views.eliminar_institucion, name='eliminar_institucion'),
    path('api/inscritos/', views.InscritosListCreateAPIView.as_view(), name='api_inscritos'),
    path('api/inscritos/<int:pk>/', views.InscritosDetailAPIView.as_view(), name='api_inscrito_detail'),
    path('api/instituciones/', views.instituciones_list, name='api_instituciones'),
    path('api/instituciones/<int:pk>/', views.institucion_detail, name='api_institucion_detail'),
    path('api/autor/', views.autor_info, name='autor_info'),
]
