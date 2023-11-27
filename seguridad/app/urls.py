from django.urls import path
from .views  import *

urlpatterns = [
    path('', login_view, name='login'),
    path('crear_usuario/', crear_usuario, name="crear_usuario"),
    path('listar_usuario/', listar_usuario, name='listar_usuario'),
    
]
