from django.urls import path
from . import views

app_name = 'nota_fiscal'
urlpatterns = [
    path('nota_fiscal/', views.consulta_email, name='consulta email'),
]